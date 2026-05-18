"""Deterministic execution authority revocation."""

from __future__ import annotations

from .governed_execution_receipt import create_execution_receipt


def revoke_execution_authority(*, token: dict, approval_chain: list[dict], revoked_at: str) -> dict:
    receipt = create_execution_receipt(token=token, authority_status="REVOKED", approval_chain=approval_chain)
    return {
        "status": "REVOKED",
        "token_id": token.get("token_id", ""),
        "revoked_at": revoked_at,
        "future_execution_valid": False,
        "receipt": receipt,
    }
