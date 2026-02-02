import os

from sapianta_chat.execution.claude_adapter import ClaudeAdapter


def get_execution_backend():
    """
    Select execution backend.

    Defaults to 'claude'.
    This module performs selection only.
    Adapters remain configuration-agnostic.
    """

    backend = os.getenv("EXECUTION_BACKEND", "claude")

    if backend == "claude":
        from runtime.claude_client import ClaudeClient  # runtime wiring only
        client = ClaudeClient.from_env()
        return ClaudeAdapter(client)

    raise RuntimeError(f"Unknown EXECUTION_BACKEND: {backend}")
