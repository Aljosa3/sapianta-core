"""Replay validation for governed synchronization chains."""

from __future__ import annotations

from copy import deepcopy

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

from .governed_synchronization_validator import validate_synchronization_chain


def validate_synchronization_replay(chain: dict) -> dict:
    before = stable_hash(chain)
    snapshot = deepcopy(chain)
    validation = validate_synchronization_chain(chain)
    after = stable_hash(chain)
    mutated = snapshot != chain or before != after
    errors = list(validation["errors"])
    if mutated:
        errors.append({"field": "chain", "reason": "hidden synchronization mutation"})
    return {"valid": not errors, "errors": errors, "read_only": not mutated}
