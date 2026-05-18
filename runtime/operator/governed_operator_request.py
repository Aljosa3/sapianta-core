"""Deterministic governed operator requests."""

from __future__ import annotations

from sapianta_system.runtime.preview import create_preview_runtime_request


def _interaction_payload(*, artifact: str) -> dict:
    return {
        "interaction_intent": f"invoke artifact {artifact}",
        "connector_name": "local_execution",
        "request_payload": {
            "operation_intent": f"invoke artifact {artifact}",
            "authorized_execution": True,
        },
        "hidden_continuation_present": False,
        "orchestration_present": False,
        "hidden_routing_present": False,
        "hidden_execution_present": False,
        "hidden_mutable_state_present": False,
    }


def build_operator_request(*, artifact: str) -> dict:
    if not isinstance(artifact, str) or not artifact.strip():
        raise ValueError("artifact must be non-empty")
    lineage = {
        "governed_session_id": "OPERATOR-GOVERNED-SESSION",
        "runtime_activation_gate_id": "GATE-1",
        "runtime_operation_envelope_id": "ENV-1",
        "runtime_execution_surface_id": "SURFACE-1",
    }
    return create_preview_runtime_request(
        request_payload={
            "interaction_identity": f"OPERATOR-INTERACTION-{artifact}",
            "interaction_payload": _interaction_payload(artifact=artifact),
        },
        lineage=lineage,
    )
