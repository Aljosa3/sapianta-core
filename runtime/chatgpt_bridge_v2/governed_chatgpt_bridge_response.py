"""Bounded conversational bridge responses."""

from .governed_chatgpt_bridge_boundary import bridge_boundary_state
from .governed_chatgpt_bridge_evidence import governed_chatgpt_bridge_evidence
from .governed_chatgpt_bridge_normalizer import normalize_conversational_request
from .governed_chatgpt_bridge_replay import build_chatgpt_bridge_replay_identity
from .governed_chatgpt_bridge_validator import validate_chatgpt_bridge_request


def _blocked(request: dict, errors: list[dict]) -> dict:
    boundary = bridge_boundary_state()
    normalization = {"valid": False, "errors": errors}
    response = {
        "status": "BLOCKED",
        "normalized_request": None,
        "governance_mode": None,
        "downstream_governance_request": None,
        "requires_confirmation": True,
        "allowed_to_execute_automatically": False,
        "replay_visible": True,
        "bridge_boundary_state": boundary,
        "closure": "BLOCKED",
        "validation": {"valid": False, "errors": errors},
    }
    response["replay_identity"] = build_chatgpt_bridge_replay_identity(
        request=request, normalization=normalization, boundary_state=boundary
    )
    response["evidence"] = governed_chatgpt_bridge_evidence(request=request, response=response)
    return response


def bridge_chatgpt_conversation(request: dict) -> dict:
    validation = validate_chatgpt_bridge_request(request)
    if not validation["valid"]:
        return _blocked(request, validation["errors"])
    normalization = normalize_conversational_request(request["conversational_input"])
    if not normalization["valid"]:
        return _blocked(request, [{"field": "conversational_input", "reason": normalization["reason"]}])
    boundary = bridge_boundary_state()
    response = {
        "status": "NORMALIZED",
        "normalized_request": {
            "request_type": normalization["normalized_request_type"],
            "text": normalization["normalized_conversational_request"],
        },
        "governance_mode": normalization["governance_mode"],
        "downstream_governance_request": normalization["downstream_governance_request"],
        "requires_confirmation": True,
        "allowed_to_execute_automatically": False,
        "replay_visible": True,
        "bridge_boundary_state": boundary,
        "closure": "PREVIEW",
        "validation": validation,
    }
    response["replay_identity"] = build_chatgpt_bridge_replay_identity(
        request=request, normalization=normalization, boundary_state=boundary
    )
    response["evidence"] = governed_chatgpt_bridge_evidence(request=request, response=response)
    return response
