"""Deterministic request objects for bounded intent interpretation."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def create_governed_intent_request(*, natural_language: str) -> dict:
    value = {"natural_language": natural_language}
    replay_identity = stable_hash(value)
    return {
        "governed_intent_request_id": f"GOVERNED-INTENT-REQUEST-{replay_identity[:24]}",
        "natural_language": natural_language,
        "replay_identity": replay_identity,
        "bounded": True,
    }
