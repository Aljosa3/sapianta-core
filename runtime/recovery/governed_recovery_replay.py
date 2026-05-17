"""Replay validation for governed operational recovery."""

from __future__ import annotations

from copy import deepcopy

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

from .governed_recovery_validator import validate_recovery_chain


def validate_recovery_replay(chain: dict) -> dict:
    before = stable_hash(chain)
    snapshot = deepcopy(chain)
    validation = validate_recovery_chain(chain)
    after = stable_hash(chain)
    mutated = snapshot != chain or before != after
    errors = list(validation["errors"])
    if mutated:
        errors.append({"field": "chain", "reason": "hidden continuation attempts"})
    return {"valid": not errors, "errors": errors, "read_only": not mutated}
