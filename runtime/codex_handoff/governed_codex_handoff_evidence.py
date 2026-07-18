"""Replay-visible evidence for governed Codex handoff packaging."""

from __future__ import annotations


def governed_codex_handoff_evidence(*, request: dict, package: dict, validation: dict) -> dict:
    return {
        "governed_codex_handoff_request_id": request.get("governed_codex_handoff_request_id", ""),
        "original_human_request": request.get("original_human_request", ""),
        "synthesized_prompt": package.get("codex_prompt"),
        "bounded_prompt_sha256": package.get("bounded_prompt_sha256"),
        "worker_execution_contract": package.get("worker_execution_contract"),
        "handoff_package": package,
        "replay_identity": package.get("replay_identity", ""),
        "blocked_capability_guarantees": package.get("blocked_capabilities", []),
        "requires_confirmation": package.get("requires_confirmation") is True,
        "downstream_execution_authority": package.get("downstream_execution_authority") is False,
        "export_identity": package.get("export_identity", ""),
        "closure": package.get("closure", {}),
        "validation": validation,
    }
