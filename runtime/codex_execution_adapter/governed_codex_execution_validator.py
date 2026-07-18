"""Fail-closed validation for bounded Codex execution requests."""

from __future__ import annotations

from hashlib import sha256

from sapianta_bridge.provider_connectors.bounded_codex_execution import (
    bounded_codex_command,
    validate_bounded_codex_command,
)
from sapianta_system.runtime.execution_consumer.governed_execution_consumer_validator import (
    validate_execution_consumer_request,
)


def validate_codex_execution_request(request: dict) -> dict:
    errors = []
    consumer_validation = validate_execution_consumer_request(request)
    errors.extend(consumer_validation["errors"])
    prompt = request.get("handoff_package", {}).get("codex_prompt", "")
    prompt_hash = sha256(prompt.encode("utf-8")).hexdigest()
    if request.get("bounded_prompt_sha256") != prompt_hash:
        errors.append({"field": "bounded_prompt_sha256", "reason": "prompt hash mismatch"})
    command = bounded_codex_command(codex_executable=request.get("codex_executable", ""), bounded_prompt=prompt)
    command_validation = validate_bounded_codex_command(
        codex_executable=request.get("codex_executable", ""),
        command=command,
    )
    errors.extend(command_validation["errors"])
    timeout = request.get("timeout_seconds")
    if not isinstance(timeout, int) or timeout <= 0 or timeout > 120:
        errors.append({"field": "timeout_seconds", "reason": "timeout must remain bounded"})
    return {
        "valid": not errors,
        "errors": errors,
        "consumer_validation": consumer_validation,
        "command_validation": command_validation,
        "bounded_prompt_sha256": prompt_hash,
        "command": command,
    }
