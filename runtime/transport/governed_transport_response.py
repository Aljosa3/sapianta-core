"""Deterministic governed live transport response."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def create_governed_transport_response(*, request: dict, envelope: dict, surface_evidence: dict) -> dict:
    value = {
        "governed_transport_request_id": request["governed_transport_request_id"],
        "governed_transport_envelope_id": envelope["governed_transport_envelope_id"],
        "runtime_execution_surface_id": surface_evidence["runtime_execution_surface_id"],
        "request_replay_identity": request["replay_identity"],
        "result_payload": {
            "delivery_status": "DELIVERED",
            "runtime_surface": surface_evidence["runtime_surface"],
            "bounded_result": True,
        },
    }
    result_identity = stable_hash(value)
    return {
        **value,
        "governed_transport_result_id": f"GOVERNED-TRANSPORT-RESULT-{result_identity[:24]}",
        "result_replay_identity": result_identity,
        "response_returned": True,
    }
