from typing import List
from .models import OptionProposal


class DummyLLM:
    """
    LLM STUB
    - brez avtoritete
    - brez optimalnosti
    - brez odločanja
    """

    def generate(self, question: str) -> List[OptionProposal]:
        return [
            OptionProposal(
                title="Možnost A (po mnenju sistema najbolj smiselna)",
                rationale="Na podlagi splošne logike in omejenih informacij se zdi razumna.",
                consequences=[
                    "Lahko prinese stabilen izid.",
                    "Obstaja tveganje napačne presoje."
                ],
                uncertainty="Ocena temelji na omejenem kontekstu in je lahko nepopolna."
            ),
            OptionProposal(
                title="Možnost B (alternativa)",
                rationale="Manj očitna možnost, a z drugačnim profilom tveganja.",
                consequences=[
                    "Lahko omogoči več fleksibilnosti.",
                    "Povečana negotovost."
                ],
                uncertainty="Manj podatkov za zanesljivo presojo."
            )
        ]
