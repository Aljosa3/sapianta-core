"""Deterministic ChatGPT bridge requests."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


def create_chatgpt_bridge_request(*, artifact: str, host: str, port: int) -> dict:
    value = {"artifact": artifact, "host": host, "port": port}
    replay_identity = stable_hash(value)
    return {
        **value,
        "chatgpt_bridge_request_id": f"CHATGPT-BRIDGE-REQUEST-{replay_identity[:24]}",
        "replay_identity": replay_identity,
        "tool_name": "sapianta_governed_invoke",
    }
