"""
SAPIANTA Development Orchestrator

Purpose
-------
Coordinates the Governed Autonomous Development (GAD) pipeline.

The orchestrator supports two development modes:

1. Strategic Mode
   Human provides strategic direction.

2. Autonomous Mode
   System detects capability gaps and proposes development tasks.

Pipeline

Strategic Direction / Capability Gap
        ↓
Architecture Proposal
        ↓
Implementation Plan
        ↓
Mutation Validation
        ↓
Human Approval
        ↓
Code Generation
"""

from datetime import datetime, UTC

from runtime.development.mutation_validator import MutationValidator
from runtime.development.code_generator import CodeGenerator
from runtime.system.system_knowledge import SystemKnowledge
from runtime.development.capability_gap_detector import CapabilityGapDetector


class DevelopmentOrchestrator:

    def __init__(self):

        self.validator = MutationValidator()
        self.code_generator = CodeGenerator()

        # new components
        self.system_knowledge = SystemKnowledge()
        self.gap_detector = CapabilityGapDetector()

    # ------------------------------------------------
    # Architecture proposal (strategic mode)
    # ------------------------------------------------

    def propose_architecture(self, strategic_direction: str):

        """
        Converts strategic direction into an architecture proposal.

        This is currently a stub and will later be replaced by
        the Architecture Agent.
        """

        if "market regime" in strategic_direction.lower():

            return {
                "description": "Add Market Regime Engine",
                "files_to_create": [
                    "runtime/market/regime_engine.py"
                ],
                "files_to_modify": []
            }

        return {
            "description": "No proposal generated",
            "files_to_create": [],
            "files_to_modify": []
        }

    # ------------------------------------------------
    # Autonomous capability proposal
    # ------------------------------------------------

    def propose_from_capability_gaps(self):

        proposals = self.gap_detector.detect()

        if not proposals:
            return None

        p = proposals[0]  # first proposal for now

        mapping = {

            "portfolio_engine": "runtime/portfolio/portfolio_engine.py",

            "regime_detection": "runtime/market/regime_detector.py",

            "risk_engine": "runtime/risk/risk_engine.py"
        }

        file_path = mapping.get(
            p["capability"],
            f"runtime/development/{p['capability']}.py"
        )

        return {
            "description": f"Add capability: {p['capability']}",
            "files_to_create": [file_path],
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

        print("\nProposed file changes:")

        for p in implementation_plan:
            print("-", p)

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

        approval = input("\nApprove implementation plan? (y/n): ")

        if approval.lower() != "y":

            print("\nDevelopment cancelled.")
            return

        print("\nImplementation approved.")

        print("\nGenerating code...")

        for file_path in architecture["files_to_create"]:

            self.code_generator.generate_module(
                file_path,
                architecture["description"]
            )

        print("\n✅ Code generation completed.")


# ------------------------------------------------
# Manual test
# ------------------------------------------------

if __name__ == "__main__":

    orchestrator = DevelopmentOrchestrator()

    mode = input("Mode (strategic / autonomous): ")

    if mode == "autonomous":

        orchestrator.run_autonomous()

    else:

        strategic_direction = input("\nEnter strategic direction:\n")

        orchestrator.run(strategic_direction)