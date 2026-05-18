"""Deterministic requests for governed Codex handoff packages."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def create_governed_codex_handoff_request(*, synthesis_response: dict, original_human_request: str) -> dict:
    value = {
        "synthesis_response": synthesis_response,
        "original_human_request": original_human_request,
    }
    replay_identity = stable_hash(value)
    return {
        "governed_codex_handoff_request_id": f"GOVERNED-CODEX-HANDOFF-REQUEST-{replay_identity[:24]}",
        "synthesis_response": synthesis_response,
        "original_human_request": original_human_request,
        "replay_identity": replay_identity,
        "bounded": True,
    }
