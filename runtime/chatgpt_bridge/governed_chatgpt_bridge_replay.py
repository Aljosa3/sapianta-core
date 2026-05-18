"""Replay validation for governed ChatGPT bridge requests."""

from __future__ import annotations

from copy import deepcopy

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

from .governed_chatgpt_bridge_validator import validate_chatgpt_bridge_request


def validate_chatgpt_bridge_replay(request: dict) -> dict:
    before = stable_hash(request)
    snapshot = deepcopy(request)
    validation = validate_chatgpt_bridge_request(request)
    after = stable_hash(request)
    mutated = snapshot != request or before != after
    errors = list(validation["errors"])
    if mutated:
        errors.append({"field": "request", "reason": "hidden bridge mutation"})
    return {"valid": not errors, "errors": errors, "read_only": not mutated}
