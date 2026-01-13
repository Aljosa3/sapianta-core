from dataclasses import dataclass
from enum import Enum
from sapianta.core.types import ChatResponse


class ROINormativeLevel(str, Enum):
    COMMUNITY = "COMMUNITY"
    ORGANIZATIONAL = "ORG"


@dataclass(frozen=True)
class ROIContext:
    """
    Določa, kateri normativni okvirji so aktivni.
    """
    active_community_frameworks: list[str]
    active_org_policies: list[str]


@dataclass(frozen=True)
class ROIResult:
    """
    ROI ne spreminja Core odločitve.
    Lahko pa omeji nadaljnjo izvedbo.
    """
    allowed: bool
    reason: str | None = None
    originating_layer: ROINormativeLevel | None = None
