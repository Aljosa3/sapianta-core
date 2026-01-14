from abc import ABC, abstractmethod
from .types import RuntimeTraceRecord


class RuntimeTraceSink(ABC):
    """
    Read-only trace sink interface.
    """

    @abstractmethod
    def emit(self, record: RuntimeTraceRecord) -> None:
        pass
