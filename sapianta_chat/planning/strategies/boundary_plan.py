from sapianta_chat.planning.strategy_base import PlanningStrategy
from sapianta_chat.planning.plan import Plan
from sapianta_chat.planning.plan_step import PlanStep
from sapianta_chat.models import ChatRequest


class BoundaryPlan(PlanningStrategy):
    def build(self, request: ChatRequest) -> Plan:
        steps = [
            PlanStep(
                title="Prepoznava omejitve",
                description="Ugotovitev, katere aktivnosti niso dovoljene."
            ),
            PlanStep(
                title="Opredelitev varnega obsega",
                description="Kaj je mogoče obravnavati zgolj konceptualno."
            ),
        ]

        return Plan(
            steps=steps,
            plan_type="boundary"
        )
