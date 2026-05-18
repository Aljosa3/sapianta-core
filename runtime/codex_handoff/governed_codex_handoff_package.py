"""Deterministic package and export construction for governed handoffs."""

from __future__ import annotations

import json
from pathlib import Path

PACKAGE_VERSION = "GOVERNED_CODEX_HANDOFF_PACKAGE_V1"
BOUNDARY_STATEMENT = "AiGOL remains governance authority; Codex remains downstream bounded execution surface."
DISCLAIMER = "This package is non-executing and does not grant downstream execution authority."


def build_handoff_package(*, synthesis_response: dict, replay_identity: str, export_identity: str) -> dict:
    return {
        "package_version": PACKAGE_VERSION,
        "status": "HANDOFF_READY",
        "task_class": synthesis_response["task_class"],
        "governance_mode": synthesis_response["governance_mode"],
        "replay_identity": replay_identity,
        "requires_confirmation": True,
        "allowed_to_execute_automatically": False,
        "downstream_execution_authority": False,
        "codex_prompt": synthesis_response["codex_prompt_preview"],
        "blocked_capabilities": synthesis_response["blocked_capability_checks"],
        "constitutional_boundary_statement": BOUNDARY_STATEMENT,
        "closure": {"state": "HANDOFF_READY", "deterministic": True},
        "downstream_execution_disclaimer": DISCLAIMER,
        "export_identity": export_identity,
    }


def export_handoff_package(*, package: dict, export_dir: Path) -> Path:
    export_dir.mkdir(parents=True, exist_ok=True)
    path = export_dir / f"governed_codex_handoff_{package['replay_identity']}.json"
    path.write_text(json.dumps(package, sort_keys=True, separators=(",", ":")), encoding="utf-8")
    return path
