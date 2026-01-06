from abc import ABC, abstractmethod
from sapianta_chat.models import ChatRequest


class ReasoningStrategy(ABC):
    @abstractmethod
    def explain(self, request: ChatRequest) -> str:
        pass
