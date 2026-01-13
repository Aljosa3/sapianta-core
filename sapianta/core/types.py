from dataclasses import dataclass
from enum import Enum


class DecisionStatus(str, Enum):
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"


@dataclass(frozen=True)
class CoreRequest:
    request_type: str
    payload: str


@dataclass(frozen=True)
class ChatResponse:
    status: DecisionStatus
    reason: str | None = None
    core_marker: str = "SAPIANTA_CORE_V1"
