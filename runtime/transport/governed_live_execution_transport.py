"""Synchronous deterministic governed live execution transport."""

from __future__ import annotations

from .governed_transport_envelope import create_governed_transport_envelope
from .governed_transport_evidence import governed_transport_evidence
from .governed_transport_request import create_governed_transport_request
from .governed_transport_response import create_governed_transport_response
from .governed_transport_validator import (
    validate_governed_transport_envelope,
    validate_governed_transport_request,
    validate_governed_transport_response,
)


def execute_governed_live_execution_transport(
    *,
    request_payload: dict,
    lineage: dict,
    activation_output: dict,
    operation_output: dict,
    surface_output: dict,
) -> dict:
    request = create_governed_transport_request(request_payload=request_payload, lineage=lineage)
    request_validation = validate_governed_transport_request(request)
    if not request_validation["valid"]:
        return {
            "request": request,
            "validation": request_validation,
            "states": ["BLOCKED"],
            "transport_status": "BLOCKED",
        }

    try:
        envelope = create_governed_transport_envelope(
            request=request,
            activation_binding=activation_output["runtime_activation_gate_binding"],
            operation_evidence=operation_output["runtime_operation_evidence"],
            surface_evidence=surface_output["runtime_execution_surface_evidence"],
        )
    except KeyError:
        return {
            "request": request,
            "validation": {"valid": False, "errors": [{"field": "transport_envelope", "reason": "malformed transport envelope"}]},
            "states": ["BLOCKED"],
            "transport_status": "BLOCKED",
        }
    envelope_validation = validate_governed_transport_envelope(
        envelope=envelope,
        request=request,
        activation_output=activation_output,
        operation_output=operation_output,
        surface_output=surface_output,
    )
    if not envelope_validation["valid"]:
        return {
            "request": request,
            "envelope": envelope,
            "validation": envelope_validation,
            "states": ["BLOCKED"],
            "transport_status": "BLOCKED",
        }

    response = create_governed_transport_response(
        request=request,
        envelope=envelope,
        surface_evidence=surface_output["runtime_execution_surface_evidence"],
    )
    response_validation = validate_governed_transport_response(response=response, request=request, envelope=envelope)
    valid = response_validation["valid"]
    evidence = governed_transport_evidence(request=request, envelope=envelope, response=response, valid=valid)
    return {
        "request": request,
        "envelope": envelope,
        "response": response,
        "evidence": evidence,
        "validation": response_validation,
        "states": ["TRANSPORT_COMPLETED"] if valid else ["BLOCKED"],
        "transport_status": "COMPLETED" if valid else "BLOCKED",
    }
