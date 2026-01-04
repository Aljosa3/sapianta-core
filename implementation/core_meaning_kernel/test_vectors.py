"""
Sapianta Core — Meaning Kernel Test Vectors

Status: LIMITED IMPLEMENTATION
Phase: 1
Purpose: Define static, non-executable test vectors.

This module defines example inputs and their expected outputs.
It does NOT execute tests.
It does NOT invoke the Core.
It serves as a specification artifact only.
"""

from .types import (
    AbstractRequest,
    ChatResponse,
    DecisionStatus,
    DecisionReason,
)

# ---------------------------------------------------------------------
# Test Vector 1: Minimal abstract request
# ---------------------------------------------------------------------

REQUEST_MINIMAL = AbstractRequest(
    request_id="REQ-0001",
    payload=None,
)

EXPECTED_RESPONSE_MINIMAL = ChatResponse(
    status=DecisionStatus.REJECTED,
    reason=DecisionReason.NOT_IMPLEMENTED,
    core_version="v1.0",
    invariant_marker="SAPIANTA_CORE_CANON_v1.0",
)

# ---------------------------------------------------------------------
# Test Vector 2: Abstract request with opaque payload
# ---------------------------------------------------------------------

REQUEST_WITH_PAYLOAD = AbstractRequest(
    request_id="REQ-0002",
    payload={
        "opaque": True,
        "content": "This payload has no semantic meaning in Phase 1.",
    },
)

EXPECTED_RESPONSE_WITH_PAYLOAD = ChatResponse(
    status=DecisionStatus.REJECTED,
    reason=DecisionReason.NOT_IMPLEMENTED,
    core_version="v1.0",
    invariant_marker="SAPIANTA_CORE_CANON_v1.0",
)

# ---------------------------------------------------------------------
# Notes
# ---------------------------------------------------------------------
#
# - All expected responses are identical by design.
# - Payload content does not influence outcomes.
# - These vectors demonstrate determinism and Canon compliance.
#
# Execution of these vectors is explicitly forbidden in Phase 1.
