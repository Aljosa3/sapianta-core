"""Deterministic governed synchronization state records."""

from __future__ import annotations

from copy import deepcopy

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def create_synchronization_state(
    *,
    chain: dict,
    session: dict,
    synchronized_payload: dict,
) -> dict:
    index = chain["synchronization_count"] + 1
    exchange = session["exchanges"][-1]
    value = {
        "governed_synchronization_chain_id": chain["governed_synchronization_chain_id"],
        "synchronization_index": index,
        "previous_synchronization_hash": chain["synchronization_head_hash"],
        "session_head_hash": session["session_head_hash"],
        "exchange_index": exchange["exchange_index"],
        "synchronized_payload": deepcopy(synchronized_payload),
    }
    sync_hash = stable_hash(value)
    return {
        **value,
        "governed_synchronization_id": f"GOVERNED-SYNCHRONIZATION-{sync_hash[:24]}",
        "synchronization_hash": sync_hash,
    }
