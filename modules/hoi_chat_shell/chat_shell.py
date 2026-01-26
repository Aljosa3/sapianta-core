"""
HOI ↔ Chat Shell (Read-only) with LLM Stub

Manual chat shell demonstrating cooperation between:
- Chat orchestration (this shell)
- Dummy LLM (language/explanation)
- HOI handling modes (manual)

No signal detection.
No observability mapping.
No adaptation.
No persistence.
"""

from modules.llm_stub.dummy_llm import DummyLLM


def hoi_menu():
    print("\n[HOI] Select handling mode:")
    print("1) ORIENT")
    print("2) PAUSE")
    print("3) REDIRECT")
    print("0) CONTINUE CHAT")
    return input("Choice: ").strip()


def apply_hoi(mode: str) -> bool:
    if mode == "1":
        print("\n[HOI:ORIENT]")
        print("Additional orientation requested.")
        print("Reference: HUMAN_ORIENTATION_SAFEGUARD")
        return True
    if mode == "2":
        print("\n[HOI:PAUSE]")
        print("Chat paused. Continuation without orientation is not legitimate.")
        print("Reference: HUMAN_ORIENTATION_SAFEGUARD")
        return False
    if mode == "3":
        print("\n[HOI:REDIRECT]")
        print("Chat redirected to an orientational path.")
        print("Reference: HUMAN_ORIENTATION_SAFEGUARD")
        return True

    print("\n[HOI] Invalid choice. Continuing chat.")
    return True


def main():
    llm = DummyLLM()

    print("\nSAPIANTA CHAT SHELL (with HOI + DummyLLM)")
    print("----------------------------------------")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("[USER] ").strip()
        if user_input.lower() == "exit":
            print("\n[CHAT] Session ended.")
            break

        reply = llm.respond(user_input)
        print("\n[LLM]")
        print(reply.text)

        choice = hoi_menu()
        if choice == "0":
            continue

        should_continue = apply_hoi(choice)
        if not should_continue:
            break


if __name__ == "__main__":
    main()
