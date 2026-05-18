"""Concise read-only governed execution summaries."""

from __future__ import annotations


def summarize_execution_trace(*, trace: dict) -> dict:
    return {
        "authority_status": trace["authorization_status"],
        "receipt_status": {
            "consumer": trace["consumer_receipt_status"],
            "adapter": trace["adapter_receipt_status"],
        },
        "replay_identity": trace["replay_identity"],
        "stdout_hash": trace["stdout_hash"],
        "stderr_hash": trace["stderr_hash"],
        "blocked_capabilities": trace["blocked_capabilities"],
        "execution_performed": trace["execution_performed"],
    }
