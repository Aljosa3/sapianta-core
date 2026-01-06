from datetime import datetime
from typing import Optional

from sapianta_chat.models import ChatRequest


class ChatRouter:
    def route(self, raw_input: str) -> ChatRequest:
        normalized = self._normalize(raw_input)
        interaction_type = self._classify(normalized)

        return ChatRequest(
            original_input=raw_input,
            normalized_input=normalized,
            interaction_type=interaction_type,
            metadata={
                "routed_at": datetime.utcnow().isoformat(),
                "router": self.__class__.__name__
            }
        )

    def _normalize(self, text: str) -> str:
        return text.strip()

    def _classify(self, text: str) -> str:
        lowered = text.lower()

        if not lowered:
            return "unknown"

        if lowered.endswith("?"):
            if any(word in lowered for word in ["ali lahko", "ali sme", "ali je dovoljeno"]):
                return "boundary"
            return "explanatory"

        if any(word in lowered for word in ["kako je sestavljen", "struktura", "arhitektura"]):
            return "structural"

        if any(word in lowered for word in ["kaj je", "razloži", "pojasni"]):
            return "informational"

        return "unknown"
