from typing import Dict, Tuple, Set


# ------------------------------------------------------------
# Governance Mode C — Explicit State Registry
# ------------------------------------------------------------
# ALL_STATES predstavlja kanonični in popolnoma deklariran
# state space Layer 0 (Kernel).
# Nobeno stanje ne sme obstajati implicitno.
# ------------------------------------------------------------

ALL_STATES: Set[str] = {
    "INITIAL",
    "RUNNING",
    "STOPPED",
}

# Optional but recommended for explicit governance clarity
INITIAL_STATE: str = "INITIAL"


# ------------------------------------------------------------
# Deterministic transition mapping
# (current_state, event_type) -> next_state
# ------------------------------------------------------------
TRANSITIONS: Dict[Tuple[str, str], str] = {
    ("INITIAL", "START"): "RUNNING",
    ("RUNNING", "STOP"): "STOPPED",
}
