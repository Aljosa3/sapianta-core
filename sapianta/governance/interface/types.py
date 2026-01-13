from dataclasses import dataclass
from sapianta.core.types import ChatResponse


@dataclass(frozen=True)
class GovernanceRequest:
    """
    Normativno prazen transportni objekt.
    """
    request_type: str
    raw_input: str


@dataclass(frozen=True)
class GovernanceResponse:
    """
    1:1 projekcija Core ChatResponse.
    """
    core_response: ChatResponse
