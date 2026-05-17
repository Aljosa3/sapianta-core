"""Fail-closed governed UX interaction validation."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

from .governed_interaction_session import ALLOWED_INTERACTION_SCOPE

REQUIRED_LINEAGE_FIELDS = (
    "governed_session_id",
    "runtime_activation_gate_id",
    "runtime_operation_envelope_id",
    "runtime_execution_surface_id",
)


def _missing_text(value: object) -> bool:
    return not isinstance(value, str) or not value.strip()


def validate_interaction_payload(payload: dict) -> dict:
    errors = []
    if not isinstance(payload, dict):
        return {"valid": False, "errors": [{"field": "interaction_payload", "reason": "malformed interaction payload"}]}
    for field in ("interaction_intent", "connector_name"):
        if _missing_text(payload.get(field)):
            errors.append({"field": field, "reason": "malformed interaction payload"})
    if not isinstance(payload.get("request_payload"), dict) or not payload.get("request_payload"):
        errors.append({"field": "request_payload", "reason": "malformed interaction payload"})
    forbidden_true_fields = (
        "hidden_continuation_present",
        "orchestration_present",
        "hidden_routing_present",
        "hidden_execution_present",
        "hidden_mutable_state_present",
    )
    for field in forbidden_true_fields:
        if payload.get(field) is not False:
            errors.append({"field": field, "reason": "unauthorized interaction continuation"})
    return {"valid": not errors, "errors": errors}


def validate_interaction_session(session: dict) -> dict:
    errors = []
    base = {
        "interaction_seed": session.get("interaction_seed"),
        "lineage": session.get("lineage"),
        "interaction_scope": session.get("interaction_scope"),
    }
    replay_identity = stable_hash(base)
    expected_id = f"GOVERNED-INTERACTION-SESSION-{replay_identity[:24]}"
    if session.get("governed_interaction_session_id") != expected_id:
        errors.append({"field": "governed_interaction_session_id", "reason": "invalid interaction lineage"})
    if session.get("replay_identity") != replay_identity:
        errors.append({"field": "replay_identity", "reason": "replay mismatch"})
    if session.get("interaction_scope") != ALLOWED_INTERACTION_SCOPE:
        errors.append({"field": "interaction_scope", "reason": "invalid interaction lineage"})
    for field in REQUIRED_LINEAGE_FIELDS:
        if _missing_text(session.get("lineage", {}).get(field)):
            errors.append({"field": field, "reason": "invalid interaction lineage"})
    interactions = session.get("interactions")
    if not isinstance(interactions, list):
        errors.append({"field": "interactions", "reason": "malformed interaction payload"})
        interactions = []
    previous_hash = ""
    for expected_index, interaction in enumerate(interactions, start=1):
        request = interaction.get("request", {})
        response = interaction.get("response", {})
        if request.get("interaction_index") != expected_index:
            errors.append({"field": "interaction_index", "reason": "invalid interaction continuity"})
        if request.get("previous_interaction_hash") != previous_hash:
            errors.append({"field": "previous_interaction_hash", "reason": "invalid interaction continuity"})
        errors.extend(validate_interaction_payload(request.get("interaction_payload", {}))["errors"])
        request_value = {
            "governed_interaction_session_id": request.get("governed_interaction_session_id"),
            "interaction_index": request.get("interaction_index"),
            "previous_interaction_hash": request.get("previous_interaction_hash"),
            "interaction_payload": request.get("interaction_payload"),
        }
        request_hash = stable_hash(request_value)
        if request.get("request_hash") != request_hash:
            errors.append({"field": "request_hash", "reason": "replay mismatch"})
        response_value = {
            "governed_interaction_request_id": response.get("governed_interaction_request_id"),
            "governed_transport_request_id": response.get("governed_transport_request_id"),
            "connector_result_id": response.get("connector_result_id"),
            "transport_replay_identity": response.get("transport_replay_identity"),
            "connector_replay_identity": response.get("connector_replay_identity"),
            "operational_evidence": response.get("operational_evidence"),
        }
        response_hash = stable_hash(response_value)
        if response.get("response_hash") != response_hash:
            errors.append({"field": "response_hash", "reason": "replay mismatch"})
        if response.get("governed_interaction_request_id") != request.get("governed_interaction_request_id"):
            errors.append({"field": "governed_interaction_request_id", "reason": "invalid response continuity"})
        if response.get("response_status") != "RETURNED":
            errors.append({"field": "response_status", "reason": "invalid response continuity"})
        previous_hash = response.get("response_hash", "")
    if session.get("interaction_count") != len(interactions):
        errors.append({"field": "interaction_count", "reason": "malformed interaction payload"})
    if session.get("interaction_head_hash") != previous_hash:
        errors.append({"field": "interaction_head_hash", "reason": "invalid interaction continuity"})
    return {"valid": not errors, "errors": errors}


def validate_interaction_append(*, session: dict, interaction_payload: dict) -> dict:
    errors = list(validate_interaction_session(session)["errors"])
    if session.get("closed") is True:
        errors.append({"field": "closed", "reason": "invalid interaction closure"})
    errors.extend(validate_interaction_payload(interaction_payload)["errors"])
    return {"valid": not errors, "errors": errors}
