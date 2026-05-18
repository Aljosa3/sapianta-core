"""Fail-closed validation for localhost preview runtime requests."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

from .governed_preview_runtime_request import LOCALHOST_HOST


def _missing_text(value: object) -> bool:
    return not isinstance(value, str) or not value.strip()


def validate_preview_binding(*, host: str) -> dict:
    if host != LOCALHOST_HOST:
        return {"valid": False, "errors": [{"field": "host", "reason": "localhost-only binding required"}]}
    return {"valid": True, "errors": []}


def validate_preview_runtime_request(request: dict) -> dict:
    errors = []
    if _missing_text(request.get("preview_runtime_request_id")):
        errors.append({"field": "preview_runtime_request_id", "reason": "malformed payload"})
    payload = request.get("request_payload", {})
    if _missing_text(payload.get("interaction_identity")):
        errors.append({"field": "interaction_identity", "reason": "malformed payload"})
    for field in ("interaction_payload",):
        if field not in payload:
            errors.append({"field": field, "reason": "malformed payload"})
    interaction_payload = payload.get("interaction_payload", {})
    for field in (
        "hidden_continuation_present",
        "orchestration_present",
        "hidden_routing_present",
        "hidden_execution_present",
        "hidden_mutable_state_present",
    ):
        if interaction_payload.get(field) is not False:
            errors.append({"field": field, "reason": "unauthorized continuation"})
    for field in ("governed_session_id", "runtime_activation_gate_id", "runtime_operation_envelope_id", "runtime_execution_surface_id"):
        if _missing_text(request.get("lineage", {}).get(field)):
            errors.append({"field": field, "reason": "invalid runtime lineage"})
    expected_replay = stable_hash({"request_payload": request.get("request_payload"), "lineage": request.get("lineage")})
    if request.get("replay_identity") != expected_replay:
        errors.append({"field": "replay_identity", "reason": "replay mismatch"})
    return {"valid": not errors, "errors": errors}


def validate_preview_runtime_response(*, response: dict, request: dict) -> dict:
    errors = []
    if response.get("preview_runtime_request_id") != request.get("preview_runtime_request_id"):
        errors.append({"field": "preview_runtime_request_id", "reason": "invalid response continuity"})
    if response.get("status") != "RETURNED":
        errors.append({"field": "status", "reason": "invalid response continuity"})
    if response.get("closure") != "PASS":
        errors.append({"field": "closure", "reason": "invalid lifecycle closure"})
    value = {
        "preview_runtime_request_id": response.get("preview_runtime_request_id"),
        "runtime_invocation_response_id": response.get("runtime_invocation_response_id"),
        "invocation_replay_identity": response.get("invocation_replay_identity"),
        "lineage": response.get("lineage"),
        "evidence": response.get("evidence"),
        "closure_id": response.get("closure_id"),
    }
    if response.get("response_sha256") != stable_hash(value):
        errors.append({"field": "response_sha256", "reason": "replay mismatch"})
    return {"valid": not errors, "errors": errors}
