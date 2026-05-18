"""Deterministic ingestion requests for explicit transfer packages."""

from copy import deepcopy

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def create_intent_transfer_ingestion_request(
    *,
    transfer_package: dict,
    replay_identity: str,
    transfer_identity: str,
) -> dict:
    package = deepcopy(transfer_package)
    value = {
        "transfer_package": package,
        "replay_identity": replay_identity,
        "transfer_identity": transfer_identity,
    }
    request_identity = stable_hash(value)
    return {
        "governed_intent_transfer_ingestion_request_id": f"GOV-INTENT-TRANSFER-INGEST-{request_identity[:24]}",
        **value,
        "request_replay_identity": request_identity,
        "bounded": True,
    }
