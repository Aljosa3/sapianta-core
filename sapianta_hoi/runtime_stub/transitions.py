from typing import Dict, Tuple


# Deterministic transition mapping
# (current_state, event_type) -> next_state
TRANSITIONS: Dict[Tuple[str, str], str] = {
    ("INITIAL", "START"): "RUNNING",
    ("RUNNING", "STOP"): "STOPPED",
}
