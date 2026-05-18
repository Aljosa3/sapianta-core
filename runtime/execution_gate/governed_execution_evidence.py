"""Replay-visible evidence for downstream execution authorization."""

from __future__ import annotations


def governed_execution_authorization_evidence(
    *,
    request: dict,
    token: dict,
    approval_chain: list[dict],
    receipt: dict,
    revocation_events: list[dict] | None = None,
) -> dict:
    package = request["handoff_package"]
    return {
        "original_human_request": package["evidence"]["original_human_request"],
        "synthesized_prompt": package["codex_prompt"],
        "handoff_package": package,
        "authorization_token": token,
        "approval_chain": approval_chain,
        "authority_expiration": token["authorization_expiration"],
        "revocation_events": revocation_events or [],
        "execution_receipts": [receipt],
        "blocked_capability_guarantees": token["blocked_capabilities"],
        "constitutional_boundary_evidence": token["constitutional_boundary_statement"],
    }
