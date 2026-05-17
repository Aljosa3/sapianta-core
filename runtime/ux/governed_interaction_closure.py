"""Deterministic governed UX interaction closure."""

from __future__ import annotations

from copy import deepcopy

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

from .governed_interaction_replay import validate_interaction_replay


def close_governed_interaction_session(*, session: dict) -> dict:
    validation = validate_interaction_replay(session)
    if not validation["valid"] or session.get("closed") is True or session.get("interaction_count", 0) == 0:
        errors = list(validation["errors"])
        if session.get("closed") is True:
            errors.append({"field": "closed", "reason": "invalid interaction closure"})
        if session.get("interaction_count", 0) == 0:
            errors.append({"field": "interaction_count", "reason": "invalid interaction closure"})
        return {"session": deepcopy(session), "validation": {"valid": False, "errors": errors}, "states": ["BLOCKED"]}
    value = {
        "governed_interaction_session_id": session["governed_interaction_session_id"],
        "final_interaction_hash": session["interaction_head_hash"],
        "interaction_count": session["interaction_count"],
        "replay_identity": session["replay_identity"],
    }
    closure_hash = stable_hash(value)
    closure = {
        **value,
        "governed_interaction_closure_id": f"GOVERNED-INTERACTION-CLOSURE-{closure_hash[:24]}",
        "closure_sha256": closure_hash,
        "replay_safe": True,
    }
    closed_session = deepcopy(session)
    closed_session["closed"] = True
    closed_session["closure_id"] = closure["governed_interaction_closure_id"]
    return {"session": closed_session, "closure": closure, "validation": {"valid": True, "errors": []}, "states": ["INTERACTION_CLOSED"]}
