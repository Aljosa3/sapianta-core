"""Explicit governed recovery authorization rules."""

ALLOWED_RECOVERY_SCOPE = "AUTHORIZED_INTERRUPTION_CONTINUATION"
REQUIRED_AUTHORIZATION_FIELDS = (
    "recovery_authorization_id",
    "authorization_source",
    "approved_by",
)


def validate_recovery_authorization(authorization: dict) -> dict:
    errors = []
    if not isinstance(authorization, dict):
        return {"valid": False, "errors": [{"field": "authorization", "reason": "unauthorized recovery"}]}
    for field in REQUIRED_AUTHORIZATION_FIELDS:
        value = authorization.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append({"field": field, "reason": "unauthorized recovery"})
    if authorization.get("approved_by") != "human":
        errors.append({"field": "approved_by", "reason": "unauthorized recovery"})
    if authorization.get("recovery_authorized") is not True:
        errors.append({"field": "recovery_authorized", "reason": "unauthorized recovery"})
    return {"valid": not errors, "errors": errors}
