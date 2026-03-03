from typing import List
from runtime.governance.decision_envelope import DecisionEnvelope
from runtime.trading.deterministic_utils import stable_hash


def verify_chain(history: List[DecisionEnvelope]) -> bool:
    """
    Verify integrity of a DecisionEnvelope hash chain.

    Checks:
    - Each envelope_hash matches recomputed hash
    - previous_hash matches previous envelope's envelope_hash
    - Chain starts correctly (previous_hash is None for first element)

    Returns:
        True if chain is valid
        False if any integrity violation is detected
    """

    if not history:
        return True

    previous_hash = None

    for envelope in history:

        # 1️⃣ Check previous hash linkage
        if envelope.previous_hash != previous_hash:
            return False

        # 2️⃣ Recompute expected hash
        base_payload = {
            "engine_version": envelope.engine_version,
            "policy_name": envelope.policy_name,
            "policy_version": envelope.policy_version,
            "config_hash": envelope.config_hash,
            "t": envelope.t,
            "candidates": envelope.candidates,
            "positions": envelope.positions,
            "cash": envelope.cash,
            "previous_hash": envelope.previous_hash,
        }

        expected_hash = stable_hash(base_payload)

        if envelope.envelope_hash != expected_hash:
            return False

        previous_hash = envelope.envelope_hash

    return True