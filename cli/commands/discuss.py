from datetime import datetime
import uuid

from runtime.discussion.discussion_engine import DiscussionEngine
from runtime.development.dev_orchestrator import DevelopmentOrchestrator
from runtime.development.idea_detector import detect_idea
from . import dev_add_task


class IdeaParser:

    @staticmethod
    def parse(user_input: str):

        idea = {
            "idea_id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat(),
            "description": user_input.strip(),
        }

        return idea


class TaskProposalGenerator:

    @staticmethod
    def generate(idea: dict):

        task = {
            "task_id": str(uuid.uuid4()),
            "title": idea["description"],
            "description": f"Implement idea: {idea['description']}",
            "priority": "normal",
            "created_at": datetime.utcnow().isoformat(),
        }

        return task


def run(args):

    print("\nSAPIANTA Discussion Mode")
    print("------------------------")
    print("Commands: implement | task | confirm | exit")

    engine = DiscussionEngine()
    orchestrator = DevelopmentOrchestrator()

    implement_mode = False

    while True:

        # SAFE INPUT (Ctrl+C handling)
        try:
            user_input = input("\nYou: ").strip()
        except KeyboardInterrupt:
            print("\nExiting discussion.")
            break

        if user_input.lower() in ["exit", "quit"]:
            print("\nExiting discussion.")
            break

        if not user_input:
            continue

        # ENTER IMPLEMENT MODE
        if user_input.lower() == "implement":

            print("\nSwitching to IMPLEMENT MODE")
            print("\nIMPLEMENT MODE activated.\n")

            context = "\n".join(
                m["content"]
                for m in engine.messages
                if m["role"] != "system"
            )

            orchestrator.run_implementation(context)

            implement_mode = True
            continue

        # CONFIRM PATCH
        if implement_mode and user_input.lower() == "confirm":

            print("\nApplying patch...\n")

            orchestrator.apply_patch()

            print("✅ Patch applied successfully.")

            implement_mode = False
            continue

        # IDEA → TASK PROPOSAL
        if user_input.lower().startswith("task "):

            idea_text = user_input[5:]

            idea = IdeaParser.parse(idea_text)
            task = TaskProposalGenerator.generate(idea)

            print("\nSAPIANTA Task Proposal")
            print("----------------------")

            print(f"Title: {task['title']}")
            print(f"Description: {task['description']}")
            print(f"Priority: {task['priority']}")

            # SAFE CONFIRM INPUT
            try:
                confirm = input("\nCreate implementation for this task? (y/n): ")
            except KeyboardInterrupt:
                print("\nTask cancelled.")
                continue

            if confirm.lower() == "y":

                context = task["description"]

                orchestrator.run_implementation(context)

                implement_mode = True

            else:

                print("Task discarded.")

            continue

        # NORMAL DISCUSSION
        response = engine.ask(user_input)

        print("\nSAPIANTA:", response)

        # --- AUTO IDEA DETECTION ---
        if detect_idea(user_input):

            print("\n[AI] Development idea detected.")

            args = [user_input]

            dev_add_task.run(args)

            print("[AI] Task automatically added to registry.")