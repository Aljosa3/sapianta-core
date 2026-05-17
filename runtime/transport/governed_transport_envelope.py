"""Deterministic governed live transport envelope."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def create_governed_transport_envelope(
    *,
    request: dict,
    activation_binding: dict,
    operation_evidence: dict,
    surface_evidence: dict,
) -> dict:
    value = {
        "governed_transport_request_id": request["governed_transport_request_id"],
        "runtime_activation_gate_id": activation_binding["runtime_activation_gate_id"],
        "runtime_operation_envelope_id": operation_evidence["runtime_operation_envelope_id"],
        "runtime_execution_surface_id": surface_evidence["runtime_execution_surface_id"],
        "replay_identity": request["replay_identity"],
    }
    return {
        **value,
        "governed_transport_envelope_id": f"GOVERNED-TRANSPORT-ENVELOPE-{stable_hash(value)[:24]}",
        "envelope_sha256": stable_hash(value),
        "synchronous": True,
        "retry_present": False,
        "fallback_present": False,
    }
