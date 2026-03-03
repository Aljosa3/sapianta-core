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

    def serializable_definition(self) -> Dict[str, Any]:
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
# Credit Policy Object
# ===============================

@dataclass(frozen=True)
class CreditPolicyObject:
    policy_version: str
    constraints: List[PolicyConstraint]

    def policy_hash(self) -> str:
        """
        Deterministically hashes the policy definition.
        Policy is now fully data-based.
        """
        serializable = {
            "policy_version": self.policy_version,
            "constraints": [
                c.serializable_definition()
                for c in self.constraints
            ],
        }

        serialized = json.dumps(
            serializable,
            sort_keys=True,
            separators=(",", ":"),
        )

        return hashlib.sha256(
            serialized.encode("utf-8")
        ).hexdigest()