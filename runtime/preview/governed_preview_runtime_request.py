"""Deterministic localhost preview runtime requests."""

from __future__ import annotations

from copy import deepcopy

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

LOCALHOST_HOST = "127.0.0.1"
DEFAULT_PREVIEW_PORT = 8010


def create_preview_runtime_request(*, request_payload: dict, lineage: dict) -> dict:
    value = {"request_payload": request_payload, "lineage": lineage}
    replay_identity = stable_hash(value)
    return {
        "preview_runtime_request_id": f"PREVIEW-RUNTIME-REQUEST-{replay_identity[:24]}",
        "request_payload": deepcopy(request_payload),
        "lineage": deepcopy(lineage),
        "replay_identity": replay_identity,
        "bounded": True,
    }
