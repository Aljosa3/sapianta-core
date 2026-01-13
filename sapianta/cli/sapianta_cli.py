from sapianta.interaction.adapters.cli_adapter import handle_cli_input


def main():
    user_input = input("Sapianta > ")
    response = handle_cli_input(user_input)

    core_response = response.core_response
    print(f"[{core_response.status}] {core_response.reason}")


if __name__ == "__main__":
    main()
