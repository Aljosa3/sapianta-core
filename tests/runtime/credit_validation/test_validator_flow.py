import pytest

from runtime.modules.credit_validation.validator import validate_decision
from runtime.modules.credit_validation.policy import (
    PolicyConstraint,
    CreditPolicyObject,
)


# ===============================
# DSL Policy Definition (v1.1)
# ===============================

policy = CreditPolicyObject(
    policy_version="v1.1_dsl",
    constraints=[
        PolicyConstraint(
            constraint_id="MAX_EXPOSURE",
            description="Requested exposure must be <= 1.5M",
            severity="HARD",
            field="requested_exposure",
            operator="<=",
            value=1_500_000,
        ),
        PolicyConstraint(
            constraint_id="COLLATERAL_RATIO",
            description="Collateral coverage ratio must be >= 1.0",
            severity="HARD",
            field="collateral_coverage_ratio",
            operator=">=",
            value=1.0,
        ),
        PolicyConstraint(
            constraint_id="SOFT_GROUP_EXPOSURE",
            description="Group exposure warning threshold",
            severity="SOFT",
            field="current_group_exposure",
            operator="<=",
            value=5_000_000,
        ),
    ],
)


# ===============================
# PASS Scenario
# ===============================

def test_credit_validation_pass():

    decision = {
        "decision_id": "D-001",
        "timestamp": "2026-02-22T10:00:00Z",
        "policy_version": "v1.1_dsl",
        "currency": "EUR",
        "client_id": "C-100",
        "rating": "B",
        "sector_code": "F",
        "requested_exposure": 1_000_000,
        "tenor_months": 36,
        "collateral_value": 1_500_000,
        "collateral_type": "real_estate",
        "collateral_coverage_ratio": 1.2,
        "current_client_exposure": 1_000_000,
        "current_group_exposure": 1_000_000,
        "current_sector_exposure": 5_000_000,
        "total_portfolio_exposure": 50_000_000,
    }

    result = validate_decision(decision, policy)

    assert result["structural_valid"] is True
    assert result["decision_valid"] is True
    assert result["failed_constraints"] == []


# ===============================
# FAIL Scenario (HARD constraints)
# ===============================

def test_credit_validation_fail():

    decision = {
        "decision_id": "D-002",
        "timestamp": "2026-02-22T10:00:00Z",
        "policy_version": "v1.1_dsl",
        "currency": "EUR",
        "client_id": "C-200",
        "rating": "B",
        "sector_code": "F",
        "requested_exposure": 2_000_000,  # exceeds limit
        "tenor_months": 36,
        "collateral_value": 1_000_000,
        "collateral_type": "real_estate",
        "collateral_coverage_ratio": 0.8,  # too low
        "current_client_exposure": 2_000_000,
        "current_group_exposure": 2_000_000,
        "current_sector_exposure": 5_000_000,
        "total_portfolio_exposure": 50_000_000,
    }

    result = validate_decision(decision, policy)

    assert result["structural_valid"] is True
    assert result["decision_valid"] is False

    failed_ids = {c["constraint_id"] for c in result["failed_constraints"]}

    assert "MAX_EXPOSURE" in failed_ids
    assert "COLLATERAL_RATIO" in failed_ids


# ===============================
# SOFT Constraint Test
# ===============================

def test_soft_constraint_does_not_block():

    decision = {
        "decision_id": "D-003",
        "timestamp": "2026-02-22T10:00:00Z",
        "policy_version": "v1.1_dsl",
        "currency": "EUR",
        "client_id": "C-300",
        "rating": "B",
        "sector_code": "F",
        "requested_exposure": 1_000_000,
        "tenor_months": 36,
        "collateral_value": 1_500_000,
        "collateral_type": "real_estate",
        "collateral_coverage_ratio": 1.2,
        "current_client_exposure": 1_000_000,
        "current_group_exposure": 6_000_000,  # exceeds SOFT threshold
        "current_sector_exposure": 5_000_000,
        "total_portfolio_exposure": 50_000_000,
    }

    result = validate_decision(decision, policy)

    assert result["structural_valid"] is True
    assert result["decision_valid"] is True

    failed_ids = {c["constraint_id"] for c in result["failed_constraints"]}
    assert "SOFT_GROUP_EXPOSURE" in failed_ids


# ===============================
# Determinism Test
# ===============================

def test_credit_validation_hash_determinism():

    decision = {
        "decision_id": "D-004",
        "timestamp": "2026-02-22T10:00:00Z",
        "policy_version": "v1.1_dsl",
        "currency": "EUR",
        "client_id": "C-400",
        "rating": "B",
        "sector_code": "F",
        "requested_exposure": 1_000_000,
        "tenor_months": 36,
        "collateral_value": 1_500_000,
        "collateral_type": "real_estate",
        "collateral_coverage_ratio": 1.2,
        "current_client_exposure": 1_000_000,
        "current_group_exposure": 1_000_000,
        "current_sector_exposure": 5_000_000,
        "total_portfolio_exposure": 50_000_000,
    }

    result1 = validate_decision(decision, policy)
    result2 = validate_decision(decision, policy)

    assert result1["decision_hash"] == result2["decision_hash"]
    assert result1["decision_valid"] == result2["decision_valid"]
    assert result1["policy_hash"] == result2["policy_hash"]