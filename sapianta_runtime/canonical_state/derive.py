# sapianta_runtime/canonical_state/derive.py

def derive_canonical_state(cdrs):
    state = {}

    for cdr in cdrs:
        decision_type = cdr.get("decision_type")
        target = cdr.get("target")

        if decision_type == "ADD":
            state[target] = "ACTIVE"

        elif decision_type == "REPLACE":
            replaced = cdr.get("replaces")
            if replaced in state:
                state[replaced] = "SUPERSEDED"
            state[target] = "ACTIVE"

        elif decision_type == "DEPRECATE":
            if target in state:
                state[target] = "DEPRECATED"

        elif decision_type == "REVOKE":
            if target in state:
                state[target] = "REVOKED"

        else:
            raise RuntimeError("Unknown decision type")

    return state
