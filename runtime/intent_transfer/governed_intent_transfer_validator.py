"""Fail-closed validation for governed intent transfer requests."""

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

BLOCKED_MARKERS = (
    "execute",
    "dispatch",
    "orchestrate",
    "retry",
    "fallback",
    "continue automatically",
    "issue authority",
    "run codex",
    "hidden continuation",
    "scrape page",
    "full conversation",
)

SUPPORTED_TARGETS = {
    "GOVERNED_INTERPRETATION_REQUEST",
    "GOVERNED_SYNTHESIS_REQUEST",
    "GOVERNED_OBSERVABILITY_REQUEST",
}


def validate_intent_transfer_request(request: dict) -> dict:
    errors = []
    if not isinstance(request, dict):
        return {"valid": False, "errors": [{"field": "request", "reason": "malformed transfer package"}]}
    value = request.get("conversational_input")
    if not isinstance(value, str) or not value.strip():
        errors.append({"field": "conversational_input", "reason": "must be non-empty"})
    normalized = request.get("normalized_governed_request")
    if not isinstance(normalized, dict):
        errors.append({"field": "normalized_governed_request", "reason": "malformed normalized request"})
    elif normalized.get("request_type") not in SUPPORTED_TARGETS:
        errors.append({"field": "normalized_governed_request", "reason": "malformed runtime target"})
    if not isinstance(request.get("governance_mode"), str) or not request["governance_mode"].strip():
        errors.append({"field": "governance_mode", "reason": "missing governance mode"})
    if not isinstance(request.get("bridge_replay_identity"), str) or not request["bridge_replay_identity"].strip():
        errors.append({"field": "bridge_replay_identity", "reason": "missing replay identity"})
    expected = stable_hash(
        {
            "conversational_input": request.get("conversational_input"),
            "normalized_governed_request": request.get("normalized_governed_request"),
            "governance_mode": request.get("governance_mode"),
            "bridge_replay_identity": request.get("bridge_replay_identity"),
        }
    )
    if request.get("replay_identity") != expected:
        errors.append({"field": "replay_identity", "reason": "replay mismatch"})
    flattened = " ".join(
        [
            value.lower() if isinstance(value, str) else "",
            str(normalized).lower(),
        ]
    )
    for marker in BLOCKED_MARKERS:
        if marker in flattened:
            errors.append({"field": "transfer_payload", "reason": f"prohibited transfer marker {marker}"})
    return {"valid": not errors, "errors": errors}
