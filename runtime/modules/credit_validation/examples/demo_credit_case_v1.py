from runtime.modules.credit_validation.validator import validate_decision
from runtime.modules.credit_validation.policy import (
    PolicyConstraint,
    CreditPolicyObject,
)
import json


# ===============================
# POLICY DEFINITION (Industrial Demo)
# ===============================

policy = CreditPolicyObject(
    policy_version="credit_policy_v1.0_demo",
    constraints=[
        PolicyConstraint(
            constraint_id="MAX_EXPOSURE_BY_RATING",
            description="Max exposure for rating B is 1.5M EUR",
            severity="HARD",
            evaluator=lambda d: d["requested_exposure"] <= 1_500_000,
        ),
        PolicyConstraint(
            constraint_id="MIN_COLLATERAL_RATIO",
            description="Collateral coverage ratio must be >= 1.0",
            severity="HARD",
            evaluator=lambda d: d["collateral_coverage_ratio"] >= 1.0,
        ),
        PolicyConstraint(
            constraint_id="CLIENT_CONCENTRATION_LIMIT",
            description="Client total exposure must not exceed 3M EUR",
            severity="HARD",
            evaluator=lambda d: (
                d["current_client_exposure"]
                + d["requested_exposure"]
                <= 3_000_000
            ),
        ),
    ],
)


# ===============================
# REALISTIC CREDIT CASE
# ===============================

decision_envelope = {
    "decision_id": "CREDIT-2026-0001",
    "timestamp": "2026-02-22T10:00:00Z",
    "policy_version": policy.policy_version,
    "currency": "EUR",
    "client_id": "COMPANY-ALPHA-01",
    "rating": "B",
    "sector_code": "F",
    "requested_exposure": 1_200_000,
    "tenor_months": 48,
    "collateral_value": 1_500_000,
    "collateral_type": "commercial_real_estate",
    "collateral_coverage_ratio": 1.25,
    "current_client_exposure": 1_000_000,
    "current_group_exposure": 2_000_000,
    "current_sector_exposure": 25_000_000,
    "total_portfolio_exposure": 450_000_000,
}


# ===============================
# VALIDATION EXECUTION
# ===============================

result = validate_decision(decision_envelope, policy)


# ===============================
# OUTPUT (Demonstration Artifact)
# ===============================

print("=== CREDIT DECISION VALIDATION RESULT ===")
print(json.dumps(result, indent=4))

print("\n=== REPRODUCIBILITY CLAIM ===")
print("If the same Decision Envelope, Policy, and Engine version")
print("are provided, the validation result will be identical.")