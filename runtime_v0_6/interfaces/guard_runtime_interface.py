"""
Guard ↔ Runtime Interface — v0.6 (DECLARATIVE)

Design reference:
- GUARD_RUNTIME_INTERFACE_SPEC.md (v0.5)

This file declares interface expectations only.
No callable execution paths are permitted.
"""

from typing import Protocol, Any


class GuardRuntimeInterface(Protocol):
    def authorize(self, context: Any) -> Any:
        ...
