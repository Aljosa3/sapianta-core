"""
SAPIANTA Development Orchestrator

Purpose
-------
Coordinates the Governed Autonomous Development (GAD) pipeline.

The orchestrator receives strategic direction from the CLI
and manages the development workflow while enforcing governance rules.

Pipeline

Strategic Direction
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

from runtime.development.mutation_validator import MutationValidator
from runtime.development.code_generator import CodeGenerator


class DevelopmentOrchestrator:

    def __init__(self):

        self.validator = MutationValidator()
        self.code_generator = CodeGenerator()

    # ------------------------------------------------
    # Architecture proposal (temporary stub)
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
    # Run development pipeline
    # ------------------------------------------------

    def run(self, strategic_direction: str):

        print("\nStrategic direction received:")
        print(strategic_direction)

        print("\nGenerating architecture proposal...")

        architecture = self.propose_architecture(strategic_direction)

        print("\nArchitecture proposal:")
        print(architecture["description"])

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

        # ------------------------------------------------
        # Code generation step
        # ------------------------------------------------

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

    strategic_direction = input("Enter strategic direction:\n")

    orchestrator.run(strategic_direction)