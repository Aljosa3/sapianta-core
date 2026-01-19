"""
CHAT RESPONSE SEMANTICS

This module defines the finite set of response types that
SAPIANTA Chat is allowed to return.

Rules:
- Every chat response MUST declare its type
- Types are semantic, not stylistic
- No response type implies execution
- New types require explicit addition here
"""

from enum import Enum
from typing import Any, Dict


class ResponseType(str, Enum):
    """
    Allowed response categories for SAPIANTA Chat.
    """

    # Informational state (read-only snapshot)
    STATE = "state"

    # Explanation of a decision, rule, or constraint
    EXPLANATION = "explanation"

    # Simulation of a potential action (no execution)
    SIMULATION = "simulation"

    # Explicit rejection with reason
    REJECTION = "rejection"

    # Neutral informational message
    INFO = "info"


def make_response(
    response_type: ResponseType,
    content: Any,
    meta: Dict[str, Any] | None = None,
) -> Dict[str, Any]:
    """
    Create a structured chat response.

    This function performs no validation of content semantics.
    It only enforces response structure.
    """
    return {
        "type": response_type.value,
        "content": content,
        "meta": meta or {},
    }
