from sapianta_chat.reasoning.strategy_base import ReasoningStrategy
from sapianta_chat.models import ChatRequest


class AmbiguityExplanation(ReasoningStrategy):
    def explain(self, request: ChatRequest) -> str:
        return (
            "Vprašanje je dvoumno ali nepopolno.\n"
            "Potrebna bi bila dodatna pojasnitev."
        )
