from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class OptionProposal:
    title: str
    rationale: str
    consequences: List[str]
    uncertainty: str
