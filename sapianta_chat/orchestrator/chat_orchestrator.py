from datetime import datetime

from sapianta_chat.models import ChatRequest, ChatResponse
from sapianta_chat.reasoning import ReasoningStrategySelector


class ChatOrchestrator:
    def __init__(self):
        self.reasoning_selector = ReasoningStrategySelector()

    def handle(self, request: ChatRequest) -> ChatResponse:
        strategy = self.reasoning_selector.select(request)
        explanation = strategy.explain(request)

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
                "reasoning_strategy": strategy.__class__.__name__,
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
