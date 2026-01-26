"""
HOI ↔ Chat Shell (Read-only)

Manual chat shell demonstrating cooperation between
a chat interface and HOI handling modes.

No signal detection.
No observability mapping.
No adaptation.
"""

def hoi_menu():
    print("\n[HOI] Select handling mode:")
    print("1) ORIENT")
    print("2) PAUSE")
    print("3) REDIRECT")
    print("0) CONTINUE CHAT")

    return input("Choice: ").strip()


def apply_hoi(mode):
    if mode == "1":
        print("\n[HOI:ORIENT]")
        print("Additional orientation requested.")
        print("Reference: HUMAN_ORIENTATION_SAFEGUARD")
    elif mode == "2":
        print("\n[HOI:PAUSE]")
        print("Chat paused. Continuation without orientation is not legitimate.")
        print("Reference: HUMAN_ORIENTATION_SAFEGUARD")
        return False
    elif mode == "3":
        print("\n[HOI:REDIRECT]")
        print("Chat redirected to an orientational path.")
        print("Reference: HUMAN_ORIENTATION_SAFEGUARD")
    return True


def main():
    print("\nSAPIANTA CHAT SHELL (with HOI)")
    print("--------------------------------")
    print("Type 'exit' to quit.\n")

    running = True
    while running:
        user_input = input("[USER] ")

        if user_input.lower() == "exit":
            print("\n[CHAT] Session ended.")
            break

        print(f"\n[CHAT] Acknowledged: '{user_input}'")

        choice = hoi_menu()

        if choice == "0":
            continue

        running = apply_hoi(choice)


if __name__ == "__main__":
    main()
