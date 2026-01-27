from typing import List
from .models import OptionProposal
from .llm_stub import DummyLLM


class HDSEngine:
    """
    HDS v0.2
    - omogoča razlago na zahtevo
    - brez odločanja
    """

    def __init__(self, llm: DummyLLM):
        self.llm = llm

    def explain(self, option: OptionProposal, mode: str) -> str:
        return self.llm.generate_explanation(option, mode)
