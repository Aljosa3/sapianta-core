from dataclasses import dataclass, asdict
from typing import Tuple, Dict, Any, Optional
from runtime.trading.deterministic_utils import stable_hash


@dataclass(frozen=True)
class DecisionEnvelope:
    """
    Governance-grade immutable execution artifact.

    Represents a single deterministic engine decision step.
    Fully hash-chained and replay-verifiable.
    """

    engine_version: str
    policy_name: str
    policy_version: str
    config_hash: str

    t: int
    candidates: Tuple
    positions: Dict
    cash: float

    previous_hash: Optional[str]
    envelope_hash: str

    @staticmethod
    def create(
        engine_version: str,
        policy_name: str,
        policy_version: str,
        config_hash: str,
        t: int,
        candidates: Tuple,
        positions: Dict,
        cash: float,
        previous_hash: Optional[str],
    ) -> "DecisionEnvelope":
        """
        Deterministically construct a hash-chained DecisionEnvelope.
        """

        base_payload = {
            "engine_version": engine_version,
            "policy_name": policy_name,
            "policy_version": policy_version,
            "config_hash": config_hash,
            "t": t,
            "candidates": candidates,
            "positions": positions,
            "cash": cash,
            "previous_hash": previous_hash,
        }

        envelope_hash = stable_hash(base_payload)

        return DecisionEnvelope(
            engine_version=engine_version,
            policy_name=policy_name,
            policy_version=policy_version,
            config_hash=config_hash,
            t=t,
            candidates=candidates,
            positions=positions,
            cash=cash,
            previous_hash=previous_hash,
            envelope_hash=envelope_hash,
        )

    # Backward compatibility for existing tests expecting dict-like access
    def __getitem__(self, key: str) -> Any:
        return getattr(self, key)

    def to_dict(self) -> dict:
        return asdict(self)