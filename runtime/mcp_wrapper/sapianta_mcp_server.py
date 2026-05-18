"""MCP-ready tool registry surface.

The optional MCP transport package is not bundled in this repository. This
module intentionally exposes only the contract and local handler needed for a
host-side MCP registration step.
"""

from __future__ import annotations

from .sapianta_mcp_tool import SAPIANTA_GOVERNED_INVOKE_TOOL, handle_sapianta_governed_invoke


def list_tools() -> list[dict]:
    return [SAPIANTA_GOVERNED_INVOKE_TOOL]


def call_tool(name: str, payload: dict) -> dict:
    if name != SAPIANTA_GOVERNED_INVOKE_TOOL["name"]:
        return {"status": "BLOCKED", "errors": [{"field": "tool", "reason": "unknown tool"}]}
    return handle_sapianta_governed_invoke(payload)
