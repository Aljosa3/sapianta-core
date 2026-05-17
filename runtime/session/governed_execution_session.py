"""Deterministic governed execution session creation."""

from __future__ import annotations

from copy import deepcopy

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def create_governed_execution_session(*, session_seed: dict, lineage: dict) -> dict:
    value = {"session_seed": session_seed, "lineage": lineage}
    replay_identity = stable_hash(value)
    return {
        "governed_execution_session_id": f"GOVERNED-EXECUTION-SESSION-{replay_identity[:24]}",
        "session_seed": deepcopy(session_seed),
        "lineage": deepcopy(lineage),
        "replay_identity": replay_identity,
        "exchanges": [],
        "exchange_count": 0,
        "session_head_hash": "",
        "closed": False,
        "closure_id": "",
        "bounded": True,
    }
