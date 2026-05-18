"""Deterministic localhost preview runtime lifecycle."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

from .governed_preview_runtime_request import LOCALHOST_HOST


def start_preview_lifecycle(*, host: str, port: int) -> dict:
    value = {"host": host, "port": port, "scope": "LOCALHOST_ONLY"}
    lifecycle_hash = stable_hash(value)
    return {
        **value,
        "preview_runtime_lifecycle_id": f"PREVIEW-RUNTIME-LIFECYCLE-{lifecycle_hash[:24]}",
        "lifecycle_sha256": lifecycle_hash,
        "state": "STARTED" if host == LOCALHOST_HOST else "BLOCKED",
    }


def close_preview_lifecycle(*, lifecycle: dict, response: dict | None = None) -> dict:
    value = {
        "preview_runtime_lifecycle_id": lifecycle["preview_runtime_lifecycle_id"],
        "final_response_id": (response or {}).get("preview_runtime_response_id", ""),
        "state": lifecycle["state"],
    }
    closure_hash = stable_hash(value)
    return {
        **value,
        "preview_runtime_closure_id": f"PREVIEW-RUNTIME-CLOSURE-{closure_hash[:24]}",
        "closure_sha256": closure_hash,
        "closure": "PASS" if lifecycle["state"] == "STARTED" and response else "BLOCKED",
    }
