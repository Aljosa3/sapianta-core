"""Replay-visible governed operational recovery evidence."""


def governed_recovery_evidence(*, chain: dict, closure: dict | None = None) -> dict:
    return {
        "governed_recovery_chain_id": chain.get("governed_recovery_chain_id", ""),
        "governed_execution_session_id": chain.get("governed_execution_session_id", ""),
        "governed_synchronization_chain_id": chain.get("governed_synchronization_chain_id", ""),
        "recovery_count": chain.get("recovery_count", 0),
        "replay_identity": chain.get("replay_identity", ""),
        "closure_id": (closure or {}).get("governed_recovery_closure_id", ""),
        "replay_safe": True,
        "lineage_preserved": True,
        "recovery_authorization_explicit": True,
        "retry_present": False,
        "fallback_present": False,
        "orchestration_present": False,
        "autonomous_continuation_present": False,
        "hidden_continuation_present": False,
    }
