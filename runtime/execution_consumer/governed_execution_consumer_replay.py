"""Replay helpers for the mock execution consumer."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def build_consumer_replay_identity(*, request: dict, validation: dict, dispatch: dict) -> str:
    return stable_hash(
        {
            "execution_consumer_request_id": request["execution_consumer_request_id"],
            "validation": validation,
            "dispatch": dispatch,
        }
    )
