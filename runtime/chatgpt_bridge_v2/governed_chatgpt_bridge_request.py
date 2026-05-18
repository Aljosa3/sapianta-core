"""Deterministic conversational bridge requests."""

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def create_chatgpt_bridge_request(*, conversational_input: str) -> dict:
    replay_identity = stable_hash({"conversational_input": conversational_input})
    return {
        "governed_chatgpt_bridge_request_id": f"GOV-CHATGPT-BRIDGE-V2-REQUEST-{replay_identity[:24]}",
        "conversational_input": conversational_input,
        "replay_identity": replay_identity,
        "bounded": True,
    }
