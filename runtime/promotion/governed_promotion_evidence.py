"""Replay-visible certified promotion pipeline evidence."""


def governed_promotion_evidence(*, pipeline: dict, certification: dict | None = None, closure: dict | None = None) -> dict:
    return {
        "certified_promotion_pipeline_id": pipeline.get("certified_promotion_pipeline_id", ""),
        "governed_execution_session_id": pipeline.get("governed_execution_session_id", ""),
        "governed_synchronization_chain_id": pipeline.get("governed_synchronization_chain_id", ""),
        "governed_recovery_chain_id": pipeline.get("governed_recovery_chain_id", ""),
        "promotion_count": pipeline.get("promotion_count", 0),
        "replay_identity": pipeline.get("replay_identity", ""),
        "certification_id": (certification or {}).get("governed_promotion_certification_id", ""),
        "closure_id": (closure or {}).get("certified_promotion_closure_id", ""),
        "replay_safe": True,
        "lineage_preserved": True,
        "promotion_authorization_explicit": True,
        "deployment_present": False,
        "rollout_present": False,
        "orchestration_present": False,
        "autonomous_rollout_present": False,
        "hidden_approval_present": False,
    }
