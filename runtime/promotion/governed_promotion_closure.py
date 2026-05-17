"""Deterministic certified promotion pipeline closure."""

from __future__ import annotations

from copy import deepcopy

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

from .governed_promotion_replay import validate_promotion_replay


def close_certified_promotion_pipeline(*, pipeline: dict) -> dict:
    validation = validate_promotion_replay(pipeline)
    if not validation["valid"] or pipeline.get("closed") is True or pipeline.get("promotion_count", 0) == 0:
        errors = list(validation["errors"])
        if pipeline.get("closed") is True:
            errors.append({"field": "closed", "reason": "invalid promotion closure"})
        if pipeline.get("promotion_count", 0) == 0:
            errors.append({"field": "promotion_count", "reason": "invalid promotion closure"})
        return {"pipeline": deepcopy(pipeline), "validation": {"valid": False, "errors": errors}, "states": ["BLOCKED"]}
    value = {
        "certified_promotion_pipeline_id": pipeline["certified_promotion_pipeline_id"],
        "final_promotion_hash": pipeline["promotion_head_hash"],
        "promotion_count": pipeline["promotion_count"],
        "replay_identity": pipeline["replay_identity"],
    }
    closure_hash = stable_hash(value)
    closure = {
        **value,
        "certified_promotion_closure_id": f"CERTIFIED-PROMOTION-CLOSURE-{closure_hash[:24]}",
        "closure_sha256": closure_hash,
        "replay_safe": True,
    }
    closed_pipeline = deepcopy(pipeline)
    closed_pipeline["closed"] = True
    closed_pipeline["closure_id"] = closure["certified_promotion_closure_id"]
    return {
        "pipeline": closed_pipeline,
        "closure": closure,
        "validation": {"valid": True, "errors": []},
        "states": ["PROMOTION_CLOSED"],
    }
