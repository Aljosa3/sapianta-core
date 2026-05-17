"""Fail-closed governed execution connector validation."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

from .governed_connector_registry import CONNECTOR_REGISTRY

FORBIDDEN_BEHAVIOR_FIELDS = (
    "orchestration_present",
    "retry_present",
    "fallback_present",
    "provider_routing_present",
    "hidden_execution_present",
    "unrestricted_execution_present",
)


def _missing_text(value: object) -> bool:
    return not isinstance(value, str) or not value.strip()


def validate_connector_registration(registration: dict) -> dict:
    errors = []
    connector_name = registration.get("connector_name")
    spec = CONNECTOR_REGISTRY.get(connector_name)
    if spec is None:
        errors.append({"field": "connector_name", "reason": "unregistered connector"})
    if _missing_text(registration.get("connector_id")):
        errors.append({"field": "connector_id", "reason": "invalid connector identity"})
    if spec is not None:
        expected = stable_hash(
            {
                "connector_name": connector_name,
                "connector_type": spec["connector_type"],
                "allowed_execution_surfaces": list(spec["allowed_execution_surfaces"]),
            }
        )
        if registration.get("registration_sha256") != expected:
            errors.append({"field": "registration_sha256", "reason": "invalid connector identity"})
    for field in FORBIDDEN_BEHAVIOR_FIELDS:
        if registration.get(field) is not False:
            errors.append({"field": field, "reason": "connector registration contains prohibited behavior"})
    return {"valid": not errors, "errors": errors}


def validate_connector_envelope(*, envelope: dict, registration: dict, transport_output: dict) -> dict:
    errors = []
    if transport_output.get("transport_status") != "COMPLETED":
        errors.append({"field": "transport_status", "reason": "transport continuity break"})
    if envelope.get("connector_id") != registration.get("connector_id"):
        errors.append({"field": "connector_id", "reason": "malformed connector envelope"})
    if envelope.get("governed_transport_request_id") != transport_output.get("request", {}).get("governed_transport_request_id"):
        errors.append({"field": "governed_transport_request_id", "reason": "continuity break"})
    if envelope.get("replay_identity") != transport_output.get("request", {}).get("replay_identity"):
        errors.append({"field": "replay_identity", "reason": "replay mismatch"})
    allowed = set(registration.get("allowed_execution_surfaces", ()))
    if envelope.get("runtime_surface") not in allowed:
        errors.append({"field": "runtime_surface", "reason": "invalid execution surface"})
    if envelope.get("authorized_execution") is not True:
        errors.append({"field": "authorized_execution", "reason": "unauthorized execution attempt"})
    return {"valid": not errors, "errors": errors}


def validate_connector_result(*, result: dict, envelope: dict) -> dict:
    errors = []
    if result.get("connector_id") != envelope.get("connector_id"):
        errors.append({"field": "connector_id", "reason": "continuity break"})
    if result.get("connector_envelope_id") != envelope.get("connector_envelope_id"):
        errors.append({"field": "connector_envelope_id", "reason": "continuity break"})
    if result.get("replay_identity") != envelope.get("replay_identity"):
        errors.append({"field": "replay_identity", "reason": "replay mismatch"})
    if result.get("bounded_result") is not True:
        errors.append({"field": "connector_result_id", "reason": "invalid connector result"})
    return {"valid": not errors, "errors": errors}
