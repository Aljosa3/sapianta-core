from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class PromptPayload:
    """
    Formal deterministic prompt contract.

    This object:
    - is immutable
    - contains no executable code
    - contains no dynamic behavior
    - contains only serializable fields
    """

    state_name: str
    state_snapshot: Dict[str, str]
    template_version: str

    def to_dict(self) -> Dict[str, object]:
        """
        Deterministic dictionary export.
        """
        return {
            "state_name": self.state_name,
            "state_snapshot": dict(sorted(self.state_snapshot.items())),
            "template_version": self.template_version,
        }
