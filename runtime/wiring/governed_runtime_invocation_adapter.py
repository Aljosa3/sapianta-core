"""Minimal deterministic adapter from interaction surface to governed runtime."""

from __future__ import annotations

from copy import deepcopy

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash
from sapianta_system.runtime.ux import perform_governed_interaction

from .governed_runtime_endpoint_validator import validate_invocation_append
from .governed_runtime_request_bridge import create_runtime_request_envelope
from .governed_runtime_response_bridge import create_runtime_response_envelope


def create_runtime_invocation_session(*, interaction_identity: str, lineage: dict) -> dict:
    value = {"interaction_identity": interaction_identity, "lineage": lineage}
    replay_identity = stable_hash(value)
    return {
        "runtime_invocation_session_id": f"RUNTIME-INVOCATION-SESSION-{replay_identity[:24]}",
        "interaction_identity": interaction_identity,
        "lineage": deepcopy(lineage),
        "replay_identity": replay_identity,
        "invocations": [],
        "invocation_count": 0,
        "invocation_head_hash": "",
        "closed": False,
        "closure_id": "",
        "bounded": True,
    }


def invoke_governed_runtime(
    *,
    invocation_session: dict,
    ux_session: dict,
    interaction_payload: dict,
    transport_lineage: dict,
    activation_output: dict,
    operation_output: dict,
    surface_output: dict,
) -> dict:
    validation = validate_invocation_append(session=invocation_session, interaction_payload=interaction_payload)
    if not validation["valid"]:
        return {
            "invocation_session": deepcopy(invocation_session),
            "validation": validation,
            "states": ["BLOCKED"],
            "invocation_status": "BLOCKED",
        }
    request_envelope = create_runtime_request_envelope(
        invocation_session=invocation_session,
        interaction_payload=interaction_payload,
    )
    ux_output = perform_governed_interaction(
        session=ux_session,
        interaction_payload=interaction_payload,
        transport_lineage=transport_lineage,
        activation_output=activation_output,
        operation_output=operation_output,
        surface_output=surface_output,
    )
    if ux_output["interaction_status"] != "RETURNED":
        return {
            "invocation_session": deepcopy(invocation_session),
            "request_envelope": request_envelope,
            "ux_output": ux_output,
            "validation": ux_output["validation"],
            "states": ["BLOCKED"],
            "invocation_status": "BLOCKED",
        }
    response_envelope = create_runtime_response_envelope(request_envelope=request_envelope, ux_output=ux_output)
    next_session = deepcopy(invocation_session)
    next_session["invocations"].append({"request": request_envelope, "response": response_envelope})
    next_session["invocation_count"] += 1
    next_session["invocation_head_hash"] = response_envelope["invocation_response_hash"]
    return {
        "invocation_session": next_session,
        "ux_session": ux_output["session"],
        "request_envelope": request_envelope,
        "response_envelope": response_envelope,
        "ux_output": ux_output,
        "validation": {"valid": True, "errors": []},
        "states": ["INVOCATION_RETURNED"],
        "invocation_status": "RETURNED",
    }
