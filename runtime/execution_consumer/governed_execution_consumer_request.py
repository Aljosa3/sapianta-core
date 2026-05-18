"""Deterministic requests for the mock-only execution consumer."""

from __future__ import annotations

from copy import deepcopy

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def create_execution_consumer_request(
    *,
    handoff_package: dict,
    authority_token: dict,
    now: str,
    revoked_token_ids: set[str] | None = None,
) -> dict:
    package = deepcopy(handoff_package)
    token = deepcopy(authority_token)
    package_hash = stable_hash(package)
    value = {
        "handoff_package": package,
        "handoff_package_sha256": package_hash,
        "authority_token": token,
        "now": now,
        "revoked_token_ids": sorted(revoked_token_ids or set()),
    }
    replay_identity = stable_hash(value)
    return {
        "execution_consumer_request_id": f"EXEC-CONSUMER-REQUEST-{replay_identity[:24]}",
        **value,
        "replay_identity": replay_identity,
    }
