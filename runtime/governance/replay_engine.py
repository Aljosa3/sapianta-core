from typing import List, Callable
from runtime.governance.chain_verifier import verify_chain
from runtime.governance.decision_envelope import DecisionEnvelope


class ReplayMismatchError(Exception):
    pass


def replay_and_verify(
    engine_factory: Callable[[], object],
    original_history: List[DecisionEnvelope],
):
    """
    Re-run engine and verify that the resulting
    DecisionEnvelope chain is identical.

    engine_factory:
        zero-argument callable returning fresh engine instance

    original_history:
        previously recorded DecisionEnvelope list
    """

    # 1️⃣ Run fresh engine
    engine = engine_factory()
    engine.run()

    new_history = engine.portfolio.history

    # 2️⃣ Verify both chains internally valid
    if not verify_chain(original_history):
        raise ReplayMismatchError("Original chain invalid")

    if not verify_chain(new_history):
        raise ReplayMismatchError("Replayed chain invalid")

    # 3️⃣ Length must match
    if len(original_history) != len(new_history):
        raise ReplayMismatchError("History length mismatch")

    # 4️⃣ Envelope-by-envelope hash match
    for idx, (orig, new) in enumerate(zip(original_history, new_history)):

        if orig.envelope_hash != new.envelope_hash:
            raise ReplayMismatchError(
                f"Envelope hash mismatch at index {idx}"
            )

    return True