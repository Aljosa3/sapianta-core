from dataclasses import dataclass
from enum import Enum
from sapianta.core.types import ChatResponse
from sapianta.governance.roi.types import ROIResult


class RuntimeDecision(str, Enum):
    HALT = "HALT"
    PROCEED = "PROCEED"


@dataclass(frozen=True)
class RuntimeResult:
    """
    Končni izhod runtime faze.
    """
    decision: RuntimeDecision
    core_response: ChatResponse
    roi_result: ROIResult | None = None
    reason: str | None = None
