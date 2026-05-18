"""Local-only governed runtime operator CLI."""

from __future__ import annotations

import argparse
import http.client
import json
import sys
from pathlib import Path
from typing import Any, Callable, Sequence

from .governed_operator_request import build_operator_request
from .governed_operator_response import summarize_operator_response
from .governed_operator_validator import validate_operator_response, validate_operator_target


def _print(value: dict[str, Any]) -> None:
    print(json.dumps(value, sort_keys=True))


def invoke_preview_runtime(
    *,
    artifact: str,
    host: str = "127.0.0.1",
    port: int = 8010,
    transport: Callable[[dict, str, int], dict] | None = None,
) -> dict:
    target_validation = validate_operator_target(host=host)
    if not target_validation["valid"]:
        return {"valid": False, "errors": target_validation["errors"], "status": "BLOCKED"}
    try:
        request = build_operator_request(artifact=artifact)
    except ValueError as exc:
        return {"valid": False, "errors": [{"field": "artifact", "reason": str(exc)}], "status": "BLOCKED"}
    try:
        response = transport(request, host, port) if transport is not None else _http_transport(request, host, port)
    except OSError:
        return {
            "valid": False,
            "errors": [{"field": "preview_runtime", "reason": "preview runtime unavailable"}],
            "status": "BLOCKED",
        }
    response_validation = validate_operator_response(response)
    if not response_validation["valid"]:
        return {"valid": False, "errors": response_validation["errors"], "status": "BLOCKED"}
    return {"valid": True, "summary": summarize_operator_response(response), "status": "RETURNED"}


def _http_transport(request: dict, host: str, port: int) -> dict:
    conn = http.client.HTTPConnection(host, port, timeout=5)
    body = json.dumps(request, sort_keys=True, separators=(",", ":"))
    conn.request("POST", "/governed-invoke", body=body, headers={"Content-Type": "application/json"})
    response = conn.getresponse()
    payload = json.loads(response.read().decode("utf-8"))
    conn.close()
    return payload


def validate_response_file(path: str) -> dict:
    try:
        response = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"valid": False, "errors": [{"field": "file", "reason": "malformed response file"}]}
    return validate_operator_response(response)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="governed_runtime_operator")
    subparsers = parser.add_subparsers(dest="command", required=True)
    invoke_parser = subparsers.add_parser("invoke")
    invoke_parser.add_argument("--artifact", required=True)
    invoke_parser.add_argument("--host", default="127.0.0.1")
    invoke_parser.add_argument("--port", type=int, default=8010)
    validate_parser = subparsers.add_parser("validate-response")
    validate_parser.add_argument("--file", required=True)
    args = parser.parse_args(list(argv if argv is not None else sys.argv[1:]))

    if args.command == "invoke":
        result = invoke_preview_runtime(artifact=args.artifact, host=args.host, port=args.port)
        _print(result["summary"] if result.get("valid") else result)
        return 0 if result.get("valid") else 1
    result = validate_response_file(args.file)
    _print(result)
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
