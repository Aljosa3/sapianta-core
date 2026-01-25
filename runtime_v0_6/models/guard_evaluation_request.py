"""
GuardEvaluationRequest — v0.6 (DECLARATIVE BRIDGE)

Design references:
- Guard ↔ Runtime Interface SPEC v0.5
- Guard Lifecycle Protocol
- Execution Boundary definition

This object represents a request FOR evaluation,
not an evaluation itself.

It does NOT:
- invoke Guard
- authorize execution
- trigger decisions
"""

from dataclasses import dataclass
from runtime_v0_6.models.runtime_context import RuntimeContext
from runtime_v0_6.models.execution_request import ExecutionRequestEnvelope


@dataclass(frozen=True)
class GuardEvaluationRequest:
    """
    Declarative request for Guard evaluation.

    This object:
    - binds runtime context
    - binds execution request
    - contains no behavior

    It MUST NOT:
    - call Guard
    - decide
    - mutate
    """

    context: RuntimeContext
    execution_request: ExecutionRequestEnvelope
