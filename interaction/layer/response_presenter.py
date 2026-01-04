"""
Sapianta Interaction Layer — Response Presenter

Status: NON-AUTHORITATIVE
Phase: 2
Purpose: Faithfully present ChatResponse without reinterpretation.

This module converts canonical Core outputs into human-readable form.
It must never alter meaning, infer intent, or add guidance.
"""

from implementation.core_meaning_kernel.types import ChatResponse


def present_chat_response(response: ChatResponse) -> str:
    """
    Present a ChatResponse in a neutral, declarative format.

    Rules:
    - No reinterpretation of status or reason.
    - No added guidance or suggestions.
    - No softening or escalation of language.
    - Output mirrors the structure of ChatResponse.
    """

    lines = [
        f"Decision status: {response.status.value}",
        f"Reason: {response.reason.value if response.reason else 'N/A'}",
        f"Core version: {response.core_version}",
        f"Invariant marker: {response.invariant_marker}",
    ]

    return "\n".join(lines)
