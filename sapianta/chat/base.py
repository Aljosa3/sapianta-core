"""
CHAT MODULE BASE CONTRACT

Defines the explicit base contract for all Chat-native modules.

Rules:
- Chat modules are non-executing by default
- Read-only behavior must be explicit
- Side effects are forbidden unless explicitly overridden
- This base class enforces intent, not permissions
"""

from abc import ABC, abstractmethod
from typing import Any, Dict

from sapianta.chat.response_types import ResponseType, make_response


class ChatModule(ABC):
    """
    Base class for all Chat-native modules.

    By default, chat modules are read-only and MUST NOT
    cause side effects or execution.
    """

    # ------------------------------------------------------------------
    # Contract flags (explicit by design)
    # ------------------------------------------------------------------

    read_only: bool = True
    allows_execution: bool = False

    # ------------------------------------------------------------------
    # Required metadata
    # ------------------------------------------------------------------

    @property
    @abstractmethod
    def capability(self) -> str:
        """
        Capability name this module implements.
        Must exist in CHAT_CAPABILITIES.
        """
        raise NotImplementedError

    # ------------------------------------------------------------------
    # Main entry point
    # ------------------------------------------------------------------

    @abstractmethod
    def handle(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle a chat request.

        This method MUST:
        - Be deterministic
        - Produce no side effects
        - Return a structured response via make_response()
        """
        raise NotImplementedError

    # ------------------------------------------------------------------
    # Safety helpers
    # ------------------------------------------------------------------

    def reject_execution(self, reason: str) -> Dict[str, Any]:
        """
        Standardized rejection response for execution attempts.
        """
        return make_response(
            ResponseType.REJECTION,
            content={
                "reason": reason,
                "read_only": self.read_only,
                "allows_execution": self.allows_execution,
            },
        )
