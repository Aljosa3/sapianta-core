"""
Sapianta — Controlled Core Invocation (Single Use)

Status: LIMITED
Phase: 3
Purpose: Perform a single, explicit Core invocation under strict gating.

This module:
- checks the execution gate,
- performs exactly one Core invocation if permitted,
- does not loop, retry, or automate,
- does not interpret or act upon the result.

Execution of this module is a deliberate human action.
"""

from invocation.controlled.gate import InvocationGate, InvocationPermission
from implementation.core_meaning_kernel.kernel import evaluate_request
from implementation.core_meaning_kernel.types import AbstractRequest


def invoke_once() -> None:
    """
    Perform a single Core invocation if explicitly permitted.

    Phase 3 rules:
    - Invocation is allowed only when both states are LIMITED.
    - Exactly one invocation is performed.
    - No result interpretation or side effects occur.
    """

    # -----------------------------------------------------------------
    # Explicit system and instance states (Phase 3)
    # -----------------------------------------------------------------
    system_state = "LIMITED"
    instance_state = "LIMITED"

    gate = InvocationGate(
        system_state=system_state,
        instance_state=instance_state,
    )

    permission = gate.check()

    if permission is not InvocationPermission.ALLOWED:
        raise RuntimeError("Core invocation denied by execution gate.")

    # -----------------------------------------------------------------
    # Single, explicit invocation
    # -----------------------------------------------------------------
    request = AbstractRequest(
        request_id="PHASE3-TEST-0001",
        payload={"note": "Controlled single invocation in Phase 3"},
    )

    response = evaluate_request(request)

    # -----------------------------------------------------------------
    # Result handling (non-interpreting)
    # -----------------------------------------------------------------
    # The response is deliberately not processed further.
    # This confirms the invocation path without enabling behavior.
    _ = response


if __name__ == "__main__":
    # Explicit execution entry point.
    invoke_once()
