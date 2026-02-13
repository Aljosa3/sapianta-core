"""
HOI Controlled Execution Layer (Phase 2.2)

Provides:

- SessionController
- EventDispatcher
- execute (formal execution entry-point)

Constraints:
- No I/O
- No logging
- No LLM
- No advisory logic
- No spec modifications

Execution Surface (v1.2.1):

The canonical execution entry-point is:

    sapianta_hoi.execution.execute

All higher layers must call execution exclusively via this function.
"""

from .session_controller import SessionController
from .event_dispatcher import EventDispatcher
from .execution_entry import execute

__all__ = [
    "SessionController",
    "EventDispatcher",
    "execute",
]
