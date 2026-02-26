import hashlib
import json
from typing import Dict, Any, List, Tuple, Optional

from .policy import PolicyConstraint, TradingPolicyObject


# ===============================
# Engine Version
# ===============================

ENGINE_VERSION = "trading_validation_engine_v1.0"


# ===============================
# Deterministic Hash Utility
# ===============================

def deterministic_hash(payload: Dict[str, Any]) -> str:
    """
    Deterministically serializes and hashes a payload.
    Uses sorted keys and stable separators for reproducibility.
    """
    serialized = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    )
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


# ===============================
# Required Fields Schema
# ===============================

REQUIRED_FIELDS = {
    "decision_id": str,
    "timestamp_utc": str,
    "venue": str,
    "asset": str,
    "side": str,
    "entry_price": (int, float),
    "stop_loss_price": (int, float),
    "position_size": (int, float),
    "account_balance": (int, float),
    "current_open_positions": int,
    "total_exposure": (int, float),
    "daily_pnl": (int, float),
    "leverage_ratio": (int, float),
}

ALLOWED_SIDES = {"BUY", "SELL"}

OPTIONAL_FIELDS = {"policy_hint"}


# ===============================
# Structural Validation
# ===============================

def structural_validate(envelope: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """
    Validates required fields and types according to
    TRADING_DECISION_ENVELOPE_CONTRACT_v1.0.

    Returns (structural_valid, errors).
    Errors are sorted for deterministic output.
    """
    errors = []

    # Check required fields exist
    for field, expected_type in REQUIRED_FIELDS.items():
        if field not in envelope:
            errors.append(f"Missing required field: {field}")
            continue

        # Type validation
        if not isinstance(envelope[field], expected_type):
            errors.append(
                f"Invalid type for field '{field}'. "
                f"Expected {expected_type}, got {type(envelope[field]).__name__}"
            )

    # Side enumeration validation
    if "side" in envelope and envelope["side"] not in ALLOWED_SIDES:
        errors.append(
            f"Invalid value for field 'side'. "
            f"Expected one of {ALLOWED_SIDES}, got '{envelope['side']}'"
        )

    # Domain constraint validation (numeric ranges)
    if "entry_price" in envelope and isinstance(envelope["entry_price"], (int, float)):
        if envelope["entry_price"] <= 0:
            errors.append("entry_price must be > 0")

    if "stop_loss_price" in envelope and isinstance(envelope["stop_loss_price"], (int, float)):
        if envelope["stop_loss_price"] <= 0:
            errors.append("stop_loss_price must be > 0")

    if "position_size" in envelope and isinstance(envelope["position_size"], (int, float)):
        if envelope["position_size"] <= 0:
            errors.append("position_size must be > 0")

    if "account_balance" in envelope and isinstance(envelope["account_balance"], (int, float)):
        if envelope["account_balance"] < 0:
            errors.append("account_balance must be >= 0")

    if "current_open_positions" in envelope and isinstance(envelope["current_open_positions"], int):
        if envelope["current_open_positions"] < 0:
            errors.append("current_open_positions must be >= 0")

    if "total_exposure" in envelope and isinstance(envelope["total_exposure"], (int, float)):
        if envelope["total_exposure"] < 0:
            errors.append("total_exposure must be >= 0")

    if "leverage_ratio" in envelope and isinstance(envelope["leverage_ratio"], (int, float)):
        if envelope["leverage_ratio"] < 0:
            errors.append("leverage_ratio must be >= 0")

    # Optional field validation
    if "policy_hint" in envelope:
        if not isinstance(envelope["policy_hint"], str):
            errors.append("policy_hint must be a string if present")

    # Sort errors for deterministic output
    errors.sort()

    structural_valid = len(errors) == 0
    return structural_valid, errors


# ===============================
# Constraint Evaluation
# ===============================

def evaluate_constraint(
    envelope: Dict[str, Any],
    constraint: PolicyConstraint,
) -> Tuple[bool, Optional[str]]:
    """
    Evaluates a single DSL-based constraint.
    Returns (passed, failure_reason).
    """

    # Check field exists
    if constraint.field not in envelope:
        return False, f"Missing field '{constraint.field}'"

    actual_value = envelope[constraint.field]
    expected_value = constraint.value

    # Type compatibility check for comparison
    try:
        if constraint.operator == "<=":
            passed = actual_value <= expected_value
        elif constraint.operator == "<":
            passed = actual_value < expected_value
        elif constraint.operator == ">=":
            passed = actual_value >= expected_value
        elif constraint.operator == ">":
            passed = actual_value > expected_value
        elif constraint.operator == "==":
            passed = actual_value == expected_value
        elif constraint.operator == "!=":
            passed = actual_value != expected_value
        else:
            return False, f"Unsupported operator: {constraint.operator}"

    except TypeError:
        return False, f"Type mismatch: cannot compare {type(actual_value).__name__} with {type(expected_value).__name__}"

    if passed:
        return True, None
    else:
        return False, f"Constraint failed: {actual_value} {constraint.operator} {expected_value}"


# ===============================
# Main Validation Engine
# ===============================

def validate_trading_decision(
    envelope: Dict[str, Any],
    policy: TradingPolicyObject,
) -> Dict[str, Any]:
    """
    Validates a trading decision envelope against a policy.

    Returns a deterministic validation result with:
    - structural_valid: bool
    - decision_valid: bool
    - structural_errors: List[str]
    - failed_constraints: List[Dict]
    - decision_hash: str
    - policy_hash: str
    - engine_version: str
    """

    # Compute deterministic hashes
    decision_hash = deterministic_hash(envelope)
    policy_hash = policy.policy_hash()

    # Step 1: Structural validation
    structural_valid, structural_errors = structural_validate(envelope)

    if not structural_valid:
        return {
            "structural_valid": False,
            "decision_valid": False,
            "structural_errors": structural_errors,
            "failed_constraints": [],
            "decision_hash": decision_hash,
            "policy_hash": policy_hash,
            "engine_version": ENGINE_VERSION,
        }

    # Step 2: Policy constraint evaluation
    failed_constraints = []

    for constraint in policy.constraints:
        passed, failure_reason = evaluate_constraint(envelope, constraint)

        if not passed:
            actual_value = envelope.get(constraint.field)
            failed_constraints.append({
                "constraint_id": constraint.constraint_id,
                "field": constraint.field,
                "operator": constraint.operator,
                "value": constraint.value,
                "actual": actual_value,
                "severity": constraint.severity,
                "reason": failure_reason,
            })

    # Sort failed constraints by constraint_id for deterministic output
    failed_constraints.sort(key=lambda x: x["constraint_id"])

    # Decision is valid only if no HARD constraints failed
    has_hard_failures = any(
        fc["severity"] == "HARD"
        for fc in failed_constraints
    )
    decision_valid = not has_hard_failures

    return {
        "structural_valid": True,
        "decision_valid": decision_valid,
        "structural_errors": [],
        "failed_constraints": failed_constraints,
        "decision_hash": decision_hash,
        "policy_hash": policy_hash,
        "engine_version": ENGINE_VERSION,
    }
