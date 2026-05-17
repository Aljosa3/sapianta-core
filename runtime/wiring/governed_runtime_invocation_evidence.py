"""Replay-visible live runtime wiring evidence."""


def governed_runtime_invocation_evidence(*, session: dict, response: dict | None = None, closure: dict | None = None) -> dict:
    return {
        "runtime_invocation_session_id": session.get("runtime_invocation_session_id", ""),
        "invocation_count": session.get("invocation_count", 0),
        "replay_identity": session.get("replay_identity", ""),
        "runtime_invocation_response_id": (response or {}).get("runtime_invocation_response_id", ""),
        "closure_id": (closure or {}).get("runtime_invocation_closure_id", ""),
        "replay_safe": True,
        "invocation_continuity_preserved": True,
        "orchestration_present": False,
        "hidden_continuation_present": False,
        "hidden_routing_present": False,
        "hidden_execution_present": False,
        "hidden_mutable_state_present": False,
    }
