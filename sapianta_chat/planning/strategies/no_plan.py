from sapianta_chat.planning.strategy_base import PlanningStrategy
from sapianta_chat.planning.plan import Plan
from sapianta_chat.models import ChatRequest


class NoPlan(PlanningStrategy):
    def build(self, request: ChatRequest) -> Plan:
        return Plan(
            steps=[],
            plan_type="none"
        )
