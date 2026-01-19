"""
Decision data structure.

Represents a normative system decision.
"""

class Decision:
    def __init__(
        self,
        decision_id: str,
        outcome: str,
        authority: str,
        basis: list,
        binding: bool = False
    ):
        self.decision_id = decision_id
        self.outcome = outcome          # ALLOW | DENY | HOLD
        self.authority = authority
        self.basis = basis
        self.binding = binding
