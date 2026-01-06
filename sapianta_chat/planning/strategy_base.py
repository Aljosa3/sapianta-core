from abc import ABC, abstractmethod
from sapianta_chat.models import ChatRequest
from sapianta_chat.planning.plan import Plan


class PlanningStrategy(ABC):
    @abstractmethod
    def build(self, request: ChatRequest) -> Plan:
        pass
