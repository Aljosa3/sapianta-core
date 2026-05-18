"""Deterministic temporary execution authority tokens."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

EXECUTION_WINDOW_SECONDS = 300
BOUNDARY_STATEMENT = "Execution authorization is bounded eligibility, not execution itself."


def _parse(timestamp: str) -> datetime:
    return datetime.fromisoformat(timestamp.replace("Z", "+00:00")).astimezone(timezone.utc)


def create_execution_authority_token(*, request: dict) -> dict:
    approved_at = _parse(request["approval_timestamp"])
    expires_at = approved_at + timedelta(seconds=EXECUTION_WINDOW_SECONDS)
    seed = {
        "handoff_package_sha256": request["handoff_package_sha256"],
        "approved_task_class": request["handoff_package"]["task_class"],
        "approval_timestamp": request["approval_timestamp"],
        "authorization_expiration": expires_at.isoformat().replace("+00:00", "Z"),
    }
    replay_identity = stable_hash(seed)
    return {
        "token_id": f"EXEC-AUTH-{replay_identity[:24]}",
        "replay_identity": replay_identity,
        "approved_task_class": request["handoff_package"]["task_class"],
        "governance_mode": request["handoff_package"]["governance_mode"],
        "approval_timestamp": request["approval_timestamp"],
        "authorization_expiration": expires_at.isoformat().replace("+00:00", "Z"),
        "downstream_execution_authority": True,
        "blocked_capabilities": request["handoff_package"]["blocked_capabilities"],
        "execution_window_seconds": EXECUTION_WINDOW_SECONDS,
        "revocation_supported": True,
        "constitutional_boundary_statement": BOUNDARY_STATEMENT,
        "handoff_package_sha256": request["handoff_package_sha256"],
    }
