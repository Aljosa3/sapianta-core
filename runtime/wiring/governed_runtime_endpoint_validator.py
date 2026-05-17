"""Fail-closed validation for live runtime wiring."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

from .governed_runtime_request_bridge import GOVERNED_RUNTIME_ENDPOINT_ID


def _missing_text(value: object) -> bool:
    return not isinstance(value, str) or not value.strip()


def validate_invocation_payload(payload: dict) -> dict:
    errors = []
    if not isinstance(payload, dict):
        return {"valid": False, "errors": [{"field": "interaction_payload", "reason": "malformed invocation payload"}]}
    for field in ("interaction_intent", "connector_name"):
        if _missing_text(payload.get(field)):
            errors.append({"field": field, "reason": "malformed invocation payload"})
    if not isinstance(payload.get("request_payload"), dict) or not payload.get("request_payload"):
        errors.append({"field": "request_payload", "reason": "malformed invocation payload"})
    for field in (
        "hidden_continuation_present",
        "orchestration_present",
        "hidden_routing_present",
        "hidden_execution_present",
        "hidden_mutable_state_present",
    ):
        if payload.get(field) is not False:
            errors.append({"field": field, "reason": "unauthorized invocation continuation"})
    return {"valid": not errors, "errors": errors}


def validate_invocation_session(session: dict) -> dict:
    errors = []
    base = {
        "interaction_identity": session.get("interaction_identity"),
        "lineage": session.get("lineage"),
    }
    replay_identity = stable_hash(base)
    expected_id = f"RUNTIME-INVOCATION-SESSION-{replay_identity[:24]}"
    if session.get("runtime_invocation_session_id") != expected_id:
        errors.append({"field": "runtime_invocation_session_id", "reason": "invalid invocation lineage"})
    if session.get("replay_identity") != replay_identity:
        errors.append({"field": "replay_identity", "reason": "replay mismatch"})
    for field in ("governed_interaction_session_id", "governed_session_id"):
        if _missing_text(session.get("lineage", {}).get(field)):
            errors.append({"field": field, "reason": "invalid invocation lineage"})
    invocations = session.get("invocations")
    if not isinstance(invocations, list):
        errors.append({"field": "invocations", "reason": "malformed invocation payload"})
        invocations = []
    previous_hash = ""
    for expected_index, invocation in enumerate(invocations, start=1):
        request = invocation.get("request", {})
        response = invocation.get("response", {})
        if request.get("invocation_index") != expected_index:
            errors.append({"field": "invocation_index", "reason": "invalid invocation continuity"})
        if request.get("previous_invocation_hash") != previous_hash:
            errors.append({"field": "previous_invocation_hash", "reason": "invalid invocation continuity"})
        if request.get("governed_runtime_endpoint_id") != GOVERNED_RUNTIME_ENDPOINT_ID:
            errors.append({"field": "governed_runtime_endpoint_id", "reason": "invalid invocation lineage"})
        errors.extend(validate_invocation_payload(request.get("interaction_payload", {}))["errors"])
        request_value = {
            "runtime_invocation_session_id": request.get("runtime_invocation_session_id"),
            "invocation_index": request.get("invocation_index"),
            "previous_invocation_hash": request.get("previous_invocation_hash"),
            "governed_runtime_endpoint_id": request.get("governed_runtime_endpoint_id"),
            "interaction_payload": request.get("interaction_payload"),
        }
        if request.get("request_hash") != stable_hash(request_value):
            errors.append({"field": "request_hash", "reason": "replay mismatch"})
        response_value = {
            "runtime_invocation_request_id": response.get("runtime_invocation_request_id"),
            "governed_interaction_request_id": response.get("governed_interaction_request_id"),
            "governed_interaction_response_id": response.get("governed_interaction_response_id"),
            "response_hash": response.get("response_hash"),
            "operational_evidence": response.get("operational_evidence"),
        }
        if response.get("invocation_response_hash") != stable_hash(response_value):
            errors.append({"field": "invocation_response_hash", "reason": "replay mismatch"})
        if response.get("runtime_invocation_request_id") != request.get("runtime_invocation_request_id"):
            errors.append({"field": "runtime_invocation_request_id", "reason": "invalid response continuity"})
        if response.get("response_status") != "RETURNED":
            errors.append({"field": "response_status", "reason": "invalid response continuity"})
        previous_hash = response.get("invocation_response_hash", "")
    if session.get("invocation_count") != len(invocations):
        errors.append({"field": "invocation_count", "reason": "malformed invocation payload"})
    if session.get("invocation_head_hash") != previous_hash:
        errors.append({"field": "invocation_head_hash", "reason": "invalid invocation continuity"})
    return {"valid": not errors, "errors": errors}


def validate_invocation_append(*, session: dict, interaction_payload: dict) -> dict:
    errors = list(validate_invocation_session(session)["errors"])
    if session.get("closed") is True:
        errors.append({"field": "closed", "reason": "invalid invocation closure"})
    errors.extend(validate_invocation_payload(interaction_payload)["errors"])
    return {"valid": not errors, "errors": errors}
