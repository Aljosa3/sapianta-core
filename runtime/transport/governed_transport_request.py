"""Deterministic governed live transport request."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def create_governed_transport_request(*, request_payload: dict, lineage: dict) -> dict:
    value = {
        "request_payload": request_payload,
        "lineage": lineage,
    }
    replay_identity = stable_hash(value)
    return {
        "governed_transport_request_id": f"GOVERNED-TRANSPORT-REQUEST-{replay_identity[:24]}",
        "request_payload": request_payload,
        "lineage": lineage,
        "replay_identity": replay_identity,
        "bounded": True,
    }
