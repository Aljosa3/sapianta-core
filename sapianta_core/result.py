# /home/pisarna/work/sapianta/sapianta_system/sapianta_core/result.py
"""
SAPIANTA CORE — public result types (constitutional surface)

Deterministic data-only results returned by core control functions.
No platform coupling, no side effects.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass(frozen=True, slots=True)
class ControlResult:
    """
    Minimal control result aligned with governance/contracts/CORE_PUBLIC_INTERFACE_CONTRACT_v1.0.md.

    `ok` indicates whether validation/control succeeded.
    `errors` contains deterministic, order-stable error strings (if any).
    `data` is optional structured payload for downstream consumers.
    """
    ok: bool
    errors: tuple[str, ...] = ()
    data: Optional[Dict[str, Any]] = None