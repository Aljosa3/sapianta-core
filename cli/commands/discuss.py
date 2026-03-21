from datetime import datetime
import uuid

from runtime.discussion.discussion_engine import DiscussionEngine
from runtime.development.dev_orchestrator import DevelopmentOrchestrator
from runtime.development.idea_detector import detect_idea
from . import dev_add_task


# ---------------------------------------------------------
# 1. DETERMINISTIC LLM STUB (NO EXTERNAL DEPENDENCY)
# ---------------------------------------------------------

def ask_llm(prompt: str) -> str:
    return "[MOCK] " + prompt


# ---------------------------------------------------------
# 2. IDEA PARSER
# ---------------------------------------------------------

class IdeaParser:

    @staticmethod
    def parse(user_input: str):

        idea = {
            "idea_id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat(),
            "description": user_input.strip(),
        }

        return idea


# ---------------------------------------------------------
# 3. TASK GENERATORS
# ---------------------------------------------------------

class TaskProposalGenerator:

    @staticmethod
    def generate(idea: dict):

        # legacy format (for UI / orchestrator)
        task = {
            "task_id": str(uuid.uuid4()),
            "title": idea["description"],
            "description": f"Implement idea: {idea['description']}",
            "priority": "normal",
            "created_at": datetime.utcnow().isoformat(),
        }

        return task


class DeterministicTaskBuilder:

    @staticmethod
    def build(user_input: str):

        return {
            "goal": user_input.strip(),
            "priority": 1
        }


# ---------------------------------------------------------
# 4. CLI ENTRYPOINT
# ---------------------------------------------------------

def run(args):

    # =====================================================
    # CLI MODE (non-interactive)
    # =====================================================
    if args:

        user_input = " ".join(args).strip()

        if not user_input:
            print("[DISCUSS] Empty input")
            return

        print("\n[DISCUSS INPUT]")
        print("----------------")
        print(user_input)

        llm_output = ask_llm(user_input)

        print("\n[LLM OUTPUT]")
        print("----------------")
        print(llm_output)

        task = DeterministicTaskBuilder.build(user_input)

        print("\n[GENERATED TASK]")
        print("----------------")
        print(task)

        try:
            from runtime.development.dev_autonomous_loop import DevAutonomousLoop
        except Exception as e:
            print("\n[ERROR] Failed to import DevAutonomousLoop")
            print(str(e))
            return

        loop = DevAutonomousLoop()

        try:
            result = loop.submit_task(task)
        except Exception as e:
            print("\n[ERROR] Task submission failed")
            print(str(e))
            return

        print("\n[SUBMISSION RESULT]")
        print("----------------")
        print(result)

        return

    # =====================================================
    # INTERACTIVE MODE (existing system)
    # =====================================================

    print("\nSAPIANTA Discussion Mode")
    print("------------------------")
    print("Commands: implement | task | confirm | exit")

    engine = DiscussionEngine()
    orchestrator = DevelopmentOrchestrator()

    implement_mode = False

    while True:

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

        # ------------------------------------------------
        # IMPLEMENT MODE
        # ------------------------------------------------
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

        # ------------------------------------------------
        # CONFIRM PATCH
        # ------------------------------------------------
        if implement_mode and user_input.lower() == "confirm":

            print("\nApplying patch...\n")

            orchestrator.apply_patch()

            print("✅ Patch applied successfully.")

            implement_mode = False
            continue

        # ------------------------------------------------
        # TASK MODE
        # ------------------------------------------------
        if user_input.lower().startswith("task "):

            idea_text = user_input[5:]

            idea = IdeaParser.parse(idea_text)
            task = TaskProposalGenerator.generate(idea)

            print("\nSAPIANTA Task Proposal")
            print("----------------------")

            print(f"Title: {task['title']}")
            print(f"Description: {task['description']}")
            print(f"Priority: {task['priority']}")

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

        # ------------------------------------------------
        # NORMAL DISCUSSION
        # ------------------------------------------------
        response = engine.ask(user_input)

        print("\nSAPIANTA:", response)

        # ------------------------------------------------
        # AUTO IDEA DETECTION → DUAL PIPELINE
        # ------------------------------------------------
        if detect_idea(user_input):

            print("\n[AI] Development idea detected.")

            # 1️⃣ LEGACY (registry)
            dev_add_task.run([user_input])

            print("[AI] Task added to registry.")

            # 2️⃣ NEW (deterministic loop)
            try:
                from runtime.development.dev_autonomous_loop import DevAutonomousLoop

                loop = DevAutonomousLoop()
                task = DeterministicTaskBuilder.build(user_input)

                result = loop.submit_task(task)

                print("[AI] Autonomous loop submission:", result)

            except Exception as e:
                print(f"[AI] Autonomous submission failed: {e}")

            # 3️⃣ AUTO IMPLEMENT (existing)
            print("[AI] Starting automatic implementation...")

            try:
                orchestrator.run_auto(user_input)
            except Exception as e:
                print(f"[AI] Auto implementation failed: {e}")