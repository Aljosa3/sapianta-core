"""
SAPIANTA Development Orchestrator

Purpose
-------
Coordinates the Governed Autonomous Development (GAD) pipeline.
"""

from datetime import datetime, UTC
from pathlib import Path

from runtime.development.mutation_validator import MutationValidator
from runtime.development.code_generator import CodeGenerator
from runtime.development.mutation_guard import MutationGuard
from runtime.system.system_knowledge import SystemKnowledge
from runtime.system.repository_context import RepositoryContextBuilder
from runtime.development.capability_gap_detector import CapabilityGapDetector
from runtime.system.capability_planner import CapabilityPlanner
from runtime.development.architecture_agent import ArchitectureAgent

from runtime.governance.promotion_gate import classify_change, requires_approval
from runtime.artifacts.artifact_registry import register_artifact


class DevelopmentOrchestrator:

    """
    Coordinates governed development of the SAPIANTA system.
    """

    FORBIDDEN_PATHS = [
        "runtime/governance",
        "runtime/system",
        "runtime/ledger",
        "runtime/safety",
        "runtime/layer2",
    ]

    ALLOWED_PATHS = [
        "runtime/research",
        "runtime/strategies",
        "runtime/memory",
        "runtime/experiments",
        "runtime/analytics",
        "sapianta-domain-",
        "runtime/development",
    ]

    def __init__(self):

        self.validator = MutationValidator()
        self.code_generator = CodeGenerator()
        self.mutation_guard = MutationGuard()

        self.system_knowledge = SystemKnowledge()

        self.gap_detector = CapabilityGapDetector()
        self.capability_planner = CapabilityPlanner()

        self.repo_context = RepositoryContextBuilder()

        self.architecture_agent = ArchitectureAgent(self.system_knowledge)

        # store last patch proposal
        self.current_patch = None

    # ------------------------------------------------
    # Architecture proposal (repository-aware)
    # ------------------------------------------------

    def propose_architecture(self, strategic_direction: str):

        repo_context = self.repo_context.summarize(
            self.ALLOWED_PATHS,
            self.FORBIDDEN_PATHS
        )

        enriched_prompt = f"""
SYSTEM CONTEXT
--------------
{repo_context}

DEVELOPMENT REQUEST
-------------------
{strategic_direction}
"""

        return self.architecture_agent.propose(enriched_prompt)

    # ------------------------------------------------
    # IMPLEMENT MODE
    # ------------------------------------------------

    def run_implementation(self, discussion_context: str):

        print("\nIMPLEMENT MODE activated.")
        print("\nAnalyzing discussion context...")

        architecture = self.propose_architecture(discussion_context)

        if not architecture["files_to_create"] and not architecture["files_to_modify"]:
            print("\nNo implementation proposal generated.")
            return None

        implementation_plan = self.build_implementation_plan(architecture)

        self._check_core_modification(implementation_plan)

        print("\nRunning Promotion Gate...")

        change_level = classify_change(implementation_plan)

        print("Change classification:", change_level)

        if requires_approval(change_level):

            approval = input("\nApprove implementation plan? (y/n): ")

            if approval.lower() != "y":

                print("\nDevelopment cancelled.")
                return None

        print("\nRunning Mutation Guard...")

        self.mutation_guard.validate_patch(implementation_plan)

        print("Mutation Guard passed.")

        print("\nGenerating PATCH PROPOSAL...\n")

        patch = {
            "description": architecture["description"],
            "files": implementation_plan,
            "generated_at": datetime.now(UTC).isoformat()
        }

        self.current_patch = patch

        print("PATCH PROPOSAL")
        print("----------------")

        print("\nDescription:")
        print(patch["description"])

        print("\nAffected files:")

        for f in patch["files"]:
            print("-", f)

        return patch

    # ------------------------------------------------
    # APPLY PATCH
    # ------------------------------------------------

    def apply_patch(self):

        if not self.current_patch:

            print("No patch proposal available.")
            return

        print("Applying patch...\n")

        for file_path in self.current_patch["files"]:

            path = Path(file_path)

            path.parent.mkdir(parents=True, exist_ok=True)

            print("Generating module:", file_path)

            self.code_generator.generate_module(
                file_path,
                self.current_patch["description"]
            )

        print("\nPatch application completed.")

        self.current_patch = None

    # ------------------------------------------------
    # Build implementation plan
    # ------------------------------------------------

    def build_implementation_plan(self, architecture_proposal):

        plan = []

        for f in architecture_proposal["files_to_create"]:
            plan.append(f)

        for f in architecture_proposal["files_to_modify"]:
            plan.append(f)

        return plan

    # ------------------------------------------------
    # Core mutation protection
    # ------------------------------------------------

    def _check_core_modification(self, file_list):

        for path in file_list:

            for forbidden in self.FORBIDDEN_PATHS:

                if path.startswith(forbidden):

                    raise Exception(
                        f"Mutation forbidden: {path} is immutable core."
                    )


# ------------------------------------------------
# Manual test
# ------------------------------------------------

if __name__ == "__main__":

    orchestrator = DevelopmentOrchestrator()

    mode = input("Mode (strategic / autonomous / implement): ")

    if mode == "implement":

        context = input("\nDiscussion context:\n")

        orchestrator.run_implementation(context)

        confirm = input("\nApply patch? (y/n): ")

        if confirm == "y":

            orchestrator.apply_patch()