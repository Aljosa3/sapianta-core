# PATH: runtime/llm_output_guard.py

from dataclasses import dataclass
from typing import List, Literal, Optional
import re


GuardStatus = Literal["PASS", "DEGRADED", "REJECTED"]


@dataclass(frozen=True)
class GuardResult:
    status: GuardStatus
    reasons: List[str]
    text: str
    degraded: bool


# Minimalni nabor “normativnih” signalov, ki so v SAPIANTA kontekstu prepovedani.
# To je *heuristika* (string pattern), ne semantika.
_FORBIDDEN_PATTERNS = [
    r"\bpriporo(?:čam|čamo|ča)\b",
    r"\bpriporočilo\b",
    r"\bnajbolj(?:ša|ši|še)\b",
    r"\boptimaln(?:a|o|i|e)\b",
    r"\bmoraš\b",
    r"\bmorate\b",
    r"\bizberi\b",
    r"\bodloči\b",
    r"\bnaredi\b",
    r"\bnaredite\b",
    r"\bshould\b",
    r"\byou must\b",
    r"\bI recommend\b",
    r"\bbest option\b",
]

# Če LLM poskuša vrniti “odločitev” ali “score”, to šteje kot prepovedano.
_FORBIDDEN_STRUCTURAL_MARKERS = [
    "score:",
    "ranking:",
    "recommendation:",
    "decision:",
]


def guard_llm_output(
    text: str,
    *,
    max_len: int = 8000,
    reject_on_forbidden: bool = False,
) -> GuardResult:
    """
    Deterministic guard for LLM output.

    - Detects forbidden normative language patterns.
    - Optionally degrades (redacts) forbidden fragments.
    - Can REJECT if output is unsafe or too malformed.

    NOTE:
    This guard enforces form/surface constraints only.
    It does NOT interpret meaning or correctness.
    """

    reasons: List[str] = []

    if not isinstance(text, str):
        return GuardResult(
            status="REJECTED",
            reasons=["llm_output_not_string"],
            text="",
            degraded=False,
        )

    if len(text) == 0:
        return GuardResult(
            status="PASS",
            reasons=[],
            text=text,
            degraded=False,
        )

    if len(text) > max_len:
        reasons.append("llm_output_too_long")
        # deterministično skrajšamo, namesto zavrnitve
        text = text[:max_len] + "\n[TRUNCATED_BY_GUARD]"
        return GuardResult(
            status="DEGRADED",
            reasons=reasons,
            text=text,
            degraded=True,
        )

    lowered = text.lower()

    forbidden_hits: List[str] = []

    # struktura (markerji)
    for m in _FORBIDDEN_STRUCTURAL_MARKERS:
        if m in lowered:
            forbidden_hits.append(f"struct_marker:{m}")

    # jezikovni patterni
    for pat in _FORBIDDEN_PATTERNS:
        if re.search(pat, lowered):
            forbidden_hits.append(f"pattern:{pat}")

    if not forbidden_hits:
        return GuardResult(
            status="PASS",
            reasons=[],
            text=text,
            degraded=False,
        )

    reasons.extend(forbidden_hits)

    if reject_on_forbidden:
        return GuardResult(
            status="REJECTED",
            reasons=reasons,
            text="",
            degraded=False,
        )

    # DEGRADE: redakcija normativnih segmentov (minimalno invazivno)
    redacted = text
    for pat in _FORBIDDEN_PATTERNS:
        redacted = re.sub(
            pat,
            "[REDACTED_BY_GUARD]",
            redacted,
            flags=re.IGNORECASE,
        )

    for m in _FORBIDDEN_STRUCTURAL_MARKERS:
        # markerji: zamenjaj samo marker token, ne cele vrstice
        redacted = re.sub(
            re.escape(m),
            "[REDACTED_BY_GUARD]:",
            redacted,
            flags=re.IGNORECASE,
        )

    return GuardResult(
        status="DEGRADED",
        reasons=reasons,
        text=redacted,
        degraded=True,
    )
