"""Fail-closed validation for governed Codex handoff packages."""

from __future__ import annotations

SUPPORTED_TASK_CLASSES = {
    "GOVERNANCE_ARTIFACT_TASK",
    "VALIDATION_TASK",
    "TEST_GENERATION_TASK",
    "FINALIZE_TASK",
}

REQUIRED_BLOCKED_CAPABILITIES = {
    "shell",
    "orchestrate",
    "continue automatically",
    "retry",
    "subprocess",
    "network",
}


def validate_handoff_package(package: dict) -> dict:
    errors = []
    if not isinstance(package, dict):
        return {"valid": False, "errors": [{"field": "package", "reason": "malformed package"}]}
    if package.get("status") != "HANDOFF_READY":
        errors.append({"field": "status", "reason": "handoff not ready"})
    if package.get("task_class") not in SUPPORTED_TASK_CLASSES:
        errors.append({"field": "task_class", "reason": "unsupported task class"})
    if package.get("governance_mode") != "BOUNDED_CODEX_SYNTHESIS":
        errors.append({"field": "governance_mode", "reason": "invalid governance mode"})
    if not isinstance(package.get("replay_identity"), str) or not package["replay_identity"].strip():
        errors.append({"field": "replay_identity", "reason": "missing replay identity"})
    if package.get("requires_confirmation") is not True:
        errors.append({"field": "requires_confirmation", "reason": "approval required"})
    if package.get("allowed_to_execute_automatically") is not False:
        errors.append({"field": "allowed_to_execute_automatically", "reason": "automatic execution forbidden"})
    if package.get("downstream_execution_authority") is not False:
        errors.append({"field": "downstream_execution_authority", "reason": "authority escalation forbidden"})
    blocked = set(package.get("blocked_capabilities", []))
    if not REQUIRED_BLOCKED_CAPABILITIES.issubset(blocked):
        errors.append({"field": "blocked_capabilities", "reason": "missing blocked guarantees"})
    for field in ("shell_execution", "orchestration", "hidden_continuation", "hidden_retry"):
        if package.get(field) is True:
            errors.append({"field": field, "reason": "prohibited capability"})
    if not isinstance(package.get("codex_prompt"), str) or not package["codex_prompt"].strip():
        errors.append({"field": "codex_prompt", "reason": "missing prompt"})
    return {"valid": not errors, "errors": errors}
