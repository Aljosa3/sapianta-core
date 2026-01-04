"""
Sapianta Interaction Layer — Interaction State

Status: NON-AUTHORITATIVE
Phase: 2
Purpose: Define local, non-decisional interaction state.

This module defines passive data structures only.
It contains no logic, no transitions, and no decision-making.
"""

from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime


@dataclass(frozen=True)
class InteractionTurn:
    """
    A single interaction turn.

    This structure records interaction metadata only.
    It carries no authority and no semantic interpretation.
    """
    timestamp: datetime
    actor: str  # e.g. "human", "system"
    content: str


@dataclass(frozen=True)
class InteractionState:
    """
    Immutable interaction state container.

    This state is local to the Interaction Layer.
    It must never influence Core behavior or decisions.
    """
    session_id: str
    turns: List[InteractionTurn] = field(default_factory=list)
    last_presented_core_response: Optional[str] = None
