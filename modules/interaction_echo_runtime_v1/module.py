"""
Minimal runtime implementation for interaction_echo_runtime_v1.

This module implements a pure echo:
input -> output (unchanged).
"""


def handle_interaction(payload):
    """
    Echo handler.

    Args:
        payload: opaque input value

    Returns:
        The exact same payload, unchanged.
    """
    return payload
