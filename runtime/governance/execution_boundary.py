from typing import List, Optional
from runtime.governance.decision_envelope import DecisionEnvelope
from runtime.governance.chain_verifier import verify_chain


class ExecutionBoundary:
    """
    Level 2 Execution Isolation Boundary.

    Responsible for:
    - Creating DecisionEnvelope
    - Maintaining hash chain
    - Performing integrity verification
    """

    def __init__(self, engine_version: str):
        self.engine_version = engine_version
        self._previous_hash: Optional[str] = None
        self.history: List[DecisionEnvelope] = []

    def record(
        self,
        policy_name: str,
        policy_version: str,
        config_hash: str,
        t: int,
        candidates,
        positions,
        cash: float,
    ):

        envelope = DecisionEnvelope.create(
            engine_version=self.engine_version,
            policy_name=policy_name,
            policy_version=policy_version,
            config_hash=config_hash,
            t=t,
            candidates=candidates,
            positions=positions,
            cash=cash,
            previous_hash=self._previous_hash,
        )

        self._previous_hash = envelope.envelope_hash
        self.history.append(envelope)

    def finalize(self):
        """
        Fail-closed verification.
        """
        if not verify_chain(self.history):
            raise RuntimeError("Execution chain integrity violation detected")