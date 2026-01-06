from datetime import datetime

from sapianta_chat.models import ChatRequest, ChatResponse


class ChatOrchestrator:
    def handle(self, request: ChatRequest) -> ChatResponse:
        handler = self._select_handler(request.interaction_type)
        response_text, response_type = handler(request)

        return ChatResponse(
            response_text=response_text,
            response_type=response_type,
            metadata={
                "handled_at": datetime.utcnow().isoformat(),
                "orchestrator": self.__class__.__name__,
                "interaction_type": request.interaction_type
            }
        )

    def _select_handler(self, interaction_type: str):
        return {
            "informational": self._handle_informational,
            "explanatory": self._handle_explanatory,
            "structural": self._handle_structural,
            "boundary": self._handle_boundary,
            "unknown": self._handle_unknown,
        }.get(interaction_type, self._handle_unknown)

    def _handle_informational(self, request: ChatRequest):
        return (
            "Podan je informativni odgovor na zastavljeno vprašanje.",
            "informational"
        )

    def _handle_explanatory(self, request: ChatRequest):
        return (
            "Podana je razlaga zahtevanega koncepta ali delovanja.",
            "explanatory"
        )

    def _handle_structural(self, request: ChatRequest):
        return (
            "Podan je strukturni opis zahtevanega dela sistema.",
            "structural"
        )

    def _handle_boundary(self, request: ChatRequest):
        return (
            "Podan je odgovor glede zmožnosti ali omejitev sistema.",
            "boundary"
        )

    def _handle_unknown(self, request: ChatRequest):
        return (
            "Zahteve ni bilo mogoče zanesljivo razvrstiti.",
            "unknown"
        )
