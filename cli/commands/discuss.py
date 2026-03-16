from runtime.discussion.discussion_engine import DiscussionEngine
from runtime.development.dev_orchestrator import DevelopmentOrchestrator


def run(args):

    print("\nSAPIANTA Discussion Mode")
    print("------------------------")

    engine = DiscussionEngine()
    orchestrator = DevelopmentOrchestrator()

    implement_mode = False

    while True:

        user_input = input("\nYou: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("\nExiting discussion.")
            break

        # ENTER IMPLEMENT MODE
        if user_input.lower() == "implement":

            print("\nSwitching to IMPLEMENT MODE")
            print("\nIMPLEMENT MODE activated.\n")

            # Build context from discussion history
            context = "\n".join(
                m["content"]
                for m in engine.messages
                if m["role"] != "system"
            )

            orchestrator.run_implementation(context)

            implement_mode = True
            continue

        # CONFIRM PATCH APPLICATION
        if implement_mode and user_input.lower() == "confirm":

            print("\nApplying patch...\n")

            orchestrator.apply_patch()

            print("✅ Patch applied successfully.")

            implement_mode = False
            continue

        # NORMAL DISCUSSION
        response = engine.ask(user_input)

        print("\nSAPIANTA:", response)