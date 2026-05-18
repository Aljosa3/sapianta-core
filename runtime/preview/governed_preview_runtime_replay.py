"""Replay validation for localhost preview runtime artifacts."""

from __future__ import annotations

from copy import deepcopy

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

from .governed_preview_runtime_validator import validate_preview_runtime_response


def validate_preview_response_replay(*, response: dict, request: dict) -> dict:
    before = stable_hash(response)
    snapshot = deepcopy(response)
    validation = validate_preview_runtime_response(response=response, request=request)
    after = stable_hash(response)
    mutated = snapshot != response or before != after
    errors = list(validation["errors"])
    if mutated:
        errors.append({"field": "response", "reason": "hidden runtime mutation"})
    return {"valid": not errors, "errors": errors, "read_only": not mutated}
