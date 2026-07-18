"""Fail-closed validation for synthesized Codex prompt previews."""

from __future__ import annotations

REQUIRED_SECTIONS = (
    "GOAL:",
    "CURRENT CONTEXT:",
    "ALLOWED SCOPE:",
    "PROHIBITED ACTIONS:",
    "VALIDATION REQUIREMENTS:",
    "REPLAY REQUIREMENTS:",
    "TEST REQUIREMENTS:",
    "ACCEPTANCE CRITERIA:",
    "FINAL RESPONSE REQUIREMENTS:",
)

WORKER_EXECUTION_SECTIONS = (
    "WORKER ROLE:",
    "PRIMARY AUTHORIZED TASK:",
    "GROUNDED TARGETS:",
    "REQUIRED OUTPUT:",
)

ORCHESTRATION_PRIMARY_INSTRUCTIONS = (
    "Prepare a bounded runtime validation task.",
    "Preview-only downstream Codex task formation",
    "describe what another Worker should do",
    "return an invocation plan",
)


def validate_codex_prompt(prompt: str, *, worker_execution_contract: dict | None = None) -> dict:
    errors = []
    if not isinstance(prompt, str) or not prompt.strip():
        errors.append({"field": "codex_prompt_preview", "reason": "prompt missing"})
    if isinstance(prompt, str) and len(prompt) > 2400:
        errors.append({"field": "codex_prompt_preview", "reason": "prompt must remain bounded"})
    for section in REQUIRED_SECTIONS:
        if section not in prompt:
            errors.append({"field": "codex_prompt_preview", "reason": f"missing section {section}"})
    if worker_execution_contract is not None:
        for section in WORKER_EXECUTION_SECTIONS:
            if section not in prompt:
                errors.append({"field": "codex_prompt_preview", "reason": f"missing section {section}"})
        for instruction in ORCHESTRATION_PRIMARY_INSTRUCTIONS:
            if instruction in prompt:
                errors.append({
                    "field": "codex_prompt_preview",
                    "reason": "orchestration instruction replaced Worker task",
                })
    return {"valid": not errors, "errors": errors}
