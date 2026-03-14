"""
SAPIANTA Development Orchestrator

Purpose
-------
Coordinates the Governed Autonomous Development (GAD) pipeline.

The orchestrator supports three development modes:

1. Strategic Mode
   Human provides strategic direction.

2. Autonomous Mode
   System detects capability gaps and proposes development tasks.

3. Implementation Mode
   Triggered from sapianta discuss.
   Generates a patch proposal instead of executing code generation.

Pipeline

Strategic Direction / Capability Gap / Discussion Request
        ↓
Architecture Proposal
        ↓
Artifact Registry (hash)
        ↓
Promotion Gate
        ↓
Mutation Guard
        ↓
Mutation Validation
        ↓
Human Approval (if required)
        ↓
Code Generation
"""

from datetime import datetime, UTC

from runtime.development.mutation_validator import MutationValidator
from runtime.development.code_generator import CodeGenerator
from runtime.development.mutation_guard import MutationGuard
from runtime.system.system_knowledge import SystemKnowledge
from runtime.development.capability_gap_detector import CapabilityGapDetector
from runtime.system.capability_planner import CapabilityPlanner
from runtime.development.architecture_agent import ArchitectureAgent

from runtime.governance.promotion_gate import classify_change, requires_approval
from runtime.artifacts.artifact_registry import register_artifact


class DevelopmentOrchestrator:

    """
    Coordinates governed development of the SAPIANTA system.
    """

    # ------------------------------------------------
    # Immutable core protection
    # ------------------------------------------------

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

        self.architecture_agent = ArchitectureAgent(self.system_knowledge)

    # ------------------------------------------------
    # Architecture proposal
    # ------------------------------------------------

    def propose_architecture(self, strategic_direction: str):

        return self.architecture_agent.propose(strategic_direction)

    # ------------------------------------------------
    # Autonomous capability proposal
    # ------------------------------------------------

    def propose_from_capability_gaps(self):

        proposals = self.gap_detector.detect()

        if not proposals:
            return None

        proposals = sorted(
            proposals,
            key=lambda p: p["capability"]
        )

        capability = proposals[0]["capability"]

        ordered_capabilities = self.capability_planner.plan(capability)

        target_capability = ordered_capabilities[-1]

        blueprint = self.architecture_agent.design_capability(
            target_capability
        )

        return {
            "description": blueprint["description"],
            "files_to_create": blueprint["modules"],
            "files_to_modify": []
        }

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

        print("PATCH PROPOSAL")
        print("----------------")

        print("\nDescription:")
        print(patch["description"])

        print("\nAffected files:")

        for f in patch["files"]:
            print("-", f)

        return patch

    # ------------------------------------------------
    # Strategic development pipeline
    # ------------------------------------------------

    def run(self, strategic_direction: str):

        print("\nStrategic direction received:")
        print(strategic_direction)

        print("\nGenerating architecture proposal...")

        architecture = self.propose_architecture(strategic_direction)

        self._execute_pipeline(architecture)

    # ------------------------------------------------
    # Autonomous development pipeline
    # ------------------------------------------------

    def run_autonomous(self):

        print("\nRunning autonomous development analysis...")

        state = self.system_knowledge.build_knowledge()
        self.system_knowledge.save(state)

        architecture = self.propose_from_capability_gaps()

        if not architecture:

            print("\nNo capability gaps detected.")
            return

        print("\nAutonomous proposal generated:")
        print(architecture["description"])

        self._execute_pipeline(architecture)

    # ------------------------------------------------
    # Execute pipeline
    # ------------------------------------------------

    def _execute_pipeline(self, architecture):

        implementation_plan = self.build_implementation_plan(architecture)

        if not implementation_plan:
            print("\nNo implementation required.")
            return

        self._check_core_modification(implementation_plan)

        # ------------------------------------------------
        # Artifact Registry
        # ------------------------------------------------

        print("\nRegistering architecture artifact...")

        artifact = register_artifact(
            artifact_type="architecture_proposal",
            domain_id="core",
            artifact_location="runtime/development/dev_orchestrator",
            producer="development_orchestrator",
            metadata=architecture
        )

        print("Artifact registered:", artifact["artifact_id"])

        # ------------------------------------------------
        # Promotion Gate
        # ------------------------------------------------

        print("\nRunning Promotion Gate...")

        change_level = classify_change(implementation_plan)

        print("Change classification:", change_level)

        approval_required = requires_approval(change_level)

        # ------------------------------------------------
        # Mutation Guard
        # ------------------------------------------------

        print("\nRunning Mutation Guard...")

        self.mutation_guard.validate_patch(implementation_plan)

        print("Mutation Guard passed.")

        print("\nProposed file changes:")

        for p in implementation_plan:
            print("-", p)

        # ------------------------------------------------
        # Mutation validation
        # ------------------------------------------------

        print("\nRunning mutation validation...")

        validation = self.validator.validate_changes(implementation_plan)

        rejected = False

        for r in validation:

            print(r)

            if r["status"] == "REJECTED":
                rejected = True

        if rejected:

            print("\n❌ Mutation validation failed.")
            print("Changes violate governance policy.")
            return

        print("\n✅ Mutation validation passed.")

        # ------------------------------------------------
        # Conditional human approval
        # ------------------------------------------------

        if approval_required:

            approval = input("\nApprove implementation plan? (y/n): ")

            if approval.lower() != "y":

                print("\nDevelopment cancelled.")
                return

        # ------------------------------------------------
        # Code generation
        # ------------------------------------------------

        print("\nImplementation approved.")

        print("\nGenerating code...")

        for file_path in architecture["files_to_create"]:

            self.code_generator.generate_module(
                file_path,
                architecture["description"]
            )

        print("\n✅ Code generation completed.")

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

    if mode == "autonomous":

        orchestrator.run_autonomous()

    elif mode == "implement":

        context = input("\nDiscussion context:\n")

        orchestrator.run_implementation(context)

    else:

        strategic_direction = input("\nEnter strategic direction:\n")

        orchestrator.run(strategic_direction)