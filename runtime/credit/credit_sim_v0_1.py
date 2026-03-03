from runtime.modules.credit_validation.credit_domain_policy import CreditDomainPolicy
from runtime.domain_contract import DomainPolicy
from runtime.trading.deterministic_utils import stable_hash, freeze_config
from runtime.governance.execution_boundary import ExecutionBoundary


class CreditEngine:

    def __init__(self, config, applications):

        # Deterministic config handling
        self.config_hash = stable_hash(config)
        self.config = freeze_config(config)

        self.applications = applications

        # Governance isolation boundary
        self.boundary = ExecutionBoundary(engine_version="0.1")

        # DomainPolicy adapter
        self.policy: DomainPolicy = CreditDomainPolicy(self.config)

    def run(self):

        for idx, application in enumerate(self.applications):

            # 🔄 NEW: use domain-agnostic execute()
            decision = self.policy.execute(
                application,
                self.config,
                idx
            )

            # Governance recording
            self.boundary.record(
                policy_name=self.policy.POLICY_NAME,
                policy_version=self.policy.POLICY_VERSION,
                config_hash=self.config_hash,
                t=idx,
                candidates=(decision,),
                positions={},
                cash=0.0,
            )

        # Fail-closed integrity enforcement
        self.boundary.finalize()

        return self.boundary.history