"""
SAPIANTA Mutation Validator

Purpose
-------
Validates whether proposed repository mutations are allowed
according to the SAPIANTA Mutation Map governance policy.

Used by:
- GAD CLI
- Development Orchestrator
- Governance Gate

Safety guarantees:
- blocks forbidden repository paths
- enforces mutation class rules
- protects L0/L1 architecture
"""

from pathlib import Path


class MutationValidator:

    def __init__(self):

        # Hard safety rules (first layer protection)

        self.forbidden_paths = [
            "governance/constitution",
            "governance/contracts",
        ]

        # Layer mutation permissions

        self.layer_rules = {

            "L0": "IMMUTABLE",
            "L1": "IMMUTABLE",
            "L2": "RESTRICTED",
            "L3": "GOVERNED",
            "L4": "EVOLVABLE",
            "runtime": "EVOLVABLE",
        }

    # --------------------------------------------------------
    # Path safety check
    # --------------------------------------------------------

    def is_forbidden_path(self, file_path: str) -> bool:

        for forbidden in self.forbidden_paths:

            if file_path.startswith(forbidden):
                return True

        return False

    # --------------------------------------------------------
    # Layer detection
    # --------------------------------------------------------

    def detect_layer(self, file_path: str) -> str:

        """
        Detect which architectural layer a file belongs to.
        """

        if file_path.startswith("governance/constitution"):
            return "L0"

        if file_path.startswith("governance/contracts"):
            return "L1"

        if file_path.startswith("runtime/decision"):
            return "L2"

        if file_path.startswith("governance/"):
            return "L3"

        if file_path.startswith("runtime/research"):
            return "L4"

        if file_path.startswith("runtime/"):
            return "runtime"

        return "unknown"

    # --------------------------------------------------------
    # Mutation permission check
    # --------------------------------------------------------

    def check_mutation_permission(self, layer: str) -> bool:

        rule = self.layer_rules.get(layer)

        if rule == "IMMUTABLE":
            return False

        return True

    # --------------------------------------------------------
    # Main validation method
    # --------------------------------------------------------

    def validate_changes(self, proposed_changes):

        """
        proposed_changes = list of file paths
        """

        results = []

        for file_path in proposed_changes:

            # Normalize path
            file_path = file_path.replace("\\", "/")

            # Forbidden path check

            if self.is_forbidden_path(file_path):

                results.append({
                    "file": file_path,
                    "status": "REJECTED",
                    "reason": "forbidden_path"
                })

                continue

            # Layer detection

            layer = self.detect_layer(file_path)

            # Permission check

            allowed = self.check_mutation_permission(layer)

            if not allowed:

                results.append({
                    "file": file_path,
                    "status": "REJECTED",
                    "reason": f"{layer}_immutable"
                })

                continue

            results.append({
                "file": file_path,
                "status": "ALLOWED",
                "layer": layer
            })

        return results


# ------------------------------------------------------------
# Example usage
# ------------------------------------------------------------

if __name__ == "__main__":

    validator = MutationValidator()

    test_changes = [
        "runtime/market/regime_engine.py",
        "governance/contracts/SAPIANTA_STRATEGY_ARTIFACT_SCHEMA_v1.0.md",
        "runtime/research/new_experiment.py"
    ]

    result = validator.validate_changes(test_changes)

    for r in result:
        print(r)