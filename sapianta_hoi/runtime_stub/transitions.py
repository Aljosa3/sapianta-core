from typing import Dict, Tuple, Set


# ------------------------------------------------------------
# Governance Mode B — Explicit & Controlled Recovery Kernel
# ------------------------------------------------------------
# ALL_STATES predstavlja kanonični in popolnoma deklariran
# state space Layer 0 (Kernel).
# Nobeno stanje ne sme obstajati implicitno.
# ------------------------------------------------------------

ALL_STATES: Set[str] = {
    "INITIAL",
    "RUNNING",
    "STOPPED",
    "ERROR",
}

# Explicit kernel entry state
INITIAL_STATE: str = "INITIAL"


# ------------------------------------------------------------
# Deterministic transition mapping
# (current_state, event_type) -> next_state
#
# Model B:
# - STOPPED = normalen, čist zaključek
# - ERROR   = obravnavana napaka
# - Recovery cikel je edini dovoljen cikel:
#       RUNNING -> ERROR -> RUNNING
# ------------------------------------------------------------

TRANSITIONS: Dict[Tuple[str, str], str] = {

    # Startup
    ("INITIAL", "START"): "RUNNING",

    # Normal lifecycle
    ("RUNNING", "STOP"): "STOPPED",

    # Failure path
    ("RUNNING", "FAIL"): "ERROR",

    # Recovery path (allowed cycle)
    ("ERROR", "RECOVER"): "RUNNING",

    # Abort path (graceful shutdown after error)
    ("ERROR", "ABORT"): "STOPPED",
}
