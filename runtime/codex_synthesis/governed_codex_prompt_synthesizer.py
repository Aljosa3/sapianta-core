"""Deterministic prompt synthesis for bounded downstream Codex previews."""

from __future__ import annotations

GOAL_BY_TASK = {
    "GOVERNANCE_ARTIFACT_TASK": "Create a bounded governance artifact proposal.",
    "VALIDATION_TASK": "Prepare a bounded runtime validation task.",
    "TEST_GENERATION_TASK": "Prepare bounded test-generation work.",
    "FINALIZE_TASK": "Prepare a bounded finalization milestone.",
}


def synthesize_codex_prompt(*, task_class: str, natural_language: str) -> str:
    goal = GOAL_BY_TASK[task_class]
    return "\n".join(
        [
            "GOAL:",
            goal,
            "",
            "CURRENT CONTEXT:",
            "Use the finalized operational-governed-interaction-runtime-v1 baseline.",
            f"Original governed request: {natural_language}",
            "",
            "ALLOWED SCOPE:",
            "Preview-only downstream Codex task formation within explicitly governed bounds.",
            "",
            "PROHIBITED ACTIONS:",
            "No autonomous execution, orchestration, hidden continuation, shell access, retries, fallback routing, unrestricted filesystem access, unrestricted subprocesses, networking, or authority expansion.",
            "",
            "VALIDATION REQUIREMENTS:",
            "Preserve deterministic, fail-closed, replay-visible semantics and do not bypass existing governance.",
            "",
            "REPLAY REQUIREMENTS:",
            "Keep task synthesis reviewable and replay-visible before any downstream handoff.",
            "",
            "TEST REQUIREMENTS:",
            "Add or update only bounded tests appropriate to the approved task scope.",
            "",
            "ACCEPTANCE CRITERIA:",
            "Task remains bounded, non-executing at synthesis time, and explicitly approved before any handoff.",
            "",
            "FINAL RESPONSE REQUIREMENTS:",
            "Return the files touched, validation performed, limitations, and confirmation that prohibited capabilities were not introduced.",
        ]
    )
