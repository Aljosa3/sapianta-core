"""Governed execution session state evidence."""


def session_state_evidence(*, session: dict, valid: bool) -> dict:
    return {
        "governed_execution_session_id": session.get("governed_execution_session_id", ""),
        "exchange_count": session.get("exchange_count", 0),
        "session_head_hash": session.get("session_head_hash", ""),
        "closed": session.get("closed", False),
        "replay_identity": session.get("replay_identity", ""),
        "continuity_valid": valid,
        "hidden_state_present": False,
        "hidden_memory_present": False,
        "autonomous_continuation_present": False,
        "replay_safe": valid,
    }
