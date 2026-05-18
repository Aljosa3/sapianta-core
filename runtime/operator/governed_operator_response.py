"""Concise deterministic governed operator response summaries."""


def summarize_operator_response(response: dict) -> dict:
    return {
        "status": response["status"],
        "closure": response["closure"],
        "replay_identity": response["invocation_replay_identity"],
        "request_id": response["preview_runtime_request_id"],
        "response_id": response["preview_runtime_response_id"],
        "evidence": {
            "localhost_only": response["evidence"]["localhost_only"],
            "response_returned": response["evidence"]["response_returned"],
            "replay_safe": response["evidence"]["replay_safe"],
        },
    }
