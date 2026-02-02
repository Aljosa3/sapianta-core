from abc import ABC, abstractmethod


class ExecutionAdapter(ABC):
    """
    Execution-only adapter.

    Responsibilities:
    - receive a locked build plan
    - execute exactly one LLM call
    - return raw output as string

    Forbidden:
    - validation
    - retries
    - plan interpretation
    - file I/O
    """

    @abstractmethod
    def execute(self, build_plan: dict) -> str:
        """
        Execute a single LLM call based on the provided build plan.

        :param build_plan: SAPIANTA_BUILD_PLAN_V1 (already validated upstream)
        :return: raw LLM output (string, unmodified)
        """
        raise NotImplementedError
