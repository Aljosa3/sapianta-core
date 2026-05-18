"""Deterministic requests for governed intent transfer packaging."""

from copy import deepcopy

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def create_intent_transfer_request(
    *,
    conversational_input: str,
    normalized_governed_request: dict,
    governance_mode: str,
    replay_identity: str,
) -> dict:
    normalized = deepcopy(normalized_governed_request)
    value = {
        "conversational_input": conversational_input,
        "normalized_governed_request": normalized,
        "governance_mode": governance_mode,
        "bridge_replay_identity": replay_identity,
    }
    request_replay_identity = stable_hash(value)
    return {
        "governed_intent_transfer_request_id": f"GOV-INTENT-TRANSFER-REQUEST-{request_replay_identity[:24]}",
        **value,
        "replay_identity": request_replay_identity,
        "bounded": True,
    }
