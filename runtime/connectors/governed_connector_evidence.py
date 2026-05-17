"""Replay-visible governed execution connector evidence."""


def governed_connector_evidence(*, registration: dict, envelope: dict, result: dict, valid: bool) -> dict:
    return {
        "connector_id": registration.get("connector_id", ""),
        "connector_name": registration.get("connector_name", ""),
        "connector_envelope_id": envelope.get("connector_envelope_id", ""),
        "connector_result_id": result.get("connector_result_id", ""),
        "governed_transport_request_id": envelope.get("governed_transport_request_id", ""),
        "runtime_surface": envelope.get("runtime_surface", ""),
        "replay_identity": envelope.get("replay_identity", ""),
        "connector_completed": valid,
        "lineage_preserved": valid,
        "replay_safe": valid,
        "orchestration_present": False,
        "retry_present": False,
        "fallback_present": False,
        "provider_routing_present": False,
        "hidden_execution_present": False,
    }
