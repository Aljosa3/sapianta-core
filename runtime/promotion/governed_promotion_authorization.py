"""Explicit governed promotion authorization rules."""

ALLOWED_CERTIFICATION_SCOPE = "BOUNDED_OPERATIONAL_STATE_ELIGIBILITY"
REQUIRED_AUTHORIZATION_FIELDS = (
    "promotion_authorization_id",
    "authorization_source",
    "approved_by",
)


def validate_promotion_authorization(authorization: dict) -> dict:
    errors = []
    if not isinstance(authorization, dict):
        return {"valid": False, "errors": [{"field": "authorization", "reason": "unauthorized promotion"}]}
    for field in REQUIRED_AUTHORIZATION_FIELDS:
        value = authorization.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append({"field": field, "reason": "unauthorized promotion"})
    if authorization.get("approved_by") != "human":
        errors.append({"field": "approved_by", "reason": "unauthorized promotion"})
    if authorization.get("promotion_authorized") is not True:
        errors.append({"field": "promotion_authorized", "reason": "unauthorized promotion"})
    return {"valid": not errors, "errors": errors}
