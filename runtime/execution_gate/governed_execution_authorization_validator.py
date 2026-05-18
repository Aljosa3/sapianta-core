"""Fail-closed validation for execution authorization."""

from __future__ import annotations

from datetime import datetime, timezone

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash
from sapianta_system.runtime.codex_handoff.governed_codex_handoff_validator import (
    SUPPORTED_TASK_CLASSES,
    validate_handoff_package,
)


def _parse(timestamp: str) -> datetime:
    return datetime.fromisoformat(timestamp.replace("Z", "+00:00")).astimezone(timezone.utc)


def validate_authorization_request(request: dict) -> dict:
    errors = []
    package = request.get("handoff_package", {})
    package_validation = validate_handoff_package(package)
    if not package_validation["valid"]:
        errors.extend(package_validation["errors"])
    if request.get("explicit_approval") is not True or request.get("approved_by") != "human":
        errors.append({"field": "explicit_approval", "reason": "implicit approval forbidden"})
    if request.get("handoff_package_sha256") != stable_hash(package):
        errors.append({"field": "handoff_package", "reason": "mutated handoff package"})
    try:
        _parse(request.get("approval_timestamp", ""))
    except (TypeError, ValueError):
        errors.append({"field": "approval_timestamp", "reason": "invalid approval timestamp"})
    return {"valid": not errors, "errors": errors}


def validate_authority_token(
    token: dict,
    *,
    now: str,
    used_token_ids: set[str] | None = None,
    revoked_token_ids: set[str] | None = None,
) -> dict:
    errors = []
    if not isinstance(token, dict):
        return {"valid": False, "errors": [{"field": "token", "reason": "malformed authority token"}]}
    for field in ("token_id", "replay_identity", "approval_timestamp", "authorization_expiration"):
        if not isinstance(token.get(field), str) or not token[field].strip():
            errors.append({"field": field, "reason": "malformed authority token"})
    if token.get("approved_task_class") not in SUPPORTED_TASK_CLASSES:
        errors.append({"field": "approved_task_class", "reason": "unsupported task class"})
    if token.get("downstream_execution_authority") is not True:
        errors.append({"field": "downstream_execution_authority", "reason": "authority missing"})
    if token.get("execution_window_seconds") != 300:
        errors.append({"field": "execution_window_seconds", "reason": "authority extension forbidden"})
    if token.get("revocation_supported") is not True:
        errors.append({"field": "revocation_supported", "reason": "revocation required"})
    used_token_ids = used_token_ids or set()
    revoked_token_ids = revoked_token_ids or set()
    if token.get("token_id") in used_token_ids:
        errors.append({"field": "token_id", "reason": "reused authorization token"})
    if token.get("token_id") in revoked_token_ids:
        errors.append({"field": "token_id", "reason": "revoked authorization token"})
    try:
        if _parse(now) >= _parse(token.get("authorization_expiration", "")):
            errors.append({"field": "authorization_expiration", "reason": "expired authority"})
    except (TypeError, ValueError):
        errors.append({"field": "authorization_expiration", "reason": "invalid expiration"})
    return {"valid": not errors, "errors": errors}
