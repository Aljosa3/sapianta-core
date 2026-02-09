"""
Runtime IntentEcho
Non-semantic · Deterministic · Read-only · EXT-1 Runtime

This module returns the input string exactly as received.
No interpretation. No transformation. No side effects.
"""


def intent_echo(raw_text: str) -> str:
    """
    Deterministically returns the input string as output.

    Invariants:
    - output length equals input length
    - character sequence unchanged
    - whitespace and newlines unchanged

    Prohibitions:
    - no normalization
    - no logging
    - no state access
    - no WRITE-GATE interaction
    """

    # Fail-safe: if input is None, treat as empty string deterministically
    if raw_text is None:
        return ""

    return raw_text
