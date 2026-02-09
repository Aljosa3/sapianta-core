"""
Runtime IntentEcho+Meta (EXT-2)
Non-semantic · Deterministic · Read-only

- Echo: returns the input string exactly as received.
- Meta: reports strictly non-semantic, technical properties of the string.
- No side effects, no logging, no state access, no WRITE-GATE interaction.
"""

import hashlib
from typing import Dict, Any


def intent_echo_meta(raw_text: str) -> Dict[str, Any]:
    """
    Returns a structured output with:
      - 'echo': bitwise-identical input string
      - 'meta': strictly non-semantic technical properties

    Invariants:
      - echo equals input (no normalization, no transformation)
      - meta fields are deterministic and content-agnostic
    """

    # Deterministic fail-safe: treat None as empty string
    if raw_text is None:
        raw_text = ""

    # Echo (EXT-1)
    echo = raw_text

    # Meta (EXT-2) — strictly technical properties
    meta = {
        "char_count": len(raw_text),
        "contains_letters": any(ch.isalpha() for ch in raw_text),
        "contains_digits": any(ch.isdigit() for ch in raw_text),
        "contains_whitespace": any(ch.isspace() for ch in raw_text),
        # Deterministic, non-reversible technical hash
        "hash": hashlib.sha256(raw_text.encode("utf-8")).hexdigest(),
    }

    return {
        "echo": echo,
        "meta": meta,
    }
