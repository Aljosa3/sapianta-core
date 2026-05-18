"""Replay helpers for bounded Codex execution."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def build_codex_execution_replay_identity(*, request: dict, validation: dict, dispatch: dict) -> str:
    return stable_hash(
        {
            "codex_execution_request_id": request["codex_execution_request_id"],
            "validation": validation,
            "dispatch": dispatch,
        }
    )
