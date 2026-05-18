"""Fail-closed validation for read-only execution observability."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash
from sapianta_system.runtime.codex_handoff.governed_codex_handoff_validator import validate_handoff_package


def validate_execution_observability_request(request: dict) -> dict:
    errors = []
    package = request.get("handoff_package", {})
    token = request.get("authority_token", {})
    consumer = request.get("consumer_response", {})
    adapter = request.get("adapter_response", {})

    package_validation = validate_handoff_package(package)
    if not package_validation["valid"]:
        errors.extend(package_validation["errors"])
    if request.get("handoff_package_sha256") != stable_hash(package):
        errors.append({"field": "handoff_package", "reason": "handoff mismatch"})
    if token.get("handoff_package_sha256") != request.get("handoff_package_sha256"):
        errors.append({"field": "authority_token", "reason": "handoff mismatch"})
    for field in ("token_id", "replay_identity", "approved_task_class", "governance_mode"):
        if not isinstance(token.get(field), str) or not token[field].strip():
            errors.append({"field": field, "reason": "malformed authority token"})
    if not isinstance(consumer, dict) or not isinstance(consumer.get("receipt"), dict):
        errors.append({"field": "consumer_response", "reason": "malformed consumer receipt"})
    if not isinstance(adapter, dict) or not isinstance(adapter.get("receipt"), dict):
        errors.append({"field": "adapter_response", "reason": "malformed adapter receipt"})
    if isinstance(consumer.get("receipt"), dict) and consumer["receipt"].get("authority_token_id") != token.get("token_id"):
        errors.append({"field": "consumer_response", "reason": "authority token mismatch"})
    if isinstance(adapter.get("receipt"), dict) and adapter["receipt"].get("authority_token_id") != token.get("token_id"):
        errors.append({"field": "adapter_response", "reason": "authority token mismatch"})
    return {"valid": not errors, "errors": errors}
