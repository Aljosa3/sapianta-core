"""Replay-visible evidence for governed ChatGPT bridge calls."""


def governed_chatgpt_bridge_evidence(*, request: dict, response: dict | None = None) -> dict:
    return {
        "chatgpt_bridge_request_id": request.get("chatgpt_bridge_request_id", ""),
        "tool_name": request.get("tool_name", ""),
        "replay_identity": request.get("replay_identity", ""),
        "response_id": (response or {}).get("response_id", ""),
        "localhost_only": request.get("host") == "127.0.0.1",
        "replay_safe": True,
        "retry_present": False,
        "fallback_present": False,
        "orchestration_present": False,
        "hidden_execution_present": False,
    }
