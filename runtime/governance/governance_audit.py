from dataclasses import dataclass
from typing import List, Optional
from runtime.trading.decision_envelope import DecisionEnvelope
from runtime.trading.chain_verifier import verify_chain


@dataclass(frozen=True)
class GovernanceAuditReport:
    chain_valid: bool
    envelope_count: int
    first_hash: Optional[str]
    last_hash: Optional[str]
    policy_name: Optional[str]
    policy_version: Optional[str]
    config_hash: Optional[str]


def generate_audit_report(history: List[DecisionEnvelope]) -> GovernanceAuditReport:

    if not history:
        return GovernanceAuditReport(
            chain_valid=True,
            envelope_count=0,
            first_hash=None,
            last_hash=None,
            policy_name=None,
            policy_version=None,
            config_hash=None,
        )

    chain_valid = verify_chain(history)

    first = history[0]
    last = history[-1]

    return GovernanceAuditReport(
        chain_valid=chain_valid,
        envelope_count=len(history),
        first_hash=first.envelope_hash,
        last_hash=last.envelope_hash,
        policy_name=last.policy_name,
        policy_version=last.policy_version,
        config_hash=last.config_hash,
    )