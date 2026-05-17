"""Deterministic governed synchronization closure."""

from __future__ import annotations

from copy import deepcopy

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

from .governed_synchronization_replay import validate_synchronization_replay


def close_governed_synchronization_chain(*, chain: dict) -> dict:
    validation = validate_synchronization_replay(chain)
    if not validation["valid"] or chain.get("closed") is True or chain.get("synchronization_count", 0) == 0:
        errors = list(validation["errors"])
        if chain.get("closed") is True:
            errors.append({"field": "closed", "reason": "invalid synchronization closure"})
        if chain.get("synchronization_count", 0) == 0:
            errors.append({"field": "synchronization_count", "reason": "invalid synchronization closure"})
        return {"chain": deepcopy(chain), "validation": {"valid": False, "errors": errors}, "states": ["BLOCKED"]}
    value = {
        "governed_synchronization_chain_id": chain["governed_synchronization_chain_id"],
        "final_synchronization_hash": chain["synchronization_head_hash"],
        "synchronization_count": chain["synchronization_count"],
        "replay_identity": chain["replay_identity"],
    }
    closure_hash = stable_hash(value)
    closure = {
        **value,
        "governed_synchronization_closure_id": f"GOVERNED-SYNCHRONIZATION-CLOSURE-{closure_hash[:24]}",
        "closure_sha256": closure_hash,
        "replay_safe": True,
    }
    closed_chain = deepcopy(chain)
    closed_chain["closed"] = True
    closed_chain["closure_id"] = closure["governed_synchronization_closure_id"]
    return {"chain": closed_chain, "closure": closure, "validation": {"valid": True, "errors": []}, "states": ["SYNCHRONIZATION_CLOSED"]}
