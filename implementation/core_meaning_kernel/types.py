"""
Sapianta Core — Meaning Kernel Types

Status: LIMITED IMPLEMENTATION
Phase: 1
Purpose: Define immutable data structures for Core communication.

This module defines data structures only.
It contains no logic, no decision-making, and no behavior.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class DecisionStatus(Enum):
    """
    Canonical decision status as produced by the Core.

    Note:
    In Phase 1, this enum is defined but not meaningfully used.
    """
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"


class DecisionReason(Enum):
    """
    Canonical reason categories.

    Note:
    In Phase 1, reasons are placeholders only.
    """
    NOT_IMPLEMENTED = "NOT_IMPLEMENTED"
    INVALID_REQUEST = "INVALID_REQUEST"
    UNSPECIFIED = "UNSPECIFIED"


@dataclass(frozen=True)
class ChatResponse:
    """
    Authoritative Core output structure.

    This structure mirrors the Canon definition.
    It is immutable and side-effect free.
    """
    status: DecisionStatus
    reason: Optional[DecisionReason]
    core_version: str
    invariant_marker: str


@dataclass(frozen=True)
class AbstractRequest:
    """
    Abstract request representation.

    This is a placeholder structure.
    It intentionally carries no semantic meaning.
    """
    request_id: str
    payload: Optional[dict] = None
