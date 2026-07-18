"""Replay-visible evidence for bounded Codex task synthesis."""

from __future__ import annotations


def governed_codex_synthesis_evidence(*, request: dict, response: dict) -> dict:
    return {
        "governed_codex_task_request_id": request.get("governed_codex_task_request_id", ""),
        "original_human_input": request.get("natural_language", ""),
        "task_class": response.get("task_class"),
        "governance_mode": response.get("governance_mode"),
        "codex_prompt_preview": response.get("codex_prompt_preview"),
        "bounded_prompt_sha256": response.get("bounded_prompt_sha256"),
        "worker_execution_contract": response.get("worker_execution_contract"),
        "replay_identity": response.get("replay_identity", ""),
        "blocked_capability_checks": response.get("blocked_capability_checks", []),
        "validator_outcomes": response.get("validation", {}),
        "requires_confirmation": response.get("requires_confirmation") is True,
        "allowed_to_execute_automatically": False,
        "closure": response.get("closure", ""),
    }
