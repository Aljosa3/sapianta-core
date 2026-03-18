"""
SAPIANTA Development Orchestrator

Purpose
-------
Coordinates the Governed Autonomous Development (GAD) pipeline.
"""

from datetime import datetime, UTC
from pathlib import Path
import os

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

from runtime.development.artifact_outcome_tracker import ArtifactOutcomeTracker
from runtime.development.artifact_evaluator import ArtifactEvaluator
from runtime.development.strategy_selector import StrategySelector

from runtime.development.test_runner import TestRunner
from runtime.development.auto_fix_engine import AutoFixEngine


# ------------------------------------------------
# EXECUTION CONTEXT DETECTOR
# ------------------------------------------------

def is_running_under_pytest():
    return "PYTEST_CURRENT_TEST" in os.environ


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

        # tracking
        self.outcome_tracker = ArtifactOutcomeTracker()

        # evaluation
        self.evaluator = ArtifactEvaluator()

        # strategy
        self.strategy_selector = StrategySelector()

        # testing + auto-fix
        self.test_runner = TestRunner()
        self.auto_fix_engine = AutoFixEngine()

        self.current_patch = None

    # ------------------------------------------------
    # Architecture proposal
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

            print("\n⚠️ No architecture proposal generated.")
            print("➡️ Activating fallback architecture generator...\n")

            safe_name = discussion_context.lower().replace(" ", "_")[:40]
            fallback_file = f"runtime/development/generated/{safe_name}.py"

            architecture = {
                "description": f"Auto-generated fallback for: {discussion_context}",
                "files_to_create": [fallback_file],
                "files_to_modify": []
            }

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

        patch = {
            "description": architecture["description"],
            "files": implementation_plan,
            "generated_at": datetime.now(UTC).isoformat()
        }

        self.current_patch = patch

        return patch

    # ------------------------------------------------
    # AUTO IMPLEMENTATION
    # ------------------------------------------------

    def run_auto(self, discussion_context=None):

        print("\nAUTO DEVELOPMENT MODE")

        if not discussion_context:
            discussion_context = "Implement generic system improvement"

        artifact_id = None

        try:

            architecture = self.propose_architecture(discussion_context)

            if not architecture["files_to_create"] and not architecture["files_to_modify"]:
                return self.run_implementation(discussion_context)

            implementation_plan = self.build_implementation_plan(architecture)

            self._check_core_modification(implementation_plan)

            print("Running Mutation Guard...")
            self.mutation_guard.validate_patch(implementation_plan)
            print("Mutation Guard passed.")

            print("\nGenerating modules...\n")

            for file_path in implementation_plan:

                path = Path(file_path)
                path.parent.mkdir(parents=True, exist_ok=True)

                self.code_generator.generate_module(
                    file_path,
                    architecture["description"]
                )

            # ------------------------------------------------
            # TEST + AUTO-FIX LOOP (SAFE)
            # ------------------------------------------------

            if not is_running_under_pytest():

                print("\nRunning test suite...")

                test_result = self.test_runner.run_tests()

                print("Test success:", test_result.success)

                if not test_result.success:

                    print("\nTests failed → attempting auto-fix...")

                    fix = self.auto_fix_engine.attempt_fix({
                        "success": test_result.success,
                        "error": test_result.raw_error,
                        "output": test_result.raw_output
                    })

                    print("Fix result:", fix)

            # ------------------------------------------------
            # ARTIFACT + EVALUATION
            # ------------------------------------------------

            artifact = {
                "description": architecture["description"],
                "files": implementation_plan,
                "generated_at": datetime.now(UTC).isoformat()
            }

            evaluation = self.evaluator.evaluate(artifact)
            strategy = self.strategy_selector.select(evaluation)

            artifact_id = register_artifact(
                artifact_type="auto_development_patch",
                domain_id="development",
                artifact_location="runtime/development",
                producer="DevelopmentOrchestrator",
                metadata={
                    "artifact": artifact,
                    "mode": "auto",
                    "files": implementation_plan,
                    "timestamp": artifact["generated_at"],
                    "evaluation": evaluation,
                    "strategy": strategy
                }
            )

            self.outcome_tracker.record_outcome(
                artifact_id=artifact_id,
                status="success"
            )

            print("AUTO IMPLEMENTATION COMPLETED")

            return artifact

        except Exception as e:

            print(f"\n[ERROR] AUTO DEVELOPMENT FAILED: {e}")

            if artifact_id:
                self.outcome_tracker.record_outcome(
                    artifact_id=artifact_id,
                    status="failed",
                    error=str(e)
                )

            return None

    # ------------------------------------------------
    # APPLY PATCH
    # ------------------------------------------------

    def apply_patch(self):

        if not self.current_patch:
            return

        for file_path in self.current_patch["files"]:

            path = Path(file_path)
            path.parent.mkdir(parents=True, exist_ok=True)

            self.code_generator.generate_module(
                file_path,
                self.current_patch["description"]
            )

        self.current_patch = None

    # ------------------------------------------------
    # Build implementation plan
    # ------------------------------------------------

    def build_implementation_plan(self, architecture_proposal):

        return (
            architecture_proposal["files_to_create"] +
            architecture_proposal["files_to_modify"]
        )

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