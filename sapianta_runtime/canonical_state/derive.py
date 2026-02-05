from sapianta_runtime.validator.validate import ValidationError


def derive_canonical_state(cdrs):
    state = {}

    for cdr in cdrs:
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
            raise ValidationError("Unreachable decision type")

    return state
