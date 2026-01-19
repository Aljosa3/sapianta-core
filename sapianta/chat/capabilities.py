"""
CHAT CAPABILITY BOUNDARY

This module defines the explicit and finite set of capabilities
that SAPIANTA Chat is allowed to invoke against the runtime.

Rules:
- Capabilities are declarative, not executable
- Absence from this list == NOT SUPPORTED
- Capabilities do NOT imply permission, only availability
- This list is intentionally small and conservative
"""

from typing import Set


# ---------------------------------------------------------------------
# Chat-visible capabilities
# ---------------------------------------------------------------------

CHAT_CAPABILITIES: Set[str] = {
    # Read-only system introspection
    "inspect_system_state",

    # Explain why a guard decision occurred
    "explain_guard_decision",

    # Simulate (never execute) an action through ExecutionGate
    "simulate_execution",
}


def is_capability_supported(capability: str) -> bool:
    """
    Check whether a capability is officially supported by SAPIANTA Chat.

    This function performs no authorization and no execution.
    It is a pure boundary check.
    """
    return capability in CHAT_CAPABILITIES


def list_capabilities() -> Set[str]:
    """
    Return the full set of chat-supported capabilities.
    Intended for inspection and debugging only.
    """
    return set(CHAT_CAPABILITIES)
