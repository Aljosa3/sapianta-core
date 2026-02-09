from enum import Enum
from typing import Optional


class Phase(Enum):
    DESIGN = "DESIGN"
    SPEC = "SPEC"
    BUILD = "BUILD"
    VALIDATE = "VALIDATE"
    CONFIRM = "CONFIRM"


# Allowed CPSP signals (exact match, at start of input)
_PHASE_SIGNAL_MAP = {
    "PHASE: DESIGN": Phase.DESIGN,
    "PHASE: SPEC": Phase.SPEC,
    "PHASE: BUILD": Phase.BUILD,
    "PHASE: VALIDATE": Phase.VALIDATE,
    "PHASE: CONFIRM": Phase.CONFIRM,
}


def parse_phase_signal(raw_text: str) -> Phase:
    """
    CPSP Runtime Phase Signal Parser

    - Reads only the beginning of the input string
    - Matches exact CPSP phase signals
    - Returns Phase.DESIGN as a deterministic fallback
    - Has no side effects
    """

    if not raw_text:
        return Phase.DESIGN

    # Read only the first line, without trimming or normalization
    first_line = raw_text.splitlines()[0]

    for signal, phase in _PHASE_SIGNAL_MAP.items():
        if first_line == signal:
            return phase

    # Fail-safe default
    return Phase.DESIGN
