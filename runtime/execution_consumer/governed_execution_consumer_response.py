"""Mock-only governed execution consumer responses."""

from __future__ import annotations

from .governed_execution_consumer_dispatch import perform_mock_dispatch
from .governed_execution_consumer_evidence import governed_execution_consumer_evidence
from .governed_execution_consumer_receipt import create_consumer_receipt
from .governed_execution_consumer_replay import build_consumer_replay_identity
from .governed_execution_consumer_validator import validate_execution_consumer_request


def _receipt_status(errors: list[dict]) -> str:
    reasons = {error["reason"] for error in errors}
    if "expired authority" in reasons:
        return "AUTHORITY_EXPIRED"
    if "revoked authorization token" in reasons:
        return "AUTHORITY_REVOKED"
    if "handoff mismatch" in reasons:
        return "HANDOFF_MISMATCH"
    if "blocked capability detected" in reasons or "blocked capability mismatch" in reasons:
        return "BLOCKED_CAPABILITY_DETECTED"
    return "MOCK_EXECUTION_REJECTED"


def consume_execution_authority(request: dict) -> dict:
    validation = validate_execution_consumer_request(request)
    dispatch = perform_mock_dispatch() if validation["valid"] else {
        "dispatch_status": "MOCK_DISPATCH_REJECTED",
        "dispatch_mode": "DETERMINISTIC_PRE_EXECUTION_SIMULATION",
        "execution_performed": False,
    }
    receipt_status = "MOCK_EXECUTION_ACCEPTED" if validation["valid"] else _receipt_status(validation["errors"])
    receipt = create_consumer_receipt(
        authority_token=request.get("authority_token", {}),
        receipt_status=receipt_status,
        validation=validation,
        dispatch=dispatch,
    )
    response = {
        "status": receipt_status,
        "dispatch": dispatch,
        "receipt": receipt,
        "execution_performed": False,
        "validation": validation,
    }
    response["replay_identity"] = build_consumer_replay_identity(request=request, validation=validation, dispatch=dispatch)
    if validation["valid"]:
        response["evidence"] = governed_execution_consumer_evidence(request=request, validation=validation, receipt=receipt)
    return response
