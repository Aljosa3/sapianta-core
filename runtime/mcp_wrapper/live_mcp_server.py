"""Live MCP host entrypoint for the single governed runtime tool."""

from __future__ import annotations

from typing import Any, Callable

from .sapianta_mcp_tool import handle_sapianta_governed_invoke

LIVE_MCP_SERVER_NAME = "SAPIANTA Governed Runtime"
LIVE_MCP_TRANSPORT = "streamable-http"
LIVE_MCP_CONNECTOR_PATH = "/mcp"
LIVE_MCP_DEPENDENCY = "mcp"


def load_fastmcp() -> type:
    """Load the official MCP SDK only when the live host is launched."""
    try:
        from mcp.server.fastmcp import FastMCP
    except ImportError as exc:
        raise RuntimeError("official MCP SDK package 'mcp' is required for live host registration") from exc
    return FastMCP


def build_live_mcp_server(
    *,
    fastmcp_cls: type | None = None,
    handler: Callable[[dict], dict] = handle_sapianta_governed_invoke,
) -> Any:
    """Build the one-tool live MCP server without widening runtime authority."""
    server_cls = fastmcp_cls or load_fastmcp()
    server = server_cls(LIVE_MCP_SERVER_NAME, json_response=True)

    @server.tool()
    def sapianta_governed_invoke(
        artifact: str,
        host: str = "127.0.0.1",
        port: int = 8110,
    ) -> dict:
        """Invoke the localhost governed SAPIANTA runtime through the bridge."""
        return handler({"artifact": artifact, "host": host, "port": port})

    return server


def run_live_mcp_server() -> None:
    """Launch the official SDK-backed live MCP host."""
    server = build_live_mcp_server()
    server.run(transport=LIVE_MCP_TRANSPORT)


if __name__ == "__main__":
    run_live_mcp_server()
