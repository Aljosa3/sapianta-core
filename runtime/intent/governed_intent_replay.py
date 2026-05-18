"""Replay helpers for governed intent interpretation."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def build_intent_replay_identity(*, request: dict, interpretation: dict) -> str:
    return stable_hash(
        {
            "governed_intent_request_id": request.get("governed_intent_request_id", ""),
            "natural_language": request.get("natural_language", ""),
            "interpretation": interpretation,
        }
    )
