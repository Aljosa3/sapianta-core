import pytest

from runtime.modules.trading_validation.validator import validate_trading_decision
from runtime.modules.trading_validation.policy import (
    PolicyConstraint,
    TradingPolicyObject,
)


# ===============================
# Helper Functions
# ===============================

def valid_envelope():
    """
    Returns a valid trading decision envelope with all required fields.
    """
    return {
        "decision_id": "D-001",
        "timestamp_utc": "2026-02-26T10:00:00Z",
        "venue": "IBKR",
        "asset": "BTCUSDT",
        "side": "BUY",
        "entry_price": 50000.0,
        "stop_loss_price": 48000.0,
        "position_size": 1.0,
        "account_balance": 100000.0,
        "current_open_positions": 2,
        "total_exposure": 25000.0,
        "daily_pnl": -200.0,
        "leverage_ratio": 5.0,
    }


def base_policy(constraints_order="normal"):
    """
    Returns a TradingPolicyObject with HARD constraints.

    Args:
        constraints_order: "normal" or "reversed" for testing order independence
    """
    constraints = [
        PolicyConstraint(
            constraint_id="LEVERAGE_CAP",
            description="Leverage must be <= 10",
            severity="HARD",
            field="leverage_ratio",
            operator="<=",
            value=10.0,
        ),
        PolicyConstraint(
            constraint_id="MAX_OPEN_POSITIONS",
            description="Open positions must be <= 5",
            severity="HARD",
            field="current_open_positions",
            operator="<=",
            value=5,
        ),
        PolicyConstraint(
            constraint_id="DAILY_LOSS_KILL_SWITCH",
            description="Daily P&L must be >= -500",
            severity="HARD",
            field="daily_pnl",
            operator=">=",
            value=-500.0,
        ),
        PolicyConstraint(
            constraint_id="MAX_TOTAL_EXPOSURE",
            description="Total exposure must be <= 50000",
            severity="HARD",
            field="total_exposure",
            operator="<=",
            value=50000.0,
        ),
    ]

    if constraints_order == "reversed":
        constraints = list(reversed(constraints))

    return TradingPolicyObject(
        policy_version="v1.0",
        constraints=constraints,
    )


# ===============================
# Tests
# ===============================

def test_pass_scenario():
    """
    Test that a valid envelope passes all constraints.
    """
    envelope = valid_envelope()
    policy = base_policy()

    result = validate_trading_decision(envelope, policy)

    assert result["structural_valid"] is True
    assert result["decision_valid"] is True
    assert result["failed_constraints"] == []
    assert "decision_hash" in result
    assert "policy_hash" in result
    assert result["engine_version"] == "trading_validation_engine_v1.0"


def test_hard_fail_leverage_cap():
    """
    Test that exceeding leverage cap causes HARD constraint failure.
    """
    envelope = valid_envelope()
    envelope["leverage_ratio"] = 20.0  # Exceeds cap of 10

    policy = base_policy()

    result = validate_trading_decision(envelope, policy)

    assert result["structural_valid"] is True  # Structure is valid
    assert result["decision_valid"] is False   # But decision is invalid
    assert len(result["failed_constraints"]) == 1

    # Check that LEVERAGE_CAP constraint failed
    failed_ids = [fc["constraint_id"] for fc in result["failed_constraints"]]
    assert "LEVERAGE_CAP" in failed_ids

    # Verify failed constraint details
    leverage_failure = result["failed_constraints"][0]
    assert leverage_failure["field"] == "leverage_ratio"
    assert leverage_failure["severity"] == "HARD"
    assert leverage_failure["actual"] == 20.0


def test_determinism_hashes_stable():
    """
    Test that decision and policy hashes are deterministic across multiple runs.
    """
    envelope = valid_envelope()
    policy = base_policy()

    r1 = validate_trading_decision(envelope, policy)
    r2 = validate_trading_decision(envelope, policy)

    assert r1["decision_hash"] == r2["decision_hash"]
    assert r1["policy_hash"] == r2["policy_hash"]
    assert r1["decision_valid"] == r2["decision_valid"]


def test_policy_hash_order_independent_constraints():
    """
    Test that policy hash is independent of constraint ordering.
    Constraints are sorted by constraint_id internally for deterministic hashing.
    """
    envelope = valid_envelope()

    policy_a = base_policy("normal")
    policy_b = base_policy("reversed")

    ra = validate_trading_decision(envelope, policy_a)
    rb = validate_trading_decision(envelope, policy_b)

    # Policy hashes must be identical regardless of constraint order
    assert ra["policy_hash"] == rb["policy_hash"]

    # Both should produce same validation result
    assert ra["decision_valid"] == rb["decision_valid"]
    assert ra["structural_valid"] == rb["structural_valid"]


def test_structural_fail_missing_required_field():
    """
    Test that missing a required field causes structural validation failure.
    Structural failures must block decision approval and skip policy evaluation.
    """
    envelope = valid_envelope()
    # Remove one REQUIRED field to trigger structural validation failure
    envelope.pop("asset", None)  # required field per spec

    policy = base_policy()

    result = validate_trading_decision(envelope, policy)

    assert result["structural_valid"] is False

    # Decision must not be approved when structure invalid
    assert result["decision_valid"] is False

    # Structural failures are not policy failures; failed_constraints should be empty
    assert result["failed_constraints"] == []

    # Verify structural_errors contains information about missing field
    assert len(result["structural_errors"]) > 0
    assert any("asset" in err.lower() for err in result["structural_errors"])


def test_boundary_values_pass():
    """
    Test that values exactly at constraint boundaries pass validation.
    Validates inclusive boundaries for all HARD constraints.
    """
    envelope = valid_envelope()

    # Boundary values (exactly at limits should PASS)
    envelope["leverage_ratio"] = 10.0       # <= 10
    envelope["current_open_positions"] = 5  # <= 5
    envelope["daily_pnl"] = -500.0          # >= -500
    envelope["total_exposure"] = 50000.0    # <= 50000

    policy = base_policy()

    result = validate_trading_decision(envelope, policy)

    assert result["structural_valid"] is True
    assert result["decision_valid"] is True
    assert result["failed_constraints"] == []
