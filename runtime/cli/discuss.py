from sapianta_system.runtime.discussion.discussion_engine import DiscussionEngine


def run_discussion():

    engine = DiscussionEngine()

    print("\nSAPIANTA Discussion Mode")
    print("------------------------")
    print("Type 'exit' to quit")
    print("Type 'implement' to convert idea into implementation task\n")

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("\nLeaving discussion mode.")
            break

        if user_input.lower() == "implement":

            print("\n[Prototype] Implementation request detected.")
            print("Future step: send goal to GAD planner.\n")
            continue

        response = engine.ask(user_input)

        print("\nSAPIANTA:", response)
        print()