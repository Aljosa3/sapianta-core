"""Deterministic downstream execution authorization requests."""

from __future__ import annotations

from copy import deepcopy

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def create_execution_authorization_request(
    *,
    handoff_package: dict,
    approved_by: str,
    approval_timestamp: str,
) -> dict:
    handoff_copy = deepcopy(handoff_package)
    handoff_package_sha256 = stable_hash(handoff_copy)
    value = {
        "handoff_package": handoff_copy,
        "handoff_package_sha256": handoff_package_sha256,
        "approved_by": approved_by,
        "approval_timestamp": approval_timestamp,
    }
    replay_identity = stable_hash(value)
    return {
        "execution_authorization_request_id": f"EXEC-AUTH-REQUEST-{replay_identity[:24]}",
        **value,
        "replay_identity": replay_identity,
        "explicit_approval": approved_by == "human",
    }
