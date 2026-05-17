"""Deterministic governed UX response records."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def create_governed_interaction_response(*, request: dict, transport_output: dict, connector_output: dict) -> dict:
    value = {
        "governed_interaction_request_id": request["governed_interaction_request_id"],
        "governed_transport_request_id": transport_output["request"]["governed_transport_request_id"],
        "connector_result_id": connector_output["result"]["connector_result_id"],
        "transport_replay_identity": transport_output["request"]["replay_identity"],
        "connector_replay_identity": connector_output["result"]["replay_identity"],
        "operational_evidence": {
            "transport_completed": transport_output["evidence"]["transport_completed"],
            "connector_completed": connector_output["evidence"]["connector_completed"],
            "lineage_preserved": (
                transport_output["evidence"]["lineage_preserved"]
                and connector_output["evidence"]["lineage_preserved"]
            ),
        },
    }
    response_hash = stable_hash(value)
    return {
        **value,
        "governed_interaction_response_id": f"GOVERNED-INTERACTION-RESPONSE-{response_hash[:24]}",
        "response_hash": response_hash,
        "response_status": "RETURNED",
    }
