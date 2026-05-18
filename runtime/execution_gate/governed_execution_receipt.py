"""Deterministic execution authority receipts."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def create_execution_receipt(*, token: dict, authority_status: str, approval_chain: list[dict]) -> dict:
    value = {
        "token_id": token.get("token_id", ""),
        "authority_status": authority_status,
        "approval_chain": approval_chain,
        "blocked_capabilities": token.get("blocked_capabilities", []),
    }
    replay_identity = stable_hash(value)
    return {
        "receipt_id": f"EXEC-AUTH-RECEIPT-{replay_identity[:24]}",
        "replay_identity": replay_identity,
        "token_id": token.get("token_id", ""),
        "authority_status": authority_status,
        "approval_lineage": approval_chain,
        "blocked_capabilities": token.get("blocked_capabilities", []),
        "closure": {"state": authority_status, "deterministic": True},
    }
