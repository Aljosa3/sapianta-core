ALLOWED_DECISIONS = {"ADD", "REPLACE", "DEPRECATE", "REVOKE"}


class ValidationError(RuntimeError):
    pass


def validate_cdr(cdr):
    if not isinstance(cdr, dict):
        raise ValidationError("CDR must be a dict")

    if "decision_type" not in cdr:
        raise ValidationError("Missing decision_type")

    decision_type = cdr["decision_type"]

    if decision_type not in ALLOWED_DECISIONS:
        raise ValidationError(f"Unknown decision_type: {decision_type}")

    if "target" not in cdr:
        raise ValidationError("Missing target")

    if decision_type == "REPLACE":
        if "replaces" not in cdr:
            raise ValidationError("REPLACE requires 'replaces' field")
        if cdr["replaces"] == cdr["target"]:
            raise ValidationError("REPLACE target and replaces cannot be identical")

    if decision_type in {"DEPRECATE", "REVOKE"}:
        # target must exist logically; existence is checked later against state
        pass

    return True


def validate_all(cdrs):
    if not isinstance(cdrs, list):
        raise ValidationError("CDRs must be a list")

    for cdr in cdrs:
        validate_cdr(cdr)

    return True
