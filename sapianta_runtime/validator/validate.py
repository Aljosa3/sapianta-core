# sapianta_runtime/validator/validate.py

ALLOWED_DECISIONS = {"ADD", "REPLACE", "DEPRECATE", "REVOKE"}


def validate_cdr(cdr):
    if "decision_type" not in cdr:
        return False

    if cdr["decision_type"] not in ALLOWED_DECISIONS:
        return False

    if "target" not in cdr:
        return False

    return True


def validate_all(cdrs):
    for cdr in cdrs:
        if not validate_cdr(cdr):
            return False
    return True
