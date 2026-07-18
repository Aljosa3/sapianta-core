"""Replay helpers for governed Codex task synthesis."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def build_codex_synthesis_replay_identity(*, request: dict, synthesis: dict) -> str:
    return stable_hash(
        {
            "governed_codex_task_request_id": request.get("governed_codex_task_request_id", ""),
            "natural_language": request.get("natural_language", ""),
            "worker_execution_contract": request.get("worker_execution_contract"),
            "synthesis": synthesis,
        }
    )
