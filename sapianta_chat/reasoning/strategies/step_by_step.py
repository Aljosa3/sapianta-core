from sapianta_chat.reasoning.strategy_base import ReasoningStrategy
from sapianta_chat.models import ChatRequest


class StepByStepExplanation(ReasoningStrategy):
    def explain(self, request: ChatRequest) -> str:
        return (
            "Razlaga poteka po korakih:\n"
            "1. Ugotovitev namena vprašanja\n"
            "2. Razčlenitev koncepta\n"
            "3. Zaključek brez izvedbe"
        )
