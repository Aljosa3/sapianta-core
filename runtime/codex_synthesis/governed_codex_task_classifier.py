"""Static deterministic classifier for bounded Codex task synthesis."""

from __future__ import annotations

SUPPORTED_TASKS = {
    "GOVERNANCE_ARTIFACT_TASK": ("governance artifact", "create governance artifact"),
    "VALIDATION_TASK": ("runtime validation", "validate runtime"),
    "TEST_GENERATION_TASK": ("generate test", "test generation"),
    "FINALIZE_TASK": ("finalize", "prepare finalize milestone"),
}

BLOCKED_MARKERS = (
    "shell",
    "orchestrate",
    "continue automatically",
    "recursive",
    "retry",
    "execute codex",
    "run codex",
    "unrestricted filesystem",
    "subprocess",
    "network",
    "ignore previous",
    "prompt injection",
    "do anything",
)


def classify_governed_codex_task(natural_language: str) -> dict:
    normalized = " ".join(natural_language.lower().split())
    blocked = [marker for marker in BLOCKED_MARKERS if marker in normalized]
    if blocked:
        return {"valid": False, "task_class": None, "reason": "prohibited task marker", "markers": blocked}
    matches = [
        task_class
        for task_class, phrases in SUPPORTED_TASKS.items()
        if any(phrase in normalized for phrase in phrases)
    ]
    if len(matches) != 1:
        return {"valid": False, "task_class": None, "reason": "ambiguous or unsupported task", "matches": matches}
    return {"valid": True, "task_class": matches[0], "reason": "deterministic match", "matches": matches}
