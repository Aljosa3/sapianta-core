"""
Sapianta Core — Meaning Kernel (Phase 1)

Status: LIMITED IMPLEMENTATION
Phase: 1
Purpose: Deterministic pipeline proof without semantic evaluation.

This module implements exactly one function.
The function is deterministic, side-effect free, and non-authoritative.
It does not interpret meaning and does not execute actions.
"""

from .types import (
    AbstractRequest,
    ChatResponse,
    DecisionStatus,
    DecisionReason,
)


CORE_VERSION = "v1.0"
INVARIANT_MARKER = "SAPIANTA_CORE_CANON_v1.0"


def evaluate_request(request: AbstractRequest) -> ChatResponse:
    """
    Evaluate an abstract request and return a canonical ChatResponse.

    Phase 1 behavior:
    - No semantic evaluation
    - No branching logic
    - No interpretation
    - Always returns REJECTED with reason NOT_IMPLEMENTED

    This function exists solely to prove that the Core pipeline
    can be implemented without violating the Canon.
    """

    return ChatResponse(
        status=DecisionStatus.REJECTED,
        reason=DecisionReason.NOT_IMPLEMENTED,
        core_version=CORE_VERSION,
        invariant_marker=INVARIANT_MARKER,
    )
