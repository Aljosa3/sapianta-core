import pytest

from runtime.modules.credit_validation.policy import (
    CreditPolicyObject,
    PolicyConstraint,
)


def build_policy():

    return CreditPolicyObject(
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
        ],
    )


# ============================================
# Deterministic Hash Test
# ============================================

def test_policy_hash_is_deterministic():

    policy1 = build_policy()
    policy2 = build_policy()

    assert policy1.policy_hash() == policy2.policy_hash()


# ============================================
# Hash Change on Description Change
# ============================================

def test_policy_hash_changes_on_description_change():

    policy1 = build_policy()

    modified_policy = CreditPolicyObject(
        policy_version="v1.1_dsl",
        constraints=[
            PolicyConstraint(
                constraint_id="MAX_EXPOSURE",
                description="Different description",
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
        ],
    )

    assert policy1.policy_hash() != modified_policy.policy_hash()


# ============================================
# Hash Change on Constraint Order
# ============================================

def test_policy_hash_changes_on_constraint_order():

    policy1 = build_policy()

    reversed_policy = CreditPolicyObject(
        policy_version="v1.1_dsl",
        constraints=list(reversed(policy1.constraints)),
    )

    assert policy1.policy_hash() != reversed_policy.policy_hash()