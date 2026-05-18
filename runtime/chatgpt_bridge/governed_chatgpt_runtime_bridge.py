"""Bounded ChatGPT-style relay into the governed localhost runtime."""

from __future__ import annotations

from typing import Callable

from sapianta_system.runtime.operator.cli import invoke_preview_runtime

from .governed_chatgpt_bridge_request import create_chatgpt_bridge_request
from .governed_chatgpt_bridge_response import create_chatgpt_bridge_response
from .governed_chatgpt_bridge_validator import validate_chatgpt_bridge_request


def invoke_from_chatgpt_bridge(
    artifact: str,
    host: str = "127.0.0.1",
    port: int = 8110,
    *,
    transport: Callable[[dict, str, int], dict] | None = None,
) -> dict:
    request = create_chatgpt_bridge_request(artifact=artifact, host=host, port=port)
    validation = validate_chatgpt_bridge_request(request)
    if not validation["valid"]:
        return {"status": "BLOCKED", "validation": validation, "bridge_request": request}
    operator_result = invoke_preview_runtime(artifact=artifact, host=host, port=port, transport=transport)
    if not operator_result.get("valid"):
        return {
            "status": "BLOCKED",
            "validation": {"valid": False, "errors": operator_result.get("errors", [])},
            "bridge_request": request,
        }
    return create_chatgpt_bridge_response(
        bridge_request=request,
        operator_summary=operator_result["summary"],
    )
