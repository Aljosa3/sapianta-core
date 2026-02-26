import hashlib
import json
from dataclasses import dataclass
from typing import List, Dict, Any


# ===============================
# Allowed Operators (Closed Set)
# ===============================

ALLOWED_OPERATORS = {
    "<=",
    "<",
    ">=",
    ">",
    "==",
    "!=",
}


# ===============================
# Policy Constraint (DSL-based)
# ===============================

@dataclass(frozen=True)
class PolicyConstraint:
    constraint_id: str
    description: str
    severity: str  # "HARD" | "SOFT"
    field: str
    operator: str
    value: Any

    def __post_init__(self):
        if self.operator not in ALLOWED_OPERATORS:
            raise ValueError(
                f"Unsupported operator '{self.operator}'. "
                f"Allowed operators: {ALLOWED_OPERATORS}"
            )

        if self.severity not in {"HARD", "SOFT"}:
            raise ValueError(
                "Severity must be either 'HARD' or 'SOFT'"
            )

    def to_dict(self) -> Dict[str, Any]:
        """
        Deterministic representation of constraint.
        Fully serializable (no executable code).
        """
        return {
            "constraint_id": self.constraint_id,
            "description": self.description,
            "severity": self.severity,
            "field": self.field,
            "operator": self.operator,
            "value": self.value,
        }


# ===============================
# Trading Policy Object
# ===============================

@dataclass(frozen=True)
class TradingPolicyObject:
    policy_version: str
    constraints: List[PolicyConstraint]

    def to_dict(self) -> Dict[str, Any]:
        """
        Deterministic representation of policy.
        Constraints are sorted by constraint_id for stable hashing.
        """
        sorted_constraints = sorted(
            self.constraints,
            key=lambda c: c.constraint_id
        )

        return {
            "policy_version": self.policy_version,
            "constraints": [
                c.to_dict() for c in sorted_constraints
            ],
        }

    def policy_hash(self) -> str:
        """
        Deterministically hashes the policy definition.
        Policy is fully data-based.
        Constraints are sorted by constraint_id to ensure ordering stability.
        """
        serializable = self.to_dict()

        serialized = json.dumps(
            serializable,
            sort_keys=True,
            separators=(",", ":"),
        )

        return hashlib.sha256(
            serialized.encode("utf-8")
        ).hexdigest()
