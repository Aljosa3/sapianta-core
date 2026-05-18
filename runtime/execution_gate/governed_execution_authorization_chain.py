"""Deterministic approval chain construction."""

from __future__ import annotations


def build_approval_chain(*, request: dict, token: dict) -> list[dict]:
    return [
        {
            "step": "HANDOFF_PACKAGE_VALIDATED",
            "handoff_package_replay_identity": request["handoff_package"]["replay_identity"],
            "handoff_package_sha256": request["handoff_package_sha256"],
        },
        {
            "step": "EXPLICIT_HUMAN_APPROVAL",
            "approved_by": request["approved_by"],
            "approval_timestamp": request["approval_timestamp"],
        },
        {
            "step": "TEMPORARY_AUTHORITY_TOKEN_ISSUED",
            "token_id": token["token_id"],
            "authorization_expiration": token["authorization_expiration"],
        },
    ]
