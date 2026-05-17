"""Deterministic governed no-copy-paste UX flow."""

from __future__ import annotations

from copy import deepcopy

from sapianta_system.runtime.connectors import execute_governed_connector
from sapianta_system.runtime.transport import execute_governed_live_execution_transport

from .governed_interaction_request import create_governed_interaction_request
from .governed_interaction_response import create_governed_interaction_response
from .governed_interaction_validator import validate_interaction_append


def perform_governed_interaction(
    *,
    session: dict,
    interaction_payload: dict,
    transport_lineage: dict,
    activation_output: dict,
    operation_output: dict,
    surface_output: dict,
) -> dict:
    validation = validate_interaction_append(session=session, interaction_payload=interaction_payload)
    if not validation["valid"]:
        return {"session": deepcopy(session), "validation": validation, "states": ["BLOCKED"], "interaction_status": "BLOCKED"}
    request = create_governed_interaction_request(session=session, interaction_payload=interaction_payload)
    transport_output = execute_governed_live_execution_transport(
        request_payload=interaction_payload["request_payload"],
        lineage=transport_lineage,
        activation_output=activation_output,
        operation_output=operation_output,
        surface_output=surface_output,
    )
    if transport_output["transport_status"] != "COMPLETED":
        return {
            "session": deepcopy(session),
            "request": request,
            "transport": transport_output,
            "validation": transport_output["validation"],
            "states": ["BLOCKED"],
            "interaction_status": "BLOCKED",
        }
    connector_output = execute_governed_connector(
        connector_name=interaction_payload["connector_name"],
        transport_output=transport_output,
        authorized_execution=True,
    )
    if connector_output["connector_status"] != "COMPLETED":
        return {
            "session": deepcopy(session),
            "request": request,
            "transport": transport_output,
            "connector": connector_output,
            "validation": connector_output["validation"],
            "states": ["BLOCKED"],
            "interaction_status": "BLOCKED",
        }
    response = create_governed_interaction_response(
        request=request,
        transport_output=transport_output,
        connector_output=connector_output,
    )
    next_session = deepcopy(session)
    next_session["interactions"].append({"request": request, "response": response})
    next_session["interaction_count"] += 1
    next_session["interaction_head_hash"] = response["response_hash"]
    return {
        "session": next_session,
        "request": request,
        "transport": transport_output,
        "connector": connector_output,
        "response": response,
        "validation": {"valid": True, "errors": []},
        "states": ["INTERACTION_RETURNED"],
        "interaction_status": "RETURNED",
    }
