"""Deterministic closure for live runtime wiring sessions."""

from __future__ import annotations

from copy import deepcopy

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

from .governed_runtime_invocation_replay import validate_invocation_replay


def close_runtime_invocation_session(*, session: dict) -> dict:
    validation = validate_invocation_replay(session)
    if not validation["valid"] or session.get("closed") is True or session.get("invocation_count", 0) == 0:
        errors = list(validation["errors"])
        if session.get("closed") is True:
            errors.append({"field": "closed", "reason": "invalid invocation closure"})
        if session.get("invocation_count", 0) == 0:
            errors.append({"field": "invocation_count", "reason": "invalid invocation closure"})
        return {"session": deepcopy(session), "validation": {"valid": False, "errors": errors}, "states": ["BLOCKED"]}
    value = {
        "runtime_invocation_session_id": session["runtime_invocation_session_id"],
        "final_invocation_hash": session["invocation_head_hash"],
        "invocation_count": session["invocation_count"],
        "replay_identity": session["replay_identity"],
    }
    closure_hash = stable_hash(value)
    closure = {
        **value,
        "runtime_invocation_closure_id": f"RUNTIME-INVOCATION-CLOSURE-{closure_hash[:24]}",
        "closure_sha256": closure_hash,
        "replay_safe": True,
    }
    closed_session = deepcopy(session)
    closed_session["closed"] = True
    closed_session["closure_id"] = closure["runtime_invocation_closure_id"]
    return {"session": closed_session, "closure": closure, "validation": {"valid": True, "errors": []}, "states": ["INVOCATION_CLOSED"]}
