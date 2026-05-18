"""Static deterministic classifier for the initial intent vocabulary."""

from __future__ import annotations

SUPPORTED_INTENTS = {
    "GOVERNANCE_ARTIFACT_CREATION": ("create governance artifact", "governance artifact"),
    "RUNTIME_VALIDATION_REQUEST": ("validate runtime", "runtime validation"),
    "REPLAY_INSPECTION_REQUEST": ("inspect replay", "replay inspection"),
}

BLOCKED_MARKERS = (
    "shell",
    "codex",
    "execute code",
    "run command",
    "subtask",
    "orchestrate",
    "continue automatically",
    "ignore previous",
    "prompt injection",
)


def classify_governed_intent(natural_language: str) -> dict:
    normalized = " ".join(natural_language.lower().split())
    blocked = [marker for marker in BLOCKED_MARKERS if marker in normalized]
    if blocked:
        return {"valid": False, "intent_class": None, "reason": "prohibited intent marker", "markers": blocked}
    matches = [
        intent_class
        for intent_class, phrases in SUPPORTED_INTENTS.items()
        if any(phrase in normalized for phrase in phrases)
    ]
    if len(matches) != 1:
        return {
            "valid": False,
            "intent_class": None,
            "reason": "ambiguous or unsupported intent",
            "matches": matches,
        }
    return {"valid": True, "intent_class": matches[0], "reason": "deterministic match", "matches": matches}
