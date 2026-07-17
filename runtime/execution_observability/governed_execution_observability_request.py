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
    identity_value = deepcopy(value)
    identity_adapter = identity_value["adapter_response"]
    for diagnostics in (
        identity_adapter.get("dispatch", {}).get("diagnostics", {}),
        identity_adapter.get("receipt", {}).get("transport_diagnostics", {}),
        identity_adapter.get("evidence", {}).get("transport_diagnostics", {}),
    ):
        diagnostics.pop("duration_seconds", None)
    replay_identity = stable_hash(identity_value)
    return {
        "execution_observability_request_id": f"EXEC-OBS-REQUEST-{replay_identity[:24]}",
        **value,
        "replay_identity": replay_identity,
    }
