"""
STRICT READ-ONLY ADAPTER

This adapter MAY:
- read lifecycle metadata
- read audit/artifact references
- perform read-only intent structuring (CSIP view)
- perform read-only build preparation (ROBP view)
- perform read-only build plan freeze preview (HCBPF view)

This adapter MUST NOT:
- write
- execute
- mutate state
"""

def get_current_lifecycle():
    """
    Read-only lookup of current lifecycle context.

    Returns:
        dict | None
        Example (future):
        {
            "lifecycle_id": "LC-2026-0001",
            "status": "INITIALIZED",
            "created_at": "2026-02-08T10:15:00Z"
        }
    """
    # STUB (LOCK-safe): no lifecycle present
    return None


def csip_from_raw_text(raw_text: str) -> dict:
    """
    Read-only CSIP transformation.

    This function:
    - does NOT persist anything
    - does NOT change lifecycle state
    - only returns a structured intent VIEW
    """
    cleaned = raw_text.strip()

    return {
        "protocol": "CSIP",
        "version": "v1",
        "raw_input": cleaned,
        "intent": {
            "summary": cleaned[:120],
            "confidence": "UNVERIFIED",
            "scope": "HUMAN_SUBMITTED",
        },
        "constraints": {
            "write": False,
            "execute": False,
            "persist": False,
        },
    }


def robp_from_csip(csip: dict) -> dict:
    """
    Read-only Build Preparation derived from CSIP.

    Informational preview only:
    - no build generation
    - no persistence
    - no execution
    """
    summary = csip.get("intent", {}).get("summary", "").lower()

    module_type = "GENERIC"
    if "analiza" in summary or "analysis" in summary:
        module_type = "ANALYSIS"

    return {
        "protocol": "ROBP",
        "version": "v1",
        "derived_from": "CSIP",
        "module_type": module_type,
        "write_required": False,
        "execution_required": False,
        "notes": "Preview only. No build will be generated.",
    }


def hcbpf_from_robp(robp: dict) -> dict:
    """
    Read-only Human-Confirmed Build Plan Freeze (HCBPF preview).

    Informational only:
    - shows what would be frozen
    - no persistence
    - no artifact binding
    - no execution
    """
    return {
        "protocol": "HCBPF",
        "version": "v1",
        "status": "FROZEN (preview)",
        "plan": {
            "module_type": robp.get("module_type"),
            "write_required": False,
            "execution_required": False,
        },
        "constraints": {
            "immutable": True,
            "single_shot_write": "NOT PERFORMED",
        },
        "notes": "Preview only. No artifact binding has occurred.",
    }
