"""Deterministic certification artifact for governed promotion."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def create_promotion_certification(*, pipeline: dict) -> dict:
    latest = pipeline["promotions"][-1]
    value = {
        "certified_promotion_pipeline_id": pipeline["certified_promotion_pipeline_id"],
        "governed_promotion_id": latest["governed_promotion_id"],
        "promotion_hash": latest["promotion_hash"],
        "certification_scope": pipeline["certification_scope"],
        "replay_identity": pipeline["replay_identity"],
    }
    certification_hash = stable_hash(value)
    return {
        **value,
        "governed_promotion_certification_id": f"GOVERNED-PROMOTION-CERTIFICATION-{certification_hash[:24]}",
        "certification_sha256": certification_hash,
        "deployment_authorized": False,
        "replay_safe": True,
    }
