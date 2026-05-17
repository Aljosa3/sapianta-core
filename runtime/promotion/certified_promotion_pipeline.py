"""Deterministic certified promotion pipeline controller."""

from __future__ import annotations

from copy import deepcopy

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

from .governed_promotion_authorization import ALLOWED_CERTIFICATION_SCOPE
from .governed_promotion_state import create_promotion_state
from .governed_promotion_validator import validate_promotion_append


def create_certified_promotion_pipeline(
    *,
    session: dict,
    synchronization_chain: dict,
    recovery_chain: dict,
    lineage: dict,
) -> dict:
    value = {
        "governed_execution_session_id": session["governed_execution_session_id"],
        "governed_synchronization_chain_id": synchronization_chain["governed_synchronization_chain_id"],
        "governed_recovery_chain_id": recovery_chain["governed_recovery_chain_id"],
        "lineage": lineage,
        "certification_scope": ALLOWED_CERTIFICATION_SCOPE,
    }
    replay_identity = stable_hash(value)
    return {
        "certified_promotion_pipeline_id": f"CERTIFIED-PROMOTION-PIPELINE-{replay_identity[:24]}",
        "governed_execution_session_id": session["governed_execution_session_id"],
        "governed_synchronization_chain_id": synchronization_chain["governed_synchronization_chain_id"],
        "governed_recovery_chain_id": recovery_chain["governed_recovery_chain_id"],
        "lineage": deepcopy(lineage),
        "certification_scope": ALLOWED_CERTIFICATION_SCOPE,
        "replay_identity": replay_identity,
        "promotions": [],
        "promotion_count": 0,
        "promotion_head_hash": "",
        "closed": False,
        "closure_id": "",
        "bounded": True,
    }


def certify_governed_promotion(
    *,
    pipeline: dict,
    session: dict,
    synchronization_chain: dict,
    recovery_chain: dict,
    promotion_payload: dict,
    authorization: dict,
) -> dict:
    validation = validate_promotion_append(
        pipeline=pipeline,
        session=session,
        synchronization_chain=synchronization_chain,
        recovery_chain=recovery_chain,
        promotion_payload=promotion_payload,
        authorization=authorization,
    )
    if not validation["valid"]:
        return {"pipeline": deepcopy(pipeline), "validation": validation, "states": ["BLOCKED"]}
    promotion = create_promotion_state(
        pipeline=pipeline,
        session=session,
        synchronization_chain=synchronization_chain,
        recovery_chain=recovery_chain,
        promotion_payload=promotion_payload,
        authorization=authorization,
    )
    next_pipeline = deepcopy(pipeline)
    next_pipeline["promotions"].append(promotion)
    next_pipeline["promotion_count"] += 1
    next_pipeline["promotion_head_hash"] = promotion["promotion_hash"]
    return {
        "pipeline": next_pipeline,
        "promotion": promotion,
        "validation": {"valid": True, "errors": []},
        "states": ["PROMOTION_CERTIFIED"],
    }
