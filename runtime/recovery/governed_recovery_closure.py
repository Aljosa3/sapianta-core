"""Deterministic governed operational recovery closure."""

from __future__ import annotations

from copy import deepcopy

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

from .governed_recovery_replay import validate_recovery_replay


def close_governed_recovery_chain(*, chain: dict) -> dict:
    validation = validate_recovery_replay(chain)
    if not validation["valid"] or chain.get("closed") is True or chain.get("recovery_count", 0) == 0:
        errors = list(validation["errors"])
        if chain.get("closed") is True:
            errors.append({"field": "closed", "reason": "invalid recovery closure"})
        if chain.get("recovery_count", 0) == 0:
            errors.append({"field": "recovery_count", "reason": "invalid recovery closure"})
        return {"chain": deepcopy(chain), "validation": {"valid": False, "errors": errors}, "states": ["BLOCKED"]}
    value = {
        "governed_recovery_chain_id": chain["governed_recovery_chain_id"],
        "final_recovery_hash": chain["recovery_head_hash"],
        "recovery_count": chain["recovery_count"],
        "replay_identity": chain["replay_identity"],
    }
    closure_hash = stable_hash(value)
    closure = {
        **value,
        "governed_recovery_closure_id": f"GOVERNED-RECOVERY-CLOSURE-{closure_hash[:24]}",
        "closure_sha256": closure_hash,
        "replay_safe": True,
    }
    closed_chain = deepcopy(chain)
    closed_chain["closed"] = True
    closed_chain["closure_id"] = closure["governed_recovery_closure_id"]
    return {
        "chain": closed_chain,
        "closure": closure,
        "validation": {"valid": True, "errors": []},
        "states": ["RECOVERY_CLOSED"],
    }
