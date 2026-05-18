"""Deterministic requests for bounded Codex task synthesis."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def create_governed_codex_task_request(*, natural_language: str) -> dict:
    replay_identity = stable_hash({"natural_language": natural_language})
    return {
        "governed_codex_task_request_id": f"GOVERNED-CODEX-TASK-REQUEST-{replay_identity[:24]}",
        "natural_language": natural_language,
        "replay_identity": replay_identity,
        "bounded": True,
    }
