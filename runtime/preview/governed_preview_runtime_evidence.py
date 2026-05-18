"""Replay-visible localhost preview runtime evidence."""


def governed_preview_runtime_evidence(*, request: dict, response: dict | None, lifecycle: dict, closure: dict) -> dict:
    return {
        "preview_runtime_request_id": request.get("preview_runtime_request_id", ""),
        "preview_runtime_response_id": (response or {}).get("preview_runtime_response_id", ""),
        "preview_runtime_lifecycle_id": lifecycle.get("preview_runtime_lifecycle_id", ""),
        "preview_runtime_closure_id": closure.get("preview_runtime_closure_id", ""),
        "localhost_only": lifecycle.get("host") == "127.0.0.1",
        "replay_identity": request.get("replay_identity", ""),
        "replay_safe": True,
        "response_returned": (response or {}).get("status") == "RETURNED",
        "orchestration_present": False,
        "hidden_continuation_present": False,
        "hidden_execution_present": False,
        "hidden_mutable_state_present": False,
    }
