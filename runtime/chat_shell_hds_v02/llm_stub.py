from .models import OptionProposal


class DummyLLM:
    """
    LLM STUB v0.2
    - generira dodatne razlage na zahtevo
    """

    def generate_explanation(self, option: OptionProposal, mode: str) -> str:
        if mode == "why":
            return f"Dodatna razlaga razloga: {option.rationale} (razširjeno, nezavezujoče)."
        if mode == "expand":
            return "Razširjene posledice so lahko bolj kompleksne in odvisne od konteksta."
        if mode == "uncertainty":
            return f"Poglobljena negotovost: {option.uncertainty}"
        return "Neznan način razlage."
