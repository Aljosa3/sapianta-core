from dataclasses import dataclass, field
from typing import Any, Dict, List
import uuid


@dataclass(frozen=True)
class PlanStep:
    step_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    title: str = ""
    description: str = ""
    depends_on: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
