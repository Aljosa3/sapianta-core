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


def validate_codex_prompt(prompt: str) -> dict:
    errors = []
    if not isinstance(prompt, str) or not prompt.strip():
        errors.append({"field": "codex_prompt_preview", "reason": "prompt missing"})
    if isinstance(prompt, str) and len(prompt) > 2400:
        errors.append({"field": "codex_prompt_preview", "reason": "prompt must remain bounded"})
    for section in REQUIRED_SECTIONS:
        if section not in prompt:
            errors.append({"field": "codex_prompt_preview", "reason": f"missing section {section}"})
    return {"valid": not errors, "errors": errors}
