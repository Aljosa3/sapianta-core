"""Replay-visible evidence for the mock execution consumer."""

from __future__ import annotations


def governed_execution_consumer_evidence(*, request: dict, validation: dict, receipt: dict) -> dict:
    package = request["handoff_package"]
    token = request["authority_token"]
    return {
        "original_human_request": package["evidence"]["original_human_request"],
        "synthesized_task": package["codex_prompt"],
        "handoff_package": package,
        "authority_token": token,
        "consumer_validation_results": validation,
        "mock_dispatch_receipt": receipt,
        "blocked_capability_checks": token["blocked_capabilities"],
        "deterministic_closure": receipt["closure"],
    }
