"""Deterministic governed execution session closure."""

from __future__ import annotations

from copy import deepcopy

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

from .governed_session_replay import validate_session_replay


def close_governed_execution_session(*, session: dict) -> dict:
    validation = validate_session_replay(session)
    if not validation["valid"] or session.get("closed") is True or session.get("exchange_count", 0) == 0:
        errors = list(validation["errors"])
        if session.get("closed") is True:
            errors.append({"field": "closed", "reason": "invalid session closure"})
        if session.get("exchange_count", 0) == 0:
            errors.append({"field": "exchange_count", "reason": "invalid session closure"})
        return {"session": deepcopy(session), "validation": {"valid": False, "errors": errors}, "states": ["BLOCKED"]}
    value = {
        "governed_execution_session_id": session["governed_execution_session_id"],
        "final_exchange_hash": session["session_head_hash"],
        "exchange_count": session["exchange_count"],
        "replay_identity": session["replay_identity"],
    }
    closure_hash = stable_hash(value)
    closure = {
        **value,
        "governed_session_closure_id": f"GOVERNED-SESSION-CLOSURE-{closure_hash[:24]}",
        "closure_sha256": closure_hash,
        "replay_safe": True,
    }
    closed_session = deepcopy(session)
    closed_session["closed"] = True
    closed_session["closure_id"] = closure["governed_session_closure_id"]
    return {
        "session": closed_session,
        "closure": closure,
        "validation": {"valid": True, "errors": []},
        "states": ["SESSION_CLOSED"],
    }
