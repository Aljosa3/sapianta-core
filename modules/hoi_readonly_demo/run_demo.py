"""
HOI Read-only Demo

Manual demonstration of HOI handling modes.
No signal detection. No adaptation. No persistence.
"""

def main():
    print("\nHOI READ-ONLY DEMO")
    print("------------------")
    print("Select handling mode:")
    print("1) ORIENT")
    print("2) PAUSE")
    print("3) REDIRECT")

    choice = input("\nEnter choice (1/2/3): ").strip()

    if choice == "1":
        mode = "ORIENT"
        rationale = "User requires additional orientation."
    elif choice == "2":
        mode = "PAUSE"
        rationale = "Continuation without orientation is not legitimate."
    elif choice == "3":
        mode = "REDIRECT"
        rationale = "Safe redirection to an orientational path."
    else:
        print("\nInvalid choice. No action taken.")
        return

    print("\n--- HOI HANDLING MODE ACTIVATED ---")
    print(f"Mode      : {mode}")
    print(f"Rationale : {rationale}")
    print("Reference : HUMAN_ORIENTATION_SAFEGUARD")
    print("----------------------------------")


if __name__ == "__main__":
    main()
