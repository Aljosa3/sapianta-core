"""Deterministic localhost preview runtime responses."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def create_preview_runtime_response(*, request: dict, invocation_output: dict, closure_output: dict) -> dict:
    value = {
        "preview_runtime_request_id": request["preview_runtime_request_id"],
        "runtime_invocation_response_id": invocation_output["response_envelope"]["runtime_invocation_response_id"],
        "invocation_replay_identity": invocation_output["invocation_session"]["replay_identity"],
        "lineage": request["lineage"],
        "evidence": invocation_output["response_envelope"]["operational_evidence"],
        "closure_id": closure_output["closure"]["runtime_invocation_closure_id"],
    }
    response_hash = stable_hash(value)
    return {
        **value,
        "preview_runtime_response_id": f"PREVIEW-RUNTIME-RESPONSE-{response_hash[:24]}",
        "response_sha256": response_hash,
        "status": "RETURNED",
        "closure": "PASS",
    }
