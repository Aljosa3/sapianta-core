import sys

from sapianta_system.runtime.cli.discuss import run_discussion


def print_help():

    print("\nSAPIANTA CLI")
    print("------------")
    print("Available commands:\n")
    print("sapianta discuss     start architecture discussion with LLM")
    print("sapianta research    run autonomous research cycle")
    print("sapianta reflect     system self-analysis")
    print()


def main():

    if len(sys.argv) < 2:
        print_help()
        return

    command = sys.argv[1]

    if command == "discuss":
        run_discussion()

    elif command == "research":

        from sapianta_system.runtime.system.autonomy_controller import run_autonomy_loop

        run_autonomy_loop()

    elif command == "reflect":

        from sapianta_system.runtime.system.system_knowledge import SystemKnowledge

        sk = SystemKnowledge()

        state = sk.build_knowledge()

        print("\nSystem capabilities:\n")

        for c in state.get("capabilities", []):
            print("-", c)

    else:
        print("\nUnknown command\n")
        print_help()


if __name__ == "__main__":
    main()