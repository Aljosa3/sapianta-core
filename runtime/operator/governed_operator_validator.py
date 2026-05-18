"""Fail-closed validation for governed operator CLI behavior."""

from __future__ import annotations

from sapianta_system.runtime.preview.governed_preview_runtime_request import LOCALHOST_HOST


def validate_operator_target(*, host: str) -> dict:
    if host != LOCALHOST_HOST:
        return {"valid": False, "errors": [{"field": "host", "reason": "localhost-only target required"}]}
    return {"valid": True, "errors": []}


def validate_operator_response(response: dict) -> dict:
    errors = []
    if response.get("status") != "RETURNED":
        errors.append({"field": "status", "reason": "runtime response not returned"})
    if response.get("closure") != "PASS":
        errors.append({"field": "closure", "reason": "runtime closure not passed"})
    for field in ("preview_runtime_request_id", "preview_runtime_response_id", "invocation_replay_identity"):
        value = response.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append({"field": field, "reason": "malformed response"})
    evidence = response.get("evidence")
    if not isinstance(evidence, dict) or evidence.get("response_returned") is not True:
        errors.append({"field": "evidence", "reason": "missing replay evidence"})
    for field in ("orchestration_present", "hidden_continuation_present", "hidden_execution_present", "hidden_mutable_state_present"):
        if evidence is not None and evidence.get(field) is not False:
            errors.append({"field": field, "reason": "hidden execution flags"})
    return {"valid": not errors, "errors": errors}
