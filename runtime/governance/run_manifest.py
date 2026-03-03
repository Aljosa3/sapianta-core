from dataclasses import dataclass, asdict
from typing import List, Optional
from runtime.governance.decision_envelope import DecisionEnvelope
from runtime.governance.chain_verifier import verify_chain
from runtime.trading.deterministic_utils import stable_hash


@dataclass(frozen=True)
class RunManifest:

    engine_version: str
    policy_name: str
    policy_version: str
    config_hash: str

    envelope_count: int
    first_hash: Optional[str]
    last_hash: Optional[str]

    run_hash: str


def generate_run_manifest(history: List[DecisionEnvelope]) -> RunManifest:

    if not history:
        return RunManifest(
            engine_version="unknown",
            policy_name="unknown",
            policy_version="unknown",
            config_hash="unknown",
            envelope_count=0,
            first_hash=None,
            last_hash=None,
            run_hash="empty",
        )

    # Integrity check (fail-closed)
    if not verify_chain(history):
        raise RuntimeError("Invalid execution chain — cannot create manifest")

    first = history[0]
    last = history[-1]

    manifest_payload = {
        "engine_version": last.engine_version,
        "policy_name": last.policy_name,
        "policy_version": last.policy_version,
        "config_hash": last.config_hash,
        "envelope_count": len(history),
        "first_hash": first.envelope_hash,
        "last_hash": last.envelope_hash,
    }

    run_hash = stable_hash(manifest_payload)

    return RunManifest(
        engine_version=last.engine_version,
        policy_name=last.policy_name,
        policy_version=last.policy_version,
        config_hash=last.config_hash,
        envelope_count=len(history),
        first_hash=first.envelope_hash,
        last_hash=last.envelope_hash,
        run_hash=run_hash,
    )