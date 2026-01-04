"""
Sapianta Interaction Layer — Contracts

Status: NON-AUTHORITATIVE
Phase: 2
Purpose: Define binding rules for the Interaction Layer.

This module defines what the Interaction Layer MAY and MUST NOT do.
It contains no logic and must never influence Core decisions.
"""

from enum import Enum


class InteractionCapability(Enum):
    """
    Capabilities explicitly allowed for the Interaction Layer.
    """

    ACCEPT_HUMAN_INPUT = "ACCEPT_HUMAN_INPUT"
    ASSIST_REQUEST_FORMULATION = "ASSIST_REQUEST_FORMULATION"
    MAINTAIN_LOCAL_CONTEXT = "MAINTAIN_LOCAL_CONTEXT"
    PRESENT_CORE_OUTPUT = "PRESENT_CORE_OUTPUT"
    PRESENT_EXPLANATION = "PRESENT_EXPLANATION"
    PROVIDE_NON_DECISIONAL_GUIDANCE = "PROVIDE_NON_DECISIONAL_GUIDANCE"


class ForbiddenInteraction(Enum):
    """
    Explicitly forbidden behaviors for the Interaction Layer.
    """

    DECIDE_ACCEPTABILITY = "DECIDE_ACCEPTABILITY"
    SIMULATE_CORE_DECISION = "SIMULATE_CORE_DECISION"
    OVERRIDE_CORE_OUTPUT = "OVERRIDE_CORE_OUTPUT"
    MODIFY_CORE_MEANING = "MODIFY_CORE_MEANING"
    EXECUTE_ACTIONS = "EXECUTE_ACTIONS"
    LEARN_FROM_DECISIONS = "LEARN_FROM_DECISIONS"
    INFER_AUTHORITY = "INFER_AUTHORITY"
    PREDICT_OUTCOMES = "PREDICT_OUTCOMES"


class InteractionContract:
    """
    Declarative contract for Interaction Layer behavior.

    This class is non-executable.
    It exists to document constraints, not to enforce them at runtime.
    """

    ALLOWED = set(item for item in InteractionCapability)
    FORBIDDEN = set(item for item in ForbiddenInteraction)
