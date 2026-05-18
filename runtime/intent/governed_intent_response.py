"""Bounded governed interpretation response construction."""

from __future__ import annotations

from .governed_artifact_synthesizer import synthesize_governed_artifact
from .governed_intent_classifier import classify_governed_intent
from .governed_intent_evidence import governed_intent_evidence
from .governed_intent_replay import build_intent_replay_identity
from .governed_intent_validator import validate_governed_intent_request, validate_governed_intent_response


def _blocked(request: dict, errors: list[dict]) -> dict:
    response = {
        "status": "BLOCKED",
        "intent_class": None,
        "governance_mode": None,
        "artifact_candidate": None,
        "requires_confirmation": True,
        "allowed_to_execute_automatically": False,
        "replay_visible": True,
        "closure": "BLOCKED",
        "validation": {"valid": False, "errors": errors},
    }
    response["replay_identity"] = build_intent_replay_identity(request=request, interpretation=response.copy())
    response["evidence"] = governed_intent_evidence(request=request, response=response)
    return response


def interpret_governed_intent(request: dict) -> dict:
    request_validation = validate_governed_intent_request(request)
    if not request_validation["valid"]:
        return _blocked(request, request_validation["errors"])
    classification = classify_governed_intent(request["natural_language"])
    if not classification["valid"]:
        return _blocked(request, [{"field": "natural_language", "reason": classification["reason"]}])
    synthesis = synthesize_governed_artifact(classification["intent_class"])
    if not synthesis["valid"]:
        return _blocked(request, [{"field": "artifact_candidate", "reason": "unsafe artifact"}])
    response = {
        "status": "INTERPRETED",
        "intent_class": classification["intent_class"],
        "governance_mode": synthesis["governance_mode"],
        "artifact_candidate": synthesis["artifact_candidate"],
        "requires_confirmation": True,
        "allowed_to_execute_automatically": False,
        "replay_visible": True,
        "closure": "PREVIEW",
    }
    response["replay_identity"] = build_intent_replay_identity(request=request, interpretation=response.copy())
    validation = validate_governed_intent_response(response)
    if not validation["valid"]:
        return _blocked(request, validation["errors"])
    response["validation"] = validation
    response["evidence"] = governed_intent_evidence(request=request, response=response)
    return response
