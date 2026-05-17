"""Deterministic governed state synchronization controller."""

from __future__ import annotations

from copy import deepcopy

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

from .governed_synchronization_boundary import ALLOWED_SYNCHRONIZATION_SCOPE
from .governed_synchronization_state import create_synchronization_state
from .governed_synchronization_validator import validate_synchronization_append


def create_synchronization_chain(*, session: dict, lineage: dict) -> dict:
    value = {
        "governed_execution_session_id": session["governed_execution_session_id"],
        "lineage": lineage,
        "synchronization_scope": ALLOWED_SYNCHRONIZATION_SCOPE,
    }
    replay_identity = stable_hash(value)
    return {
        "governed_synchronization_chain_id": f"GOVERNED-SYNCHRONIZATION-CHAIN-{replay_identity[:24]}",
        "governed_execution_session_id": session["governed_execution_session_id"],
        "lineage": deepcopy(lineage),
        "synchronization_scope": ALLOWED_SYNCHRONIZATION_SCOPE,
        "replay_identity": replay_identity,
        "synchronizations": [],
        "synchronization_count": 0,
        "synchronization_head_hash": "",
        "closed": False,
        "closure_id": "",
        "bounded": True,
    }


def synchronize_governed_state(*, chain: dict, session: dict, synchronized_payload: dict) -> dict:
    validation = validate_synchronization_append(chain=chain, session=session, synchronized_payload=synchronized_payload)
    if not validation["valid"]:
        return {"chain": deepcopy(chain), "validation": validation, "states": ["BLOCKED"]}
    state = create_synchronization_state(chain=chain, session=session, synchronized_payload=synchronized_payload)
    next_chain = deepcopy(chain)
    next_chain["synchronizations"].append(state)
    next_chain["synchronization_count"] += 1
    next_chain["synchronization_head_hash"] = state["synchronization_hash"]
    return {
        "chain": next_chain,
        "synchronization": state,
        "validation": {"valid": True, "errors": []},
        "states": ["SYNCHRONIZED"],
    }
