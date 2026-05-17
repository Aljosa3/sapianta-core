"""Replay-visible governed synchronization evidence."""


def synchronization_evidence(*, chain: dict, valid: bool) -> dict:
    return {
        "governed_synchronization_chain_id": chain.get("governed_synchronization_chain_id", ""),
        "synchronization_count": chain.get("synchronization_count", 0),
        "synchronization_head_hash": chain.get("synchronization_head_hash", ""),
        "synchronization_scope": chain.get("synchronization_scope", ""),
        "closed": chain.get("closed", False),
        "continuity_valid": valid,
        "hidden_memory_present": False,
        "hidden_mutable_state_present": False,
        "autonomous_continuation_present": False,
        "replay_safe": valid,
    }
