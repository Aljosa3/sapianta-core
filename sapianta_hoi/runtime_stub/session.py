"""
HOI Runtime Session — Minimal Stub

This module provides a minimal runtime container for HOI interaction.

It intentionally contains:
- no decision logic
- no recommendations
- no learning
- no execution
- no interpretation

Its purpose is to hold the interaction loop and enforce silence.
"""

from sapianta_hoi.runtime_stub.rules import (
    FORBIDDEN_ACTS,
    FORBIDDEN_PHRASES,
    FORBIDDEN_IMPLICIT_BEHAVIORS,
)

from sapianta_hoi.runtime_stub.stop_conditions import (
    STOP_CONDITIONS,
    SILENCE_REQUIREMENTS,
)


class HOISession:
    """
    Minimal HOI runtime session.

    This session:
    - accepts user input
    - tracks whether interaction is ongoing
    - can enter a silent state
    - never moves the system forward
    """

    def __init__(self):
        self.active = True
        self.history = []
        self.silent = False

    def receive_input(self, user_input: str):
        """
        Accept user input.

        No interpretation.
        No inference.
        Input is stored as-is.
        """
        if self.silent:
            return

        self.history.append(user_input)

    def stop(self, reason: str):
        """
        Enter silent state.

        Reason must correspond to a defined STOP_CONDITION.
        """
        if reason not in STOP_CONDITIONS:
            raise ValueError(f"Invalid stop condition: {reason}")

        self.silent = True
        self.active = False

    def summary(self) -> dict:
        """
        Provide a neutral summary of the session state.

        This summary:
        - contains no decisions
        - contains no recommendations
        - does not imply closure
        """
        return {
            "inputs_received": len(self.history),
            "silent": self.silent,
            "responsibility": "human",
            "decisions_made": False,
        }
