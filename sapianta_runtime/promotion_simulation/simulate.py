from typing import Dict, List
from copy import deepcopy

from sapianta_runtime.validator.validate import validate_all, ValidationError


def simulate_promotion(
    base_state: Dict[str, str],
    hypothetical_cdrs: List[dict]
) -> Dict[str, Dict[str, str]]:
    """
    READ-ONLY promotion simulation.

    Applies hypothetical CDRs on top of an existing canonical state,
    without mutating it.
    """

    validate_all(hypothetical_cdrs)

    before = deepcopy(base_state)
    state = deepcopy(base_state)

    for cdr in hypothetical_cdrs:
        decision_type = cdr["decision_type"]
        target = cdr["target"]

        if decision_type == "ADD":
            if target in state:
                raise ValidationError(f"ADD on existing target: {target}")
            state[target] = "ACTIVE"

        elif decision_type == "REPLACE":
            replaced = cdr["replaces"]
            if replaced not in state:
                raise ValidationError(f"REPLACE refers to unknown target: {replaced}")
            state[replaced] = "SUPERSEDED"
            state[target] = "ACTIVE"

        elif decision_type == "DEPRECATE":
            if target not in state:
                raise ValidationError(f"DEPRECATE refers to unknown target: {target}")
            state[target] = "DEPRECATED"

        elif decision_type == "REVOKE":
            if target not in state:
                raise ValidationError(f"REVOKE refers to unknown target: {target}")
            state[target] = "REVOKED"

        else:
            raise ValidationError("Unknown decision type")

    diff: Dict[str, str] = {}
    keys = set(before.keys()) | set(state.keys())

    for k in sorted(keys):
        b = before.get(k, "ABSENT")
        a = state.get(k, "ABSENT")
        if b != a:
            diff[k] = f"{b} → {a}"

    return {
        "would_change": bool(diff),
        "before": before,
        "after": state,
        "diff": diff,
    }
