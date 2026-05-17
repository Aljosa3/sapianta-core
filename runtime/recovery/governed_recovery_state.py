"""Deterministic governed operational recovery records."""

from __future__ import annotations

from copy import deepcopy

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def create_recovery_state(
    *,
    chain: dict,
    interrupted_exchange: dict,
    interrupted_synchronization: dict,
    recovery_payload: dict,
    authorization: dict,
) -> dict:
    index = chain["recovery_count"] + 1
    value = {
        "governed_recovery_chain_id": chain["governed_recovery_chain_id"],
        "recovery_index": index,
        "previous_recovery_hash": chain["recovery_head_hash"],
        "interrupted_exchange_id": interrupted_exchange["governed_session_exchange_id"],
        "interrupted_exchange_hash": interrupted_exchange["exchange_hash"],
        "interrupted_synchronization_id": interrupted_synchronization["governed_synchronization_id"],
        "interrupted_synchronization_hash": interrupted_synchronization["synchronization_hash"],
        "recovery_authorization_id": authorization["recovery_authorization_id"],
        "recovery_payload": deepcopy(recovery_payload),
    }
    recovery_hash = stable_hash(value)
    return {
        **value,
        "governed_recovery_id": f"GOVERNED-RECOVERY-{recovery_hash[:24]}",
        "recovery_hash": recovery_hash,
    }
