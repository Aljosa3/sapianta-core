from sapianta_chat.planning.strategy_base import PlanningStrategy
from sapianta_chat.planning.plan import Plan
from sapianta_chat.planning.plan_step import PlanStep
from sapianta_chat.models import ChatRequest


class SimplePlan(PlanningStrategy):
    def build(self, request: ChatRequest) -> Plan:
        steps = [
            PlanStep(
                title="Razumevanje zahteve",
                description="Identifikacija namena in obsega vprašanja."
            ),
            PlanStep(
                title="Konceptualna razčlenitev",
                description="Razdelitev problema na logične sklope."
            ),
            PlanStep(
                title="Zaključek brez izvedbe",
                description="Povzetek možnega pristopa brez dejanj."
            ),
        ]

        return Plan(
            steps=steps,
            plan_type="conceptual"
        )
