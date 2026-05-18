"""Deterministic receipts for bounded Codex execution."""

from __future__ import annotations

import hashlib

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

CONSTITUTIONAL_STATEMENT = "Bounded Codex execution remains governance-controlled and does not constitute autonomous execution."


def create_codex_execution_receipt(
    *,
    authority_token: dict,
    execution_status: str,
    validation: dict,
    dispatch: dict,
) -> dict:
    stdout_hash = hashlib.sha256(dispatch.get("stdout", "").encode("utf-8")).hexdigest()
    stderr_hash = hashlib.sha256(dispatch.get("stderr", "").encode("utf-8")).hexdigest()
    value = {
        "authority_token_id": authority_token.get("token_id", ""),
        "execution_status": execution_status,
        "stdout_hash": stdout_hash,
        "stderr_hash": stderr_hash,
        "metadata": dispatch.get("metadata", {}),
    }
    replay_identity = stable_hash(value)
    return {
        "receipt_id": f"CODEX-EXECUTION-RECEIPT-{replay_identity[:24]}",
        "replay_identity": replay_identity,
        "authority_token_id": authority_token.get("token_id", ""),
        "execution_status": execution_status,
        "stdout_hash": stdout_hash,
        "stderr_hash": stderr_hash,
        "bounded_execution_metadata": dispatch.get("metadata", {}),
        "closure": {"state": execution_status, "deterministic": True},
        "blocked_capability_guarantees": authority_token.get("blocked_capabilities", []),
        "constitutional_statement": CONSTITUTIONAL_STATEMENT,
        "validation_outcome": validation,
    }
