"""
PHASE 8.1 — Advisory CLI + Live Audit Recording

Deterministic CLI wrapper around HOIAdapter.

Responsibilities:
- Accept raw CLI input
- Pass input into HOIAdapter
- Print canonical export
- Print prompt payload
- Print advisory overlay (non-invasive)
- Record event sequence
- Record canonical export hash
- No LLM call
- No execution side effects beyond stdout
"""

import hashlib
import json

from sapianta_hoi.integration.hoi_adapter import HOIAdapter
from sapianta_hoi.prompt_export.prompt_builder import build_prompt_payload
from sapianta_hoi.advisory.advisory_engine import AdvisoryEngine
from sapianta_hoi.audit.session_recorder import SessionRecorder


class HOICLI:
    """
    Deterministic CLI interface with advisory overlay
    and live in-memory audit recording.

    Flow:
    CLI → HOIAdapter → Canonical Export
                              ↓
                        Prompt Payload
                              ↓
                        Advisory Overlay
                              ↓
                        Audit Recorder
    """

    def __init__(self):
        self._adapter = HOIAdapter()
        self._advisory_engine = AdvisoryEngine()
        self._recorder = SessionRecorder()

    def run(self):
        print("SAPIANTA HOI CLI — Deterministic Mode (Advisory + Audit Enabled)")
        print("Type event names exactly as registered.")
        print("Type 'exit' to quit.\n")

        while True:
            user_input = input("event> ").strip()

            if user_input.lower() == "exit":
                print("\nFinalizing session audit...\n")
                self._finalize_audit()
                print("Exiting.")
                break

            try:
                canonical_snapshot = self._adapter.handle_input(user_input)

                prompt_payload = build_prompt_payload(canonical_snapshot)

                advisory_overlay = self._advisory_engine.generate(
                    canonical_snapshot
                )

                state_hash = self._hash_export(canonical_snapshot)

                # Record event + hash deterministically
                self._recorder.record_step(
                    event=user_input,
                    state_hash=state_hash
                )

                print("\n--- CANONICAL EXPORT ---")
                print(canonical_snapshot)

                print("\n--- PROMPT PAYLOAD ---")
                print(prompt_payload)

                print("\n--- ADVISORY OVERLAY ---")
                print(advisory_overlay)

                print("\n--- STATE HASH ---")
                print(state_hash)

                print("\n")

            except Exception as e:
                print(f"[ERROR] {e}")

    def _hash_export(self, export_payload: dict) -> str:
        serialized = json.dumps(export_payload, sort_keys=True)
        return hashlib.sha256(serialized.encode()).hexdigest()

    def _finalize_audit(self):
        session_summary = self._recorder.finalize()

        print("--- AUDIT SESSION SUMMARY ---")
        print(session_summary)


if __name__ == "__main__":
    cli = HOICLI()
    cli.run()
