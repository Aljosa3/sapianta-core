from runtime.modules.credit_validation.validator import validate_decision
from runtime.modules.credit_validation.policy import (
    PolicyConstraint,
    CreditPolicyObject,
)
import json


# ==========================================================
# POLICY (Industrial Demo Version)
# ==========================================================

policy = CreditPolicyObject(
    policy_version="credit_policy_v1.0_industrial_demo",
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


# ==========================================================
# CREDIT CASES
# ==========================================================

cases = {

    "CASE_A_PASS": {
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
    },

    "CASE_B_FAIL_EXPOSURE": {
        "decision_id": "CREDIT-2026-0002",
        "timestamp": "2026-02-22T10:05:00Z",
        "policy_version": policy.policy_version,
        "currency": "EUR",
        "client_id": "COMPANY-BETA-02",
        "rating": "B",
        "sector_code": "F",
        "requested_exposure": 2_200_000,  # exceeds rating limit
        "tenor_months": 36,
        "collateral_value": 3_000_000,
        "collateral_type": "commercial_real_estate",
        "collateral_coverage_ratio": 1.4,
        "current_client_exposure": 500_000,
        "current_group_exposure": 1_000_000,
        "current_sector_exposure": 20_000_000,
        "total_portfolio_exposure": 450_000_000,
    },

    "CASE_C_FAIL_COLLATERAL": {
        "decision_id": "CREDIT-2026-0003",
        "timestamp": "2026-02-22T10:10:00Z",
        "policy_version": policy.policy_version,
        "currency": "EUR",
        "client_id": "COMPANY-GAMMA-03",
        "rating": "B",
        "sector_code": "F",
        "requested_exposure": 1_000_000,
        "tenor_months": 36,
        "collateral_value": 700_000,
        "collateral_type": "machinery",
        "collateral_coverage_ratio": 0.7,  # below threshold
        "current_client_exposure": 1_500_000,
        "current_group_exposure": 2_500_000,
        "current_sector_exposure": 15_000_000,
        "total_portfolio_exposure": 450_000_000,
    },
}


# ==========================================================
# INDUSTRIAL OUTPUT FORMATTER
# ==========================================================

def print_audit_summary(case_name, result):

    print("\n==========================================================")
    print(f"VALIDATION REPORT: {case_name}")
    print("----------------------------------------------------------")

    status = "APPROVED" if result["decision_valid"] else "REJECTED"
    print(f"Decision Status : {status}")
    print(f"Policy Version  : {result['policy_version']}")
    print(f"Engine Version  : {result['engine_version']}")
    print(f"Decision Hash   : {result['decision_hash']}")
    print(f"Policy Hash     : {result['policy_hash']}")

    if result["failed_constraints"]:
        print("\nFailure Reasons:")
        for fc in result["failed_constraints"]:
            print(f" - {fc['constraint_id']} | {fc['description']}")

    print("==========================================================")


# ==========================================================
# EXECUTION
# ==========================================================

if __name__ == "__main__":

    print("\nSAPIANTA Credit Decision Validation Demonstrator v1.0")

    for case_name, envelope in cases.items():
        result = validate_decision(envelope, policy)
        print_audit_summary(case_name, result)