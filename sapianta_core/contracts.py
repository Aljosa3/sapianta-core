# /home/pisarna/work/sapianta/sapianta_system/sapianta_core/contracts.py
"""
SAPIANTA CORE — public contracts (constitutional surface)

These are lightweight type contracts only.
They must be deterministic and platform-agnostic.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass(frozen=True, slots=True)
class EventContract:
    """
    Minimal contract for an event emitted/consumed by the core execution loop.

    This is a type-level artifact aligned with governance/contracts/CORE_PUBLIC_INTERFACE_CONTRACT_v1.0.md.
    """
    name: str
    payload: Dict[str, Any]
    # Optional metadata for audit / trace without enforcing any platform coupling
    meta: Optional[Dict[str, Any]] = None