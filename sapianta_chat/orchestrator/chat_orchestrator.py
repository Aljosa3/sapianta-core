from datetime import datetime

from sapianta_chat.models import ChatRequest, ChatResponse
from sapianta_chat.reasoning import ReasoningStrategySelector
from sapianta_chat.planning.strategy_selector import PlanningStrategySelector


class ChatOrchestrator:
    def __init__(self):
        self.reasoning_selector = ReasoningStrategySelector()
        self.planning_selector = PlanningStrategySelector()

    def handle(self, request: ChatRequest) -> ChatResponse:
        # Reasoning (kako razložiti)
        reasoning_strategy = self.reasoning_selector.select(request)
        explanation = reasoning_strategy.explain(request)

        # Planning (kako bi bilo strukturirano – brez izvedbe)
        planning_strategy = self.planning_selector.select(request)
        plan = planning_strategy.build(request)

        response_text, response_type = self._base_response(
            request,
            explanation
        )

        return ChatResponse(
            response_text=response_text,
            response_type=response_type,
            metadata={
                "handled_at": datetime.utcnow().isoformat(),
                "orchestrator": self.__class__.__name__,
                "interaction_type": request.interaction_type,
                "reasoning_strategy": reasoning_strategy.__class__.__name__,
                "planning_strategy": planning_strategy.__class__.__name__,
                "plan": {
                    "plan_id": plan.plan_id,
                    "plan_type": plan.plan_type,
                    "steps": [
                        {
                            "step_id": step.step_id,
                            "title": step.title,
                            "description": step.description,
                            "depends_on": step.depends_on,
                            "metadata": step.metadata,
                        }
                        for step in plan.steps
                    ],
                },
            }
        )

    def _base_response(self, request: ChatRequest, explanation: str):
        if request.interaction_type == "informational":
            return explanation, "informational"

        if request.interaction_type == "explanatory":
            return explanation, "explanatory"

        if request.interaction_type == "structural":
            return explanation, "structural"

        if request.interaction_type == "boundary":
            return explanation, "boundary"

        return explanation, "unknown"
