# sapianta_chat/governance/hasbt.py
"""
HASBT — Human Authorization Step Before Transformation
PHASE: IMPLEMENTATION (MINIMAL SKELETON)

Constraints enforced:
- NO UNLOCK
- NO WRITE-GATE changes
- NO filesystem writes
- NO automatic authorization
- NO side effects
- FAIL-CLOSED only
"""

class HASBTDeny(Exception):
    """
    Deterministic, terminal denial exception.
    Must abort execution immediately.
    """
    pass


def evaluate_hasbt(payload: dict) -> None:
    """
    Evaluate HASBT payload.

    PASS:
        - returns None

    DENY:
        - raises HASBTDeny deterministically

    Allowed checks ONLY:
        - payload presence
        - payload type
        - required keys presence
        - explicit human authorization flag
    """

    # ---- Presence & type validation ----
    if payload is None:
        raise HASBTDeny("HASBT DENY: payload missing")

    if not isinstance(payload, dict):
        raise HASBTDeny("HASBT DENY: payload must be a dict")

    # ---- Required schema keys (LOCKED payload shape) ----
    required_keys = {
        "hasbt_version",
        "authorization_confirmed",
        "authorization_actor",
        "authorization_context",
    }

    missing = required_keys - payload.keys()
    if missing:
        raise HASBTDeny(f"HASBT DENY: missing required keys: {sorted(missing)}")

    # ---- Explicit human authorization confirmation ----
    if payload.get("authorization_confirmed") is not True:
        raise HASBTDeny("HASBT DENY: authorization not explicitly confirmed")

    # ---- PASS (no side effects) ----
    return None
