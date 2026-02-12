"""
PHASE 5.0 — CLI Integration Bridge

Deterministic CLI wrapper around HOIAdapter.

Responsibilities:
- Accept raw CLI input
- Pass input into HOIAdapter
- Print deterministic canonical export
- No advisory logic
- No LLM call
- No side effects beyond stdout
"""

import sys
from sapianta_hoi.integration.hoi_adapter import HOIAdapter
from sapianta_hoi.prompt_export.prompt_builder import build_prompt_payload


class HOICLI:
    """
    Minimal deterministic CLI interface.

    Flow:
    CLI → HOIAdapter → Canonical State → Prompt Payload
    """

    def __init__(self):
        self._adapter = HOIAdapter()

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
                canonical_state = self._adapter.handle_input(user_input)

                prompt_payload = build_prompt_payload(canonical_state)

                print("\n--- CANONICAL STATE ---")
                print(canonical_state)

                print("\n--- PROMPT PAYLOAD ---")
                print(prompt_payload)
                print("\n")

            except Exception as e:
                print(f"[ERROR] {e}")


if __name__ == "__main__":
    cli = HOICLI()
    cli.run()
