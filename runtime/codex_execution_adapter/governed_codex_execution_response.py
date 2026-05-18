"""Governed bounded Codex execution adapter responses."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from .governed_codex_execution_dispatch import dispatch_bounded_codex
from .governed_codex_execution_evidence import governed_codex_execution_evidence
from .governed_codex_execution_receipt import create_codex_execution_receipt
from .governed_codex_execution_replay import build_codex_execution_replay_identity
from .governed_codex_execution_validator import validate_codex_execution_request


def _status(errors: list[dict]) -> str:
    reasons = {error["reason"] for error in errors}
    if "expired authority" in reasons:
        return "AUTHORITY_EXPIRED"
    if "revoked authorization token" in reasons:
        return "AUTHORITY_REVOKED"
    if "handoff mismatch" in reasons:
        return "HANDOFF_MISMATCH"
    if "blocked capability detected" in reasons or "blocked capability mismatch" in reasons:
        return "BLOCKED_CAPABILITY_DETECTED"
    return "EXECUTION_REJECTED"


def execute_governed_codex(request: dict, *, runner: Callable[..., Any] | None = None) -> dict:
    validation = validate_codex_execution_request(request)
    if not validation["valid"]:
        dispatch = {
            "execution_status": "EXECUTION_REJECTED",
            "stdout": "",
            "stderr": "",
            "metadata": {
                "args": list(validation["command"]),
                "shell": False,
                "timeout_seconds": request.get("timeout_seconds"),
            },
        }
        execution_status = _status(validation["errors"])
    else:
        dispatch = dispatch_bounded_codex(
            command=validation["command"],
            timeout_seconds=request["timeout_seconds"],
            runner=runner or __import__("subprocess").run,
        )
        execution_status = dispatch["execution_status"]
    receipt = create_codex_execution_receipt(
        authority_token=request.get("authority_token", {}),
        execution_status=execution_status,
        validation=validation,
        dispatch=dispatch,
    )
    response = {
        "status": execution_status,
        "dispatch": dispatch,
        "receipt": receipt,
        "validation": validation,
    }
    response["replay_identity"] = build_codex_execution_replay_identity(request=request, validation=validation, dispatch=dispatch)
    if validation["valid"]:
        response["evidence"] = governed_codex_execution_evidence(
            request=request,
            validation=validation,
            dispatch=dispatch,
            receipt=receipt,
        )
    return response
