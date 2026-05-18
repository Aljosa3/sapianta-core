"""Replay-visible governed operator CLI evidence."""


def governed_operator_evidence(*, request: dict, summary: dict | None = None) -> dict:
    return {
        "preview_runtime_request_id": request.get("preview_runtime_request_id", ""),
        "replay_identity": request.get("replay_identity", ""),
        "summary_response_id": (summary or {}).get("response_id", ""),
        "localhost_only": True,
        "replay_safe": True,
        "retry_present": False,
        "fallback_present": False,
        "orchestration_present": False,
        "provider_routing_present": False,
    }
