"""Deterministic receipts for the mock execution consumer."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

CONSTITUTIONAL_STATEMENT = "Mock execution authorization consumption does not constitute downstream execution."


def create_consumer_receipt(
    *,
    authority_token: dict,
    receipt_status: str,
    validation: dict,
    dispatch: dict,
) -> dict:
    value = {
        "authority_token_id": authority_token.get("token_id", ""),
        "receipt_status": receipt_status,
        "validation": validation,
        "dispatch": dispatch,
        "blocked_capabilities": authority_token.get("blocked_capabilities", []),
    }
    replay_identity = stable_hash(value)
    return {
        "receipt_id": f"EXEC-CONSUMER-RECEIPT-{replay_identity[:24]}",
        "replay_identity": replay_identity,
        "authority_token_id": authority_token.get("token_id", ""),
        "validation_outcome": validation,
        "dispatch_status": dispatch.get("dispatch_status", "MOCK_DISPATCH_REJECTED"),
        "execution_performed": False,
        "closure": {"state": receipt_status, "deterministic": True},
        "blocked_capability_guarantees": authority_token.get("blocked_capabilities", []),
        "constitutional_statement": CONSTITUTIONAL_STATEMENT,
    }
