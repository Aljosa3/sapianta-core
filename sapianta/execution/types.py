from dataclasses import dataclass
from enum import Enum
from sapianta.runtime.types import RuntimeResult


class ExecutionDecision(str, Enum):
    NO_OP = "NO_OP"          # execution obstaja, a ne izvaja ničesar
    EXECUTED = "EXECUTED"    # rezervirano za kasneje


@dataclass(frozen=True)
class ExecutionResult:
    """
    Rezultat execution faze.
    """
    decision: ExecutionDecision
    runtime_result: RuntimeResult
    note: str | None = None
