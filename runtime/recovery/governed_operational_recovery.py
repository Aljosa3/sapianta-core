"""Deterministic governed operational recovery controller."""

from __future__ import annotations

from copy import deepcopy

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

from .governed_recovery_authorization import ALLOWED_RECOVERY_SCOPE
from .governed_recovery_state import create_recovery_state
from .governed_recovery_validator import validate_recovery_append


def create_recovery_chain(*, session: dict, synchronization_chain: dict, lineage: dict) -> dict:
    value = {
        "governed_execution_session_id": session["governed_execution_session_id"],
        "governed_synchronization_chain_id": synchronization_chain["governed_synchronization_chain_id"],
        "lineage": lineage,
        "recovery_scope": ALLOWED_RECOVERY_SCOPE,
    }
    replay_identity = stable_hash(value)
    return {
        "governed_recovery_chain_id": f"GOVERNED-RECOVERY-CHAIN-{replay_identity[:24]}",
        "governed_execution_session_id": session["governed_execution_session_id"],
        "governed_synchronization_chain_id": synchronization_chain["governed_synchronization_chain_id"],
        "lineage": deepcopy(lineage),
        "recovery_scope": ALLOWED_RECOVERY_SCOPE,
        "replay_identity": replay_identity,
        "recoveries": [],
        "recovery_count": 0,
        "recovery_head_hash": "",
        "closed": False,
        "closure_id": "",
        "bounded": True,
    }


def recover_governed_operation(
    *,
    chain: dict,
    session: dict,
    synchronization_chain: dict,
    recovery_payload: dict,
    authorization: dict,
) -> dict:
    validation = validate_recovery_append(
        chain=chain,
        session=session,
        synchronization_chain=synchronization_chain,
        recovery_payload=recovery_payload,
        authorization=authorization,
    )
    if not validation["valid"]:
        return {"chain": deepcopy(chain), "validation": validation, "states": ["BLOCKED"]}
    state = create_recovery_state(
        chain=chain,
        interrupted_exchange=session["exchanges"][-1],
        interrupted_synchronization=synchronization_chain["synchronizations"][-1],
        recovery_payload=recovery_payload,
        authorization=authorization,
    )
    next_chain = deepcopy(chain)
    next_chain["recoveries"].append(state)
    next_chain["recovery_count"] += 1
    next_chain["recovery_head_hash"] = state["recovery_hash"]
    return {
        "chain": next_chain,
        "recovery": state,
        "validation": {"valid": True, "errors": []},
        "states": ["RECOVERY_AUTHORIZED"],
    }
