"""Replay validation for certified promotion pipelines."""

from __future__ import annotations

from copy import deepcopy

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

from .governed_promotion_validator import validate_promotion_pipeline


def validate_promotion_replay(pipeline: dict) -> dict:
    before = stable_hash(pipeline)
    snapshot = deepcopy(pipeline)
    validation = validate_promotion_pipeline(pipeline)
    after = stable_hash(pipeline)
    mutated = snapshot != pipeline or before != after
    errors = list(validation["errors"])
    if mutated:
        errors.append({"field": "pipeline", "reason": "hidden approval attempts"})
    return {"valid": not errors, "errors": errors, "read_only": not mutated}
