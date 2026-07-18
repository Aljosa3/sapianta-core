"""Deterministic requests for bounded Codex execution."""

from __future__ import annotations

from copy import deepcopy
from hashlib import sha256

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def create_codex_execution_request(
    *,
    handoff_package: dict,
    authority_token: dict,
    now: str,
    revoked_token_ids: set[str] | None = None,
    codex_executable: str = "codex",
    timeout_seconds: int = 30,
) -> dict:
    package = deepcopy(handoff_package)
    token = deepcopy(authority_token)
    package_hash = stable_hash(package)
    prompt_hash = sha256(package.get("codex_prompt", "").encode("utf-8")).hexdigest()
    value = {
        "handoff_package": package,
        "handoff_package_sha256": package_hash,
        "bounded_prompt_sha256": prompt_hash,
        "authority_token": token,
        "now": now,
        "revoked_token_ids": sorted(revoked_token_ids or set()),
        "codex_executable": codex_executable,
        "timeout_seconds": timeout_seconds,
    }
    replay_identity = stable_hash(value)
    return {
        "codex_execution_request_id": f"CODEX-EXECUTION-REQUEST-{replay_identity[:24]}",
        **value,
        "replay_identity": replay_identity,
    }
