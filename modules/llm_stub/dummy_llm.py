"""
Dummy LLM stub for Sapianta Chat experiments.

Properties:
- No external calls
- No memory
- Deterministic-ish (template based)
- Non-authoritative (never claims policy authority)
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Any


@dataclass
class LLMReply:
    text: str
    meta: Dict[str, Any]


class DummyLLM:
    def __init__(self, model_name: str = "dummy-llm-v0"):
        self.model_name = model_name

    def respond(self, user_input: str, context: Dict[str, Any] | None = None) -> LLMReply:
        context = context or {}
        now = datetime.utcnow().isoformat()

        # Simple deterministic templates (no sentiment, no inference)
        if any(x in user_input.lower() for x in ["ne razumem", "kaj sistem", "kaj se dogaja"]):
            text = (
                "Razumem. Najprej povzemam stanje:\n"
                "- Ti sprašuješ za razlago namena / stanja.\n"
                "- Sistem ti lahko poda orientacijski povzetek (brez sprememb in brez odločanja).\n\n"
                "Predlagam: povej mi, ali želiš razlago 'kaj je HOI', 'kaj je kernel', ali 'kaj pomeni signal'."
            )
        elif any(x in user_input.lower() for x in ["ne vem, kaj lahko naredim", "kaj lahko naredim", "ne morem"]):
            text = (
                "Če razumeš stanje, a ne veš kako ukrepati, imamo dve varni poti:\n"
                "1) zahtevaj seznam možnih naslednjih korakov (read-only)\n"
                "2) aktiviraj PAUSE, če nadaljevanje brez jasnega ukrepa ni legitimno\n\n"
                "Povej: želiš (1) seznam korakov ali (2) pavzo?"
            )
        else:
            text = (
                "Sprejeto. Lahko nadaljujemo na dva načina:\n"
                "- nadaljuješ z vprašanjem (read-only razlaga)\n"
                "- sprožiš HOI način (ORIENT/PAUSE/REDIRECT)\n\n"
                "Kaj izbereš?"
            )

        return LLMReply(
            text=text,
            meta={
                "model": self.model_name,
                "timestamp_utc": now,
                "non_authoritative": True,
            },
        )
