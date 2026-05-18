"""Bounded governed Codex task synthesis responses."""

from __future__ import annotations

from .governed_codex_evidence import governed_codex_synthesis_evidence
from .governed_codex_prompt_synthesizer import synthesize_codex_prompt
from .governed_codex_prompt_validator import validate_codex_prompt
from .governed_codex_replay import build_codex_synthesis_replay_identity
from .governed_codex_task_classifier import BLOCKED_MARKERS, classify_governed_codex_task

GOVERNANCE_MODE = "BOUNDED_CODEX_SYNTHESIS"


def _request_valid(request: dict) -> dict:
    errors = []
    if not isinstance(request, dict):
        return {"valid": False, "errors": [{"field": "request", "reason": "malformed request"}]}
    value = request.get("natural_language")
    if not isinstance(value, str) or not value.strip():
        errors.append({"field": "natural_language", "reason": "must be non-empty"})
    if isinstance(value, str) and len(value) > 240:
        errors.append({"field": "natural_language", "reason": "must remain bounded"})
    return {"valid": not errors, "errors": errors}


def _blocked(request: dict, errors: list[dict]) -> dict:
    response = {
        "status": "BLOCKED",
        "task_class": None,
        "governance_mode": GOVERNANCE_MODE,
        "requires_confirmation": True,
        "allowed_to_execute_automatically": False,
        "codex_prompt_preview": None,
        "replay_visible": True,
        "blocked_capability_checks": list(BLOCKED_MARKERS),
        "closure": "BLOCKED",
        "validation": {"valid": False, "errors": errors},
    }
    response["replay_identity"] = build_codex_synthesis_replay_identity(request=request, synthesis=response.copy())
    response["evidence"] = governed_codex_synthesis_evidence(request=request, response=response)
    return response


def synthesize_governed_codex_task(request: dict) -> dict:
    request_validation = _request_valid(request)
    if not request_validation["valid"]:
        return _blocked(request, request_validation["errors"])
    classification = classify_governed_codex_task(request["natural_language"])
    if not classification["valid"]:
        return _blocked(request, [{"field": "natural_language", "reason": classification["reason"]}])
    prompt = synthesize_codex_prompt(task_class=classification["task_class"], natural_language=request["natural_language"])
    prompt_validation = validate_codex_prompt(prompt)
    if not prompt_validation["valid"]:
        return _blocked(request, prompt_validation["errors"])
    response = {
        "status": "SYNTHESIZED",
        "task_class": classification["task_class"],
        "governance_mode": GOVERNANCE_MODE,
        "requires_confirmation": True,
        "allowed_to_execute_automatically": False,
        "codex_prompt_preview": prompt,
        "replay_visible": True,
        "blocked_capability_checks": list(BLOCKED_MARKERS),
        "closure": "PREVIEW",
        "validation": prompt_validation,
    }
    response["replay_identity"] = build_codex_synthesis_replay_identity(request=request, synthesis=response.copy())
    response["evidence"] = governed_codex_synthesis_evidence(request=request, response=response)
    return response
