"""Replay validation for governed UX interaction sessions."""

from __future__ import annotations

from copy import deepcopy

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

from .governed_interaction_validator import validate_interaction_session


def validate_interaction_replay(session: dict) -> dict:
    before = stable_hash(session)
    snapshot = deepcopy(session)
    validation = validate_interaction_session(session)
    after = stable_hash(session)
    mutated = snapshot != session or before != after
    errors = list(validation["errors"])
    if mutated:
        errors.append({"field": "session", "reason": "hidden session mutation"})
    return {"valid": not errors, "errors": errors, "read_only": not mutated}
