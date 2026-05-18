"""Single MCP-ready governed runtime tool."""

from __future__ import annotations

from typing import Callable

from sapianta_system.runtime.chatgpt_bridge import invoke_from_chatgpt_bridge

from .sapianta_mcp_response import blocked_mcp_response
from .sapianta_mcp_validator import validate_mcp_tool_input, validate_mcp_tool_output

SAPIANTA_GOVERNED_INVOKE_TOOL = {
    "name": "sapianta_governed_invoke",
    "description": "Invoke the localhost governed SAPIANTA runtime through the existing governed bridge.",
    "input_schema": {
        "type": "object",
        "properties": {
            "artifact": {"type": "string"},
            "host": {"type": "string", "default": "127.0.0.1"},
            "port": {"type": "integer", "default": 8110},
        },
        "required": ["artifact"],
        "additionalProperties": False,
    },
    "output_schema": {
        "type": "object",
        "properties": {
            "status": {"type": "string"},
            "closure": {"type": "string"},
            "request_id": {"type": "string"},
            "response_id": {"type": "string"},
            "replay_identity": {"type": "string"},
            "evidence": {"type": "object"},
        },
        "required": ["status", "closure", "request_id", "response_id", "replay_identity", "evidence"],
        "additionalProperties": False,
    },
}


def handle_sapianta_governed_invoke(
    payload: dict,
    *,
    bridge: Callable[..., dict] = invoke_from_chatgpt_bridge,
) -> dict:
    input_validation = validate_mcp_tool_input(payload)
    if not input_validation["valid"]:
        return blocked_mcp_response(input_validation["errors"])
    response = bridge(
        payload["artifact"],
        host=payload.get("host", "127.0.0.1"),
        port=payload.get("port", 8110),
    )
    output_validation = validate_mcp_tool_output(response)
    if not output_validation["valid"]:
        return blocked_mcp_response(output_validation["errors"])
    return {
        "status": response["status"],
        "closure": response["closure"],
        "request_id": response["request_id"],
        "response_id": response["response_id"],
        "replay_identity": response["replay_identity"],
        "evidence": response["evidence"],
    }
