"""
Sapianta — Controlled Core Invocation Gate

Status: LIMITED
Phase: 3
Purpose: Declare an explicit execution gate for Core invocation.

This module decides ONLY whether invocation is permitted.
It does not call the Core.
It does not interpret requests or responses.
"""

from enum import Enum


class InvocationPermission(Enum):
    """
    Possible invocation permissions.
    """
    ALLOWED = "ALLOWED"
    DENIED = "DENIED"


class InvocationGate:
    """
    Declarative execution gate.

    This gate must be consulted before any Core invocation.
    It contains no side effects and no invocation logic.
    """

    def __init__(self, system_state: str, instance_state: str):
        self.system_state = system_state
        self.instance_state = instance_state

    def check(self) -> InvocationPermission:
        """
        Determine whether Core invocation is permitted.

        Rules (Phase 3):
        - Invocation is allowed ONLY if both states are explicitly LIMITED.
        - Any other state results in DENIED.
        """

        if self.system_state == "LIMITED" and self.instance_state == "LIMITED":
            return InvocationPermission.ALLOWED

        return InvocationPermission.DENIED
