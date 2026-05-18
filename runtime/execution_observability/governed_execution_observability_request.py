"""Deterministic read-only observability requests."""

from __future__ import annotations

from copy import deepcopy

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def create_execution_observability_request(
    *,
    handoff_package: dict,
    authority_token: dict,
    consumer_response: dict,
    adapter_response: dict,
    now: str,
    revoked_token_ids: set[str] | None = None,
) -> dict:
    package = deepcopy(handoff_package)
    token = deepcopy(authority_token)
    consumer = deepcopy(consumer_response)
    adapter = deepcopy(adapter_response)
    value = {
        "handoff_package": package,
        "handoff_package_sha256": stable_hash(package),
        "authority_token": token,
        "consumer_response": consumer,
        "adapter_response": adapter,
        "now": now,
        "revoked_token_ids": sorted(revoked_token_ids or set()),
    }
    replay_identity = stable_hash(value)
    return {
        "execution_observability_request_id": f"EXEC-OBS-REQUEST-{replay_identity[:24]}",
        **value,
        "replay_identity": replay_identity,
    }
