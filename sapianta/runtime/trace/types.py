from dataclasses import dataclass
from sapianta.runtime.types import RuntimeDecision


@dataclass(frozen=True)
class RuntimeTraceRecord:
    """
    Read-only observability record.
    Contains no content and no executable intent.
    """
    decision: RuntimeDecision
    reason: str | None
    source: str
