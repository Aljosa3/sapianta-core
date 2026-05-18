"""Replay helpers for downstream execution authorization."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def build_authorization_replay_identity(*, request: dict, token: dict, approval_chain: list[dict]) -> str:
    return stable_hash(
        {
            "execution_authorization_request_id": request["execution_authorization_request_id"],
            "token": token,
            "approval_chain": approval_chain,
        }
    )
