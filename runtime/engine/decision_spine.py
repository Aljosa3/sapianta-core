"""
SAPIANTA Decision Spine
Canonical runtime decision pipeline.
"""

from .proposal_validator import validate_proposal
from .policy_engine import evaluate_policy
from .decision_envelope_builder import build_decision_envelope
from .ledger_writer import write_ledger_entry
from runtime.artifacts.artifact_registry import register_artifact


def run_decision_pipeline(proposal: dict) -> dict:
    """
    Executes the full decision spine pipeline.
    """

    # 1 validate proposal
    validate_proposal(proposal)

    # 2 policy evaluation
    policy_result = evaluate_policy(proposal)

    # 3 build decision envelope
    envelope = build_decision_envelope(proposal, policy_result)

    # 4 record in ledger
    write_ledger_entry(envelope)

    # 5 register artifact
    register_artifact(
        artifact_type="decision_envelope",
        domain_id=proposal["domain_id"],
        artifact_location="runtime/history/decision_ledger.jsonl",
        producer="decision_spine",
        metadata={
            "proposal_id": proposal["proposal_id"],
            "decision_result": envelope["decision_result"]
        }
    )

    return envelope