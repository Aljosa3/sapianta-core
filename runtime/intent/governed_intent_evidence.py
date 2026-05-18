"""Replay-visible evidence for bounded interpretation outcomes."""

from __future__ import annotations


def governed_intent_evidence(*, request: dict, response: dict) -> dict:
    return {
        "governed_intent_request_id": request.get("governed_intent_request_id", ""),
        "original_natural_language": request.get("natural_language", ""),
        "status": response.get("status", ""),
        "intent_class": response.get("intent_class"),
        "governance_mode": response.get("governance_mode"),
        "artifact_candidate": response.get("artifact_candidate"),
        "replay_identity": response.get("replay_identity", ""),
        "replay_visible": True,
        "requires_confirmation": response.get("requires_confirmation") is True,
        "allowed_to_execute_automatically": False,
        "closure": response.get("closure", ""),
    }
