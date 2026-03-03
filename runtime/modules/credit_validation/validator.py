import hashlib
import json
from typing import Dict, Any

from .policy import CreditPolicyObject


# ===============================
# Engine Version
# ===============================

ENGINE_VERSION = "credit_validation_engine_v1.1_dsl"


# ===============================
# Exceptions
# ===============================

class StructuralValidationError(Exception):
    pass


# ===============================
# Deterministic Hash Utility
# ===============================

def deterministic_hash(obj: Any) -> str:
    """
    Deterministically serializes and hashes an object.
    """
    serialized = json.dumps(
        obj,
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(
        serialized.encode("utf-8")
    ).hexdigest()


# ===============================
# Structural Validation
# ===============================

REQUIRED_FIELDS = {
    "decision_id": str,
    "timestamp": str,
    "policy_version": str,
    "currency": str,
    "client_id": str,
    "rating": str,
    "sector_code": str,
    "requested_exposure": (int, float),
    "tenor_months": int,
    "collateral_value": (int, float),
    "collateral_type": str,
    "collateral_coverage_ratio": (int, float),
    "current_client_exposure": (int, float),
    "current_group_exposure": (int, float),
    "current_sector_exposure": (int, float),
    "total_portfolio_exposure": (int, float),
}


def structural_validate(decision: Dict[str, Any]) -> None:
    """
    Validates required fields and types.
    Raises StructuralValidationError if invalid.
    """
    for field, expected_type in REQUIRED_FIELDS.items():
        if field not in decision:
            raise StructuralValidationError(
                f"Missing required field: {field}"
            )

        if not isinstance(decision[field], expected_type):
            raise StructuralValidationError(
                f"Invalid type for field '{field}'. "
                f"Expected {expected_type}, got {type(decision[field])}"
            )

    if decision["requested_exposure"] <= 0:
        raise StructuralValidationError(
            "requested_exposure must be positive"
        )

    if decision["total_portfolio_exposure"] <= 0:
        raise StructuralValidationError(
            "total_portfolio_exposure must be > 0"
        )


# ===============================
# DSL Constraint Evaluator
# ===============================

def evaluate_constraint(
    decision: Dict[str, Any],
    constraint,
) -> bool:
    """
    Evaluates a DSL-based constraint.
    No executable code allowed.
    """

    if constraint.field not in decision:
        raise StructuralValidationError(
            f"Decision missing field '{constraint.field}'"
        )

    left = decision[constraint.field]
    right = constraint.value

    if constraint.operator == "<=":
        return left <= right
    if constraint.operator == "<":
        return left < right
    if constraint.operator == ">=":
        return left >= right
    if constraint.operator == ">":
        return left > right
    if constraint.operator == "==":
        return left == right
    if constraint.operator == "!=":
        return left != right

    raise ValueError(
        f"Unsupported operator: {constraint.operator}"
    )


# ===============================
# Validation Engine
# ===============================

def validate_decision(
    decision: Dict[str, Any],
    policy: CreditPolicyObject,
) -> Dict[str, Any]:

    decision_hash = deterministic_hash(decision)
    policy_hash = policy.policy_hash()

    # 1️⃣ Structural validation
    try:
        structural_validate(decision)
        structural_valid = True
    except StructuralValidationError as e:
        return {
            "decision_valid": False,
            "structural_valid": False,
            "error": str(e),
            "failed_constraints": [],
            "decision_hash": decision_hash,
            "policy_hash": policy_hash,
            "policy_version": policy.policy_version,
            "engine_version": ENGINE_VERSION,
        }

    # 2️⃣ DSL Constraint evaluation (no short-circuit)
    failed_constraints = []

    for constraint in policy.constraints:
        result = evaluate_constraint(decision, constraint)

        if not result:
            failed_constraints.append({
                "constraint_id": constraint.constraint_id,
                "description": constraint.description,
                "severity": constraint.severity,
            })

    # HARD constraint failure invalidates decision
    decision_valid = all(
        c["severity"] != "HARD"
        for c in failed_constraints
    )

    return {
        "decision_valid": decision_valid,
        "structural_valid": structural_valid,
        "failed_constraints": failed_constraints,
        "decision_hash": decision_hash,
        "policy_hash": policy_hash,
        "policy_version": policy.policy_version,
        "engine_version": ENGINE_VERSION,
    }