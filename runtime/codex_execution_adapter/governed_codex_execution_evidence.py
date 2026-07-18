"""Replay-visible evidence for bounded Codex execution."""

from __future__ import annotations


def governed_codex_execution_evidence(*, request: dict, validation: dict, dispatch: dict, receipt: dict) -> dict:
    package = request["handoff_package"]
    return {
        "original_human_request": package["evidence"]["original_human_request"],
        "synthesized_task": package["codex_prompt"],
        "handoff_package": package,
        "authority_token": request["authority_token"],
        "execution_validation_results": validation,
        "bounded_execution_metadata": dispatch["metadata"],
        "transport_diagnostics": dispatch.get("diagnostics", {}),
        "stdout_hash": receipt["stdout_hash"],
        "stderr_hash": receipt["stderr_hash"],
        "bounded_prompt_sha256": receipt["bounded_prompt_sha256"],
        "execution_receipt": receipt,
        "blocked_capability_checks": request["authority_token"]["blocked_capabilities"],
        "deterministic_closure": receipt["closure"],
    }
