from dataclasses import dataclass, field
from typing import Any, Dict, List
import uuid

from sapianta_chat.planning.plan_step import PlanStep


@dataclass(frozen=True)
class Plan:
    plan_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    steps: List[PlanStep] = field(default_factory=list)
    plan_type: str = "conceptual"
    metadata: Dict[str, Any] = field(default_factory=dict)
