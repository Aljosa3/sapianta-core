"""Deterministic certified promotion pipeline records."""

from __future__ import annotations

from copy import deepcopy

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def create_promotion_state(
    *,
    pipeline: dict,
    session: dict,
    synchronization_chain: dict,
    recovery_chain: dict,
    promotion_payload: dict,
    authorization: dict,
) -> dict:
    index = pipeline["promotion_count"] + 1
    latest_recovery = recovery_chain["recoveries"][-1]
    value = {
        "certified_promotion_pipeline_id": pipeline["certified_promotion_pipeline_id"],
        "promotion_index": index,
        "previous_promotion_hash": pipeline["promotion_head_hash"],
        "promoted_runtime_state_id": session["session_head_hash"],
        "synchronization_lineage_id": synchronization_chain["synchronization_head_hash"],
        "recovery_lineage_id": latest_recovery["recovery_hash"],
        "promotion_authorization_id": authorization["promotion_authorization_id"],
        "promotion_payload": deepcopy(promotion_payload),
    }
    promotion_hash = stable_hash(value)
    return {
        **value,
        "governed_promotion_id": f"GOVERNED-PROMOTION-{promotion_hash[:24]}",
        "promotion_hash": promotion_hash,
    }
