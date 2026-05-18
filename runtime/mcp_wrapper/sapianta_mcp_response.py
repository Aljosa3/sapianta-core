"""Deterministic MCP-ready tool responses."""


def blocked_mcp_response(errors: list[dict]) -> dict:
    return {"status": "BLOCKED", "errors": errors}
