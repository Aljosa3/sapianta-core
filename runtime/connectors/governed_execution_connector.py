"""Deterministic governed execution connector handoff."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

from .governed_connector_evidence import governed_connector_evidence
from .governed_connector_registry import CONNECTOR_REGISTRY
from .governed_connector_validator import (
    validate_connector_envelope,
    validate_connector_registration,
    validate_connector_result,
)


def register_governed_connector(*, connector_name: str) -> dict:
    spec = CONNECTOR_REGISTRY.get(connector_name)
    if spec is None:
        return {
            "connector_name": connector_name,
            "connector_id": "",
            "allowed_execution_surfaces": (),
            "registration_sha256": "",
            "orchestration_present": False,
            "retry_present": False,
            "fallback_present": False,
            "provider_routing_present": False,
            "hidden_execution_present": False,
            "unrestricted_execution_present": False,
        }
    value = {
        "connector_name": connector_name,
        "connector_type": spec["connector_type"],
        "allowed_execution_surfaces": list(spec["allowed_execution_surfaces"]),
    }
    return {
        **value,
        "connector_id": f"GOVERNED-CONNECTOR-{stable_hash(value)[:24]}",
        "registration_sha256": stable_hash(value),
        "execution_scope": "BOUNDED",
        "deterministic": True,
        "fail_closed": True,
        "orchestration_present": False,
        "retry_present": False,
        "fallback_present": False,
        "provider_routing_present": False,
        "hidden_execution_present": False,
        "unrestricted_execution_present": False,
    }


def create_connector_envelope(*, registration: dict, transport_output: dict, authorized_execution: bool = True) -> dict:
    transport_request = transport_output["request"]
    runtime_surface = transport_output["response"]["result_payload"]["runtime_surface"]
    value = {
        "connector_id": registration["connector_id"],
        "governed_transport_request_id": transport_request["governed_transport_request_id"],
        "runtime_surface": runtime_surface,
        "replay_identity": transport_request["replay_identity"],
        "authorized_execution": authorized_execution,
    }
    return {
        **value,
        "connector_envelope_id": f"GOVERNED-CONNECTOR-ENVELOPE-{stable_hash(value)[:24]}",
        "envelope_sha256": stable_hash(value),
    }


def create_connector_result(*, registration: dict, envelope: dict) -> dict:
    value = {
        "connector_id": registration["connector_id"],
        "connector_envelope_id": envelope["connector_envelope_id"],
        "replay_identity": envelope["replay_identity"],
        "runtime_surface": envelope["runtime_surface"],
        "bounded_result": True,
    }
    return {
        **value,
        "connector_result_id": f"GOVERNED-CONNECTOR-RESULT-{stable_hash(value)[:24]}",
        "result_status": "RETURNED",
    }


def execute_governed_connector(
    *,
    connector_name: str,
    transport_output: dict,
    authorized_execution: bool = True,
) -> dict:
    registration = register_governed_connector(connector_name=connector_name)
    registration_validation = validate_connector_registration(registration)
    if not registration_validation["valid"]:
        return {
            "registration": registration,
            "validation": registration_validation,
            "connector_status": "BLOCKED",
            "states": ["BLOCKED"],
        }
    try:
        envelope = create_connector_envelope(
            registration=registration,
            transport_output=transport_output,
            authorized_execution=authorized_execution,
        )
    except KeyError:
        return {
            "registration": registration,
            "validation": {"valid": False, "errors": [{"field": "connector_envelope", "reason": "malformed connector envelope"}]},
            "connector_status": "BLOCKED",
            "states": ["BLOCKED"],
        }
    envelope_validation = validate_connector_envelope(
        envelope=envelope,
        registration=registration,
        transport_output=transport_output,
    )
    if not envelope_validation["valid"]:
        return {
            "registration": registration,
            "envelope": envelope,
            "validation": envelope_validation,
            "connector_status": "BLOCKED",
            "states": ["BLOCKED"],
        }
    result = create_connector_result(registration=registration, envelope=envelope)
    result_validation = validate_connector_result(result=result, envelope=envelope)
    valid = result_validation["valid"]
    evidence = governed_connector_evidence(
        registration=registration,
        envelope=envelope,
        result=result,
        valid=valid,
    )
    return {
        "registration": registration,
        "envelope": envelope,
        "result": result,
        "evidence": evidence,
        "validation": result_validation,
        "connector_status": "COMPLETED" if valid else "BLOCKED",
        "states": ["CONNECTOR_COMPLETED"] if valid else ["BLOCKED"],
    }
