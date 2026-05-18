"""Replay helpers for the conversational bridge."""

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def build_chatgpt_bridge_replay_identity(*, request: dict, normalization: dict, boundary_state: dict) -> str:
    return stable_hash(
        {
            "governed_chatgpt_bridge_request_id": request.get("governed_chatgpt_bridge_request_id", ""),
            "conversational_input": request.get("conversational_input", ""),
            "normalization": normalization,
            "boundary_state": boundary_state,
        }
    )
