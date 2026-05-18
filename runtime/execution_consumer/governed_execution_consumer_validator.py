"""Fail-closed validation for mock execution consumption."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash
from sapianta_system.runtime.codex_handoff.governed_codex_handoff_validator import (
    REQUIRED_BLOCKED_CAPABILITIES,
    validate_handoff_package,
)
from sapianta_system.runtime.execution_gate.governed_execution_authorization_validator import validate_authority_token


def validate_execution_consumer_request(request: dict) -> dict:
    errors = []
    package = request.get("handoff_package", {})
    token = request.get("authority_token", {})
    package_validation = validate_handoff_package(package)
    if not package_validation["valid"]:
        errors.extend(package_validation["errors"])
    if request.get("handoff_package_sha256") != stable_hash(package):
        errors.append({"field": "handoff_package", "reason": "handoff mismatch"})
    if token.get("handoff_package_sha256") != request.get("handoff_package_sha256"):
        errors.append({"field": "handoff_package_sha256", "reason": "handoff mismatch"})
    token_validation = validate_authority_token(
        token,
        now=request.get("now", ""),
        revoked_token_ids=set(request.get("revoked_token_ids", [])),
    )
    if not token_validation["valid"]:
        errors.extend(token_validation["errors"])
    if token.get("governance_mode") != package.get("governance_mode"):
        errors.append({"field": "governance_mode", "reason": "governance mode mismatch"})
    if token.get("approved_task_class") != package.get("task_class"):
        errors.append({"field": "approved_task_class", "reason": "task class mismatch"})
    if set(package.get("blocked_capabilities", [])) != set(token.get("blocked_capabilities", [])):
        errors.append({"field": "blocked_capabilities", "reason": "blocked capability mismatch"})
    if not REQUIRED_BLOCKED_CAPABILITIES.issubset(set(token.get("blocked_capabilities", []))):
        errors.append({"field": "blocked_capabilities", "reason": "blocked capability guarantee missing"})
    for field in ("shell_execution", "orchestration", "hidden_continuation", "hidden_retry"):
        if package.get(field) is True:
            errors.append({"field": field, "reason": "blocked capability detected"})
    return {"valid": not errors, "errors": errors}
