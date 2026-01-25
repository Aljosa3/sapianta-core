"""
RuntimeContext — v0.6 (IMMUTABLE / PASSIVE)

Design references:
- Runtime Architecture Overview v0.5
- Execution Context definition
- Guard Lifecycle Execution Boundary

This object is a pure data container.
It contains NO behavior, NO logic, NO execution capability.
"""

from dataclasses import dataclass
from typing import Optional, Any


@dataclass(frozen=True)
class RuntimeContext:
    """
    Immutable runtime context snapshot.

    This object may be:
    - constructed
    - passed
    - inspected

    It MUST NOT:
    - mutate
    - execute
    - decide
    - invoke Guard or Runtime logic
    """

    origin: str
    phase: str
    intent_id: Optional[str] = None
    metadata: Optional[Any] = None
