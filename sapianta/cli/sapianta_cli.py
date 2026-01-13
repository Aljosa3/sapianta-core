from sapianta.interaction.adapters.cli_adapter import handle_cli_input
from sapianta.runtime import RuntimeDecision


def main():
    user_input = input("Sapianta > ")
    result = handle_cli_input(user_input)

    print(f"Runtime: {result.decision}")

    if result.decision == RuntimeDecision.HALT:
        print(f"Reason: {result.reason}")

    print(f"Core: {result.core_response.status} {result.core_response.reason}")


if __name__ == "__main__":
    main()
