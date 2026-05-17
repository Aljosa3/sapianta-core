"""Deterministic response envelopes for live runtime wiring."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def create_runtime_response_envelope(*, request_envelope: dict, ux_output: dict) -> dict:
    value = {
        "runtime_invocation_request_id": request_envelope["runtime_invocation_request_id"],
        "governed_interaction_request_id": ux_output["request"]["governed_interaction_request_id"],
        "governed_interaction_response_id": ux_output["response"]["governed_interaction_response_id"],
        "response_hash": ux_output["response"]["response_hash"],
        "operational_evidence": ux_output["response"]["operational_evidence"],
    }
    response_hash = stable_hash(value)
    return {
        **value,
        "runtime_invocation_response_id": f"RUNTIME-INVOCATION-RESPONSE-{response_hash[:24]}",
        "invocation_response_hash": response_hash,
        "response_status": "RETURNED",
    }
