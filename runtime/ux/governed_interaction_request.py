"""Deterministic governed UX request records."""

from __future__ import annotations

from copy import deepcopy

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def create_governed_interaction_request(*, session: dict, interaction_payload: dict) -> dict:
    value = {
        "governed_interaction_session_id": session["governed_interaction_session_id"],
        "interaction_index": session["interaction_count"] + 1,
        "previous_interaction_hash": session["interaction_head_hash"],
        "interaction_payload": deepcopy(interaction_payload),
    }
    request_hash = stable_hash(value)
    return {
        **value,
        "governed_interaction_request_id": f"GOVERNED-INTERACTION-REQUEST-{request_hash[:24]}",
        "request_hash": request_hash,
    }
