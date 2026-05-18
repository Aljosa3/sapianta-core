"""Replay helpers for governed intent transfer packages."""

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def build_intent_transfer_replay_identity(*, request: dict, package: dict) -> str:
    return stable_hash(
        {
            "governed_intent_transfer_request_id": request.get("governed_intent_transfer_request_id", ""),
            "package": package,
        }
    )
