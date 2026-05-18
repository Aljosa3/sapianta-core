"""Fail-closed validation for governed interpretation requests and responses."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

from .governed_artifact_synthesizer import ARTIFACT_PATTERN


def validate_governed_intent_request(request: dict) -> dict:
    errors = []
    if not isinstance(request, dict):
        return {"valid": False, "errors": [{"field": "request", "reason": "malformed request"}]}
    value = request.get("natural_language")
    if not isinstance(value, str) or not value.strip():
        errors.append({"field": "natural_language", "reason": "must be non-empty"})
    if isinstance(value, str) and len(value) > 240:
        errors.append({"field": "natural_language", "reason": "must remain bounded"})
    expected_replay = stable_hash({"natural_language": request.get("natural_language")})
    if request.get("replay_identity") != expected_replay:
        errors.append({"field": "replay_identity", "reason": "replay mismatch"})
    return {"valid": not errors, "errors": errors}


def validate_governed_intent_response(response: dict) -> dict:
    errors = []
    if response.get("status") != "INTERPRETED":
        errors.append({"field": "status", "reason": "interpretation not admitted"})
    if response.get("requires_confirmation") is not True:
        errors.append({"field": "requires_confirmation", "reason": "confirmation required"})
    if response.get("allowed_to_execute_automatically") is not False:
        errors.append({"field": "allowed_to_execute_automatically", "reason": "automatic execution forbidden"})
    artifact = response.get("artifact_candidate")
    if not isinstance(artifact, str) or not ARTIFACT_PATTERN.fullmatch(artifact):
        errors.append({"field": "artifact_candidate", "reason": "unsafe artifact"})
    if response.get("replay_visible") is not True:
        errors.append({"field": "replay_visible", "reason": "replay evidence required"})
    return {"valid": not errors, "errors": errors}
