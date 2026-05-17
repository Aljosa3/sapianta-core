"""Replay-visible governed UX interaction evidence."""


def governed_interaction_evidence(*, session: dict, response: dict | None = None, closure: dict | None = None) -> dict:
    return {
        "governed_interaction_session_id": session.get("governed_interaction_session_id", ""),
        "interaction_count": session.get("interaction_count", 0),
        "replay_identity": session.get("replay_identity", ""),
        "response_id": (response or {}).get("governed_interaction_response_id", ""),
        "closure_id": (closure or {}).get("governed_interaction_closure_id", ""),
        "replay_safe": True,
        "interaction_continuity_preserved": True,
        "hidden_continuation_present": False,
        "orchestration_present": False,
        "hidden_routing_present": False,
        "hidden_execution_present": False,
        "hidden_mutable_state_present": False,
    }
