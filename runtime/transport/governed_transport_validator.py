"""Fail-closed governed live execution transport validation."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

LINEAGE_FIELDS = (
    "runtime_activation_gate_id",
    "runtime_operation_envelope_id",
    "runtime_execution_surface_id",
    "execution_exchange_session_id",
    "execution_relay_session_id",
    "runtime_execution_commit_id",
    "response_return_id",
)


def _missing_text(value: object) -> bool:
    return not isinstance(value, str) or not value.strip()


def validate_governed_transport_request(request: dict) -> dict:
    errors = []
    payload = request.get("request_payload", {})
    if _missing_text(request.get("governed_transport_request_id")):
        errors.append({"field": "governed_transport_request_id", "reason": "invalid request"})
    if _missing_text(payload.get("operation_intent")):
        errors.append({"field": "operation_intent", "reason": "invalid request"})
    if payload.get("authorized_execution") is not True:
        errors.append({"field": "authorized_execution", "reason": "unauthorized execution attempt"})
    for field in LINEAGE_FIELDS:
        if _missing_text(request.get("lineage", {}).get(field)):
            errors.append({"field": field, "reason": "invalid lineage binding"})
    expected = stable_hash({"request_payload": request.get("request_payload"), "lineage": request.get("lineage")})
    if request.get("replay_identity") != expected:
        errors.append({"field": "replay_identity", "reason": "replay mismatch"})
    return {"valid": not errors, "errors": errors}


def validate_governed_transport_envelope(
    *,
    envelope: dict,
    request: dict,
    activation_output: dict,
    operation_output: dict,
    surface_output: dict,
) -> dict:
    errors = []
    if activation_output.get("validation", {}).get("valid") is not True:
        errors.append({"field": "activation_gate", "reason": "missing activation approval"})
    if activation_output.get("runtime_activation_gate_binding", {}).get("activation_authorized") is not True:
        errors.append({"field": "activation_gate", "reason": "missing activation approval"})
    if operation_output.get("validation", {}).get("valid") is not True:
        errors.append({"field": "operation_envelope", "reason": "malformed transport envelope"})
    if surface_output.get("validation", {}).get("valid") is not True:
        errors.append({"field": "execution_surface", "reason": "invalid execution surface"})
    expected = stable_hash(
        {
            "governed_transport_request_id": request.get("governed_transport_request_id"),
            "runtime_activation_gate_id": activation_output.get("runtime_activation_gate_binding", {}).get("runtime_activation_gate_id"),
            "runtime_operation_envelope_id": operation_output.get("runtime_operation_evidence", {}).get("runtime_operation_envelope_id"),
            "runtime_execution_surface_id": surface_output.get("runtime_execution_surface_evidence", {}).get("runtime_execution_surface_id"),
            "replay_identity": request.get("replay_identity"),
        }
    )
    if envelope.get("envelope_sha256") != expected:
        errors.append({"field": "governed_transport_envelope_id", "reason": "malformed transport envelope"})
    return {"valid": not errors, "errors": errors}


def validate_governed_transport_response(*, response: dict, request: dict, envelope: dict) -> dict:
    errors = []
    if response.get("governed_transport_request_id") != request.get("governed_transport_request_id"):
        errors.append({"field": "governed_transport_request_id", "reason": "transport continuity break"})
    if response.get("governed_transport_envelope_id") != envelope.get("governed_transport_envelope_id"):
        errors.append({"field": "governed_transport_envelope_id", "reason": "transport continuity break"})
    if response.get("request_replay_identity") != request.get("replay_identity"):
        errors.append({"field": "request_replay_identity", "reason": "replay mismatch"})
    if response.get("result_payload", {}).get("bounded_result") is not True or response.get("response_returned") is not True:
        errors.append({"field": "governed_transport_result_id", "reason": "invalid result return"})
    return {"valid": not errors, "errors": errors}
