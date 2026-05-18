"""Replay-visible evidence for read-only execution observability."""

from __future__ import annotations


def governed_execution_observability_evidence(*, request: dict, trace: dict, timeline: list[dict]) -> dict:
    return {
        "handoff_package": request["handoff_package"],
        "authority_token": request["authority_token"],
        "consumer_receipt": request["consumer_response"]["receipt"],
        "adapter_receipt": request["adapter_response"]["receipt"],
        "execution_trace": trace,
        "execution_timeline": timeline,
        "blocked_capability_guarantees": trace["blocked_capabilities"],
        "stdout_hash": trace["stdout_hash"],
        "stderr_hash": trace["stderr_hash"],
        "read_only": True,
        "deterministic_closure": trace["deterministic_closure_status"],
    }
