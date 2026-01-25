"""
ExecutionRequestEnvelope — v0.6 (DECLARATIVE / PASSIVE)

Design references:
- Runtime Architecture Overview v0.5
- Execution Intent Model
- Guard Lifecycle Execution Boundary

This object represents a declared execution request.
It does NOT perform execution.
It does NOT invoke Guard.
It does NOT imply authorization.
"""

from dataclasses import dataclass
from typing import Optional, Any
from runtime_v0_6.models.runtime_context import RuntimeContext


@dataclass(frozen=True)
class ExecutionRequestEnvelope:
    """
    Declarative execution request.

    This object:
    - describes intent
    - carries context
    - contains no logic

    It MUST NOT:
    - execute
    - authorize
    - mutate
    - dispatch
    """

    context: RuntimeContext
    requested_action: str
    parameters: Optional[Any] = None
