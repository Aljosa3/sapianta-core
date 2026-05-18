"""Replay identity helpers for execution observability."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def build_execution_observability_replay_identity(*, request: dict, validation: dict) -> str:
    return stable_hash(
        {
            "execution_observability_request_id": request["execution_observability_request_id"],
            "validation": validation,
        }
    )
