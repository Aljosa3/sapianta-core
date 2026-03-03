from runtime.domain_contract import DomainPolicy
from runtime.modules.credit_validation.policy import (
    CreditPolicyObject,
    PolicyConstraint,
)


class CreditDomainPolicy(DomainPolicy):

    POLICY_NAME = "credit_domain"
    POLICY_VERSION = "1.0"

    def __init__(self, config):
        """
        Adapter layer between ExecutionBoundary
        and low-level CreditPolicyObject.
        """

        constraints = []

        if "min_income" in config:
            constraints.append(
                PolicyConstraint(
                    constraint_id="min_income",
                    description="Minimum required income",
                    severity="HARD",
                    field="income",
                    operator=">=",
                    value=config["min_income"],
                )
            )

        if "max_dti" in config:
            constraints.append(
                PolicyConstraint(
                    constraint_id="max_dti",
                    description="Maximum debt-to-income ratio",
                    severity="HARD",
                    field="dti",
                    operator="<=",
                    value=config["max_dti"],
                )
            )

        self._policy = CreditPolicyObject(
            policy_version=self.POLICY_VERSION,
            constraints=constraints,
        )

    # ------------------------------------------------------------------
    # 🔹 Domain-agnostic execution entry point
    # ------------------------------------------------------------------

    def execute(self, input_data, config, t=None):
        """
        DomainPolicy contract implementation.
        Deterministic evaluation of credit application.
        """

        violations = []

        for constraint in self._policy.constraints:

            field_value = input_data.get(constraint.field)

            if field_value is None:
                continue

            if not self._evaluate_constraint(
                field_value,
                constraint.operator,
                constraint.value,
            ):
                violations.append(constraint.constraint_id)

        if violations:
            return ("REJECTED", tuple(sorted(violations)))

        return ("APPROVED", ())

    # ------------------------------------------------------------------
    # Deterministic constraint evaluation
    # ------------------------------------------------------------------

    def _evaluate_constraint(self, lhs, operator, rhs):

        if operator == "<=":
            return lhs <= rhs
        if operator == "<":
            return lhs < rhs
        if operator == ">=":
            return lhs >= rhs
        if operator == ">":
            return lhs > rhs
        if operator == "==":
            return lhs == rhs
        if operator == "!=":
            return lhs != rhs

        raise ValueError("Unsupported operator")