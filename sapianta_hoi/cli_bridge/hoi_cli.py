"""
PHASE 7.1 — Advisory CLI Overlay

Deterministic CLI wrapper around HOIAdapter.

Responsibilities:
- Accept raw CLI input
- Pass input into HOIAdapter
- Print deterministic canonical export
- Print prompt payload
- Print advisory overlay (non-invasive)
- No LLM call
- No execution side effects beyond stdout
"""

from sapianta_hoi.integration.hoi_adapter import HOIAdapter
from sapianta_hoi.prompt_export.prompt_builder import build_prompt_payload
from sapianta_hoi.advisory.advisory_engine import AdvisoryEngine


class HOICLI:
    """
    Deterministic CLI interface with advisory overlay.

    Flow:
    CLI → HOIAdapter → Canonical State
                              ↓
                        Prompt Payload
                              ↓
                        Advisory Overlay
    """

    def __init__(self):
        self._adapter = HOIAdapter()
        self._advisory_engine = AdvisoryEngine()

    def run(self):
        print("SAPIANTA HOI CLI — Deterministic Mode")
        print("Type event names exactly as registered.")
        print("Type 'exit' to quit.\n")

        while True:
            user_input = input("event> ").strip()

            if user_input.lower() == "exit":
                print("Exiting.")
                break

            try:
                canonical_snapshot = self._adapter.handle_input(user_input)

                prompt_payload = build_prompt_payload(canonical_snapshot)

                advisory_overlay = self._advisory_engine.generate(
                    canonical_snapshot
                )

                print("\n--- CANONICAL EXPORT ---")
                print(canonical_snapshot)

                print("\n--- PROMPT PAYLOAD ---")
                print(prompt_payload)

                print("\n--- ADVISORY OVERLAY ---")
                print(advisory_overlay)

                print("\n")

            except Exception as e:
                print(f"[ERROR] {e}")


if __name__ == "__main__":
    cli = HOICLI()
    cli.run()
