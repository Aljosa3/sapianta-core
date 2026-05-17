"""Deterministic governed UX interaction sessions."""

from __future__ import annotations

from copy import deepcopy

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

ALLOWED_INTERACTION_SCOPE = "GOVERNED_OPERATIONAL_INTERACTION"


def create_governed_interaction_session(*, interaction_seed: dict, lineage: dict) -> dict:
    value = {
        "interaction_seed": interaction_seed,
        "lineage": lineage,
        "interaction_scope": ALLOWED_INTERACTION_SCOPE,
    }
    replay_identity = stable_hash(value)
    return {
        "governed_interaction_session_id": f"GOVERNED-INTERACTION-SESSION-{replay_identity[:24]}",
        "interaction_seed": deepcopy(interaction_seed),
        "lineage": deepcopy(lineage),
        "interaction_scope": ALLOWED_INTERACTION_SCOPE,
        "replay_identity": replay_identity,
        "interactions": [],
        "interaction_count": 0,
        "interaction_head_hash": "",
        "closed": False,
        "closure_id": "",
        "bounded": True,
    }
