"""Concise governed ChatGPT bridge responses."""


def create_chatgpt_bridge_response(*, bridge_request: dict, operator_summary: dict) -> dict:
    return {
        "status": operator_summary["status"],
        "closure": operator_summary["closure"],
        "request_id": operator_summary["request_id"],
        "response_id": operator_summary["response_id"],
        "replay_identity": operator_summary["replay_identity"],
        "evidence": operator_summary["evidence"],
        "chatgpt_bridge_request_id": bridge_request["chatgpt_bridge_request_id"],
    }
