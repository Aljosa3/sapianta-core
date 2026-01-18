"""
Trace Event definition for SAPIANTA — TRACE_EXTENSION_1.

A TraceEvent is a structured record of something that happened.
It carries no meaning, severity, or interpretation.
"""

from dataclasses import dataclass
from typing import Dict, Any


@dataclass(frozen=True)
class TraceEvent:
    name: str
    metadata: Dict[str, Any] = None
