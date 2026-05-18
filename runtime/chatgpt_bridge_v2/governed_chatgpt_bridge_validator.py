"""Fail-closed validation for conversational bridge requests."""

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

BLOCKED_MARKERS = (
    "orchestrate",
    "plan recursively",
    "recursive planning",
    "continue automatically",
    "autonomous",
    "execute automatically",
    "issue authority",
    "approve automatically",
    "run codex",
    "execute codex",
    "dispatch codex",
    "hidden continuation",
)


def validate_chatgpt_bridge_request(request: dict) -> dict:
    errors = []
    if not isinstance(request, dict):
        return {"valid": False, "errors": [{"field": "request", "reason": "malformed bridge payload"}]}
    value = request.get("conversational_input")
    if not isinstance(value, str) or not value.strip():
        errors.append({"field": "conversational_input", "reason": "must be non-empty"})
    if isinstance(value, str) and len(value) > 240:
        errors.append({"field": "conversational_input", "reason": "must remain bounded"})
    expected_replay = stable_hash({"conversational_input": request.get("conversational_input")})
    if request.get("replay_identity") != expected_replay:
        errors.append({"field": "replay_identity", "reason": "replay mismatch"})
    normalized = " ".join(value.lower().split()) if isinstance(value, str) else ""
    for marker in BLOCKED_MARKERS:
        if marker in normalized:
            errors.append({"field": "conversational_input", "reason": f"prohibited conversational marker {marker}"})
    return {"valid": not errors, "errors": errors}
