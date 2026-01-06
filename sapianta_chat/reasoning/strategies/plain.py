from sapianta_chat.reasoning.strategy_base import ReasoningStrategy
from sapianta_chat.models import ChatRequest


class PlainExplanation(ReasoningStrategy):
    def explain(self, request: ChatRequest) -> str:
        return "Podana je jedrnata razlaga zahtevanega odgovora."
