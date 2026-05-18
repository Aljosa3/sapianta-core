"""Replay helpers for governed Codex handoff packages."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def build_handoff_replay_identity(*, request: dict, package_seed: dict) -> str:
    return stable_hash(
        {
            "governed_codex_handoff_request_id": request.get("governed_codex_handoff_request_id", ""),
            "original_human_request": request.get("original_human_request", ""),
            "package_seed": package_seed,
        }
    )


def build_export_identity(package_seed: dict) -> str:
    return f"GOVERNED-CODEX-HANDOFF-EXPORT-{stable_hash(package_seed)[:24]}"
