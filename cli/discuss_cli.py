class DiscussCLI:

    def run(self):

        engine = DiscussionEngine()

        print("\nSAPIANTA Discussion Mode")
        print("------------------------")
        print("Type 'exit' to quit")
        print("Type 'implement' to convert idea into implementation task\n")

        last_response = None

        while True:

            user_input = input("You: ")

            if user_input == "exit":
                break

            if user_input == "implement":

                if last_response is None:
                    print("No discussion context available.")
                    continue

                from sapianta_system.runtime.development.dev_orchestrator import DevOrchestrator
                from sapianta_system.runtime.development.implementation_request import ImplementationRequest

                request = ImplementationRequest(
                    discussion_context=last_response
                )

                orchestrator = DevOrchestrator()

                patch = orchestrator.run(request)

                print("\n--- PATCH PROPOSAL ---\n")
                print(patch)

                continue

            last_response = engine.ask(user_input)

            print("\nSAPIANTA:", last_response)