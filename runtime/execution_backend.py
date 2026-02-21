from typing import Protocol, Any


class ExecutionBackend(Protocol):
    """
    Constitutional execution backend interface.

    Core defines only the contract.
    Platform layer provides concrete implementation.
    """

    def execute(self, payload: Any) -> Any:
        ...