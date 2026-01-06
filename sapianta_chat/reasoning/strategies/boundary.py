from sapianta_chat.reasoning.strategy_base import ReasoningStrategy
from sapianta_chat.models import ChatRequest


class BoundaryExplanation(ReasoningStrategy):
    def explain(self, request: ChatRequest) -> str:
        return (
            "Sistem pojasnjuje svoje zmožnosti in omejitve.\n"
            "Do dejanskega delovanja ali izvedbe ne pride."
        )
