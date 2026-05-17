"""Deterministic request envelopes for live runtime wiring."""

from __future__ import annotations

from copy import deepcopy

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

GOVERNED_RUNTIME_ENDPOINT_ID = "LOCAL-GOVERNED-RUNTIME-ENDPOINT-V1"


def create_runtime_request_envelope(*, invocation_session: dict, interaction_payload: dict) -> dict:
    value = {
        "runtime_invocation_session_id": invocation_session["runtime_invocation_session_id"],
        "invocation_index": invocation_session["invocation_count"] + 1,
        "previous_invocation_hash": invocation_session["invocation_head_hash"],
        "governed_runtime_endpoint_id": GOVERNED_RUNTIME_ENDPOINT_ID,
        "interaction_payload": deepcopy(interaction_payload),
    }
    request_hash = stable_hash(value)
    return {
        **value,
        "runtime_invocation_request_id": f"RUNTIME-INVOCATION-REQUEST-{request_hash[:24]}",
        "request_hash": request_hash,
    }
