"""Replay helpers for governed transfer ingestion."""

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def build_intent_transfer_ingestion_replay_identity(*, request: dict, validation: dict, intake: dict) -> str:
    return stable_hash(
        {
            "governed_intent_transfer_ingestion_request_id": request.get(
                "governed_intent_transfer_ingestion_request_id", ""
            ),
            "validation": validation,
            "intake": intake,
        }
    )
