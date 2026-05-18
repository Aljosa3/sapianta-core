"""Governed Codex handoff package response construction."""

from __future__ import annotations

from .governed_codex_handoff_evidence import governed_codex_handoff_evidence
from .governed_codex_handoff_package import build_handoff_package
from .governed_codex_handoff_replay import build_export_identity, build_handoff_replay_identity
from .governed_codex_handoff_validator import validate_handoff_package


def _blocked(request: dict, errors: list[dict]) -> dict:
    return {
        "status": "BLOCKED",
        "requires_confirmation": True,
        "allowed_to_execute_automatically": False,
        "downstream_execution_authority": False,
        "validation": {"valid": False, "errors": errors},
        "closure": "BLOCKED",
    }


def create_governed_codex_handoff(request: dict) -> dict:
    synthesis = request.get("synthesis_response", {})
    if synthesis.get("status") != "SYNTHESIZED":
        return _blocked(request, [{"field": "synthesis_response", "reason": "synthesis not admitted"}])
    package_seed = {
        "task_class": synthesis.get("task_class"),
        "governance_mode": synthesis.get("governance_mode"),
        "codex_prompt": synthesis.get("codex_prompt_preview"),
        "blocked_capabilities": synthesis.get("blocked_capability_checks"),
    }
    replay_identity = build_handoff_replay_identity(request=request, package_seed=package_seed)
    export_identity = build_export_identity(package_seed)
    package = build_handoff_package(
        synthesis_response=synthesis,
        replay_identity=replay_identity,
        export_identity=export_identity,
    )
    validation = validate_handoff_package(package)
    if not validation["valid"]:
        return _blocked(request, validation["errors"])
    return {
        **package,
        "validation": validation,
        "evidence": governed_codex_handoff_evidence(request=request, package=package, validation=validation),
    }
