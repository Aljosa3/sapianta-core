"""Read-only trace synthesis for governed execution."""

from __future__ import annotations

from sapianta_system.runtime.execution_gate.governed_execution_authorization_validator import validate_authority_token


def _authority_status(*, token: dict, now: str, revoked_token_ids: set[str]) -> tuple[str, str, str]:
    validation = validate_authority_token(token, now=now, revoked_token_ids=revoked_token_ids)
    reasons = {error["reason"] for error in validation["errors"]}
    expiration = "EXPIRED" if "expired authority" in reasons else "ACTIVE"
    revocation = "REVOKED" if "revoked authorization token" in reasons else "NOT_REVOKED"
    if validation["valid"]:
        return "AUTHORIZED", expiration, revocation
    if expiration == "EXPIRED":
        return "AUTHORITY_EXPIRED", expiration, revocation
    if revocation == "REVOKED":
        return "AUTHORITY_REVOKED", expiration, revocation
    return "AUTHORITY_INVALID", expiration, revocation


def build_execution_trace(*, request: dict, validation: dict, replay_identity: str) -> dict:
    token = request["authority_token"]
    package = request["handoff_package"]
    consumer = request["consumer_response"]
    adapter = request["adapter_response"]
    authorization_status, expiration_status, revocation_status = _authority_status(
        token=token,
        now=request["now"],
        revoked_token_ids=set(request.get("revoked_token_ids", [])),
    )
    return {
        "execution_trace_id": f"EXEC-TRACE-{replay_identity[:24]}",
        "replay_identity": replay_identity,
        "authority_token_id": token["token_id"],
        "task_class": package["task_class"],
        "governance_mode": package["governance_mode"],
        "authorization_status": authorization_status,
        "expiration_status": expiration_status,
        "revocation_status": revocation_status,
        "handoff_integrity_status": "PASS" if validation["valid"] else "FAIL",
        "consumer_receipt_status": consumer.get("status", "MISSING"),
        "adapter_receipt_status": adapter.get("status", "MISSING"),
        "execution_performed": adapter.get("status") == "EXECUTION_ACCEPTED",
        "stdout_hash": adapter["receipt"].get("stdout_hash", ""),
        "stderr_hash": adapter["receipt"].get("stderr_hash", ""),
        "blocked_capabilities": token.get("blocked_capabilities", []),
        "deterministic_closure_status": "PASS",
    }
