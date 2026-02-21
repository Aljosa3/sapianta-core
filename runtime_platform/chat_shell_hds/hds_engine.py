from typing import List
from .models import OptionProposal
from .llm_stub import DummyLLM


class HDSEngine:
    """
    HUMAN DECISION SUPPORT
    - strukturira razumevanje
    - nikoli ne odloča
    """

    def __init__(self, llm: DummyLLM):
        self.llm = llm

    def analyze(self, question: str) -> List[OptionProposal]:
        return self.llm.generate(question)
