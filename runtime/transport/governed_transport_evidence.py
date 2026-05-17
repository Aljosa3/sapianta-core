"""Replay-visible evidence for governed live execution transport."""

from __future__ import annotations


def governed_transport_evidence(
    *,
    request: dict,
    envelope: dict,
    response: dict,
    valid: bool,
) -> dict:
    return {
        "governed_transport_request_id": request.get("governed_transport_request_id", ""),
        "governed_transport_envelope_id": envelope.get("governed_transport_envelope_id", ""),
        "governed_transport_result_id": response.get("governed_transport_result_id", ""),
        "replay_identity": request.get("replay_identity", ""),
        "result_replay_identity": response.get("result_replay_identity", ""),
        "transport_completed": valid,
        "transport_executed": valid,
        "lineage_preserved": valid,
        "replay_safe": valid,
        "synchronous": True,
        "retry_present": False,
        "fallback_present": False,
        "orchestration_present": False,
        "hidden_execution_present": False,
    }
