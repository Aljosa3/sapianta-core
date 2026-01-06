from sapianta_chat.models import ChatRequest
from sapianta_chat.reasoning.strategies.plain import PlainExplanation
from sapianta_chat.reasoning.strategies.step_by_step import StepByStepExplanation
from sapianta_chat.reasoning.strategies.boundary import BoundaryExplanation
from sapianta_chat.reasoning.strategies.ambiguity import AmbiguityExplanation


class ReasoningStrategySelector:
    def select(self, request: ChatRequest):
        if request.interaction_type == "boundary":
            return BoundaryExplanation()

        if request.interaction_type == "unknown":
            return AmbiguityExplanation()

        if "kako" in request.normalized_input.lower():
            return StepByStepExplanation()

        return PlainExplanation()
