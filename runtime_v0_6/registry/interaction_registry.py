"""
Interaction Registry — Runtime v0.6 (PASSIVE)

Design reference:
- INTERACTION_REGISTRY_SPEC.md (v0.5)

This module defines a passive registry container only.
No execution, no mutation logic, no dispatch.
"""

from typing import Dict, Any

InteractionRegistry: Dict[str, Any] = {}
