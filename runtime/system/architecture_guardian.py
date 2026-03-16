# PATH: sapianta_system/runtime/system/architecture_guardian.py

"""
SAPIANTA Architecture Guardian

Architecture Guardian enforces structural integrity
of the runtime architecture.

Checks performed:

- cyclic imports
- dependency explosions
- forbidden imports
- layer violations

Acts as an architecture firewall for the SAPIANTA
Governed Autonomous Development system.
"""

from pathlib import Path
from collections import defaultdict

from runtime.system.architecture_graph import ArchitectureGraph


class ArchitectureGuardian:

    def __init__(self, root):

        self.root = Path(root)

        self.graph_engine = ArchitectureGraph(self.root)

        self.graph = self.graph_engine.build_graph()

        self.runtime_graph = self.graph_engine.runtime_dependencies()

    # ---------------------------------------------------------
    # CYCLIC IMPORT DETECTION
    # ---------------------------------------------------------

    def detect_cycles(self):

        visited = set()
        stack = set()
        cycles = []

        def visit(node):

            if node in stack:
                cycles.append(node)
                return

            if node in visited:
                return

            visited.add(node)
            stack.add(node)

            for dep in self.runtime_graph.get(node, []):
                visit(dep)

            stack.remove(node)

        for module in self.runtime_graph:
            visit(module)

        return cycles

    # ---------------------------------------------------------
    # DEPENDENCY EXPLOSION DETECTION
    # ---------------------------------------------------------

    def detect_dependency_explosion(self, threshold=20):

        explosion = []

        for module, deps in self.runtime_graph.items():

            if len(deps) > threshold:

                explosion.append(
                    {
                        "module": module,
                        "dependency_count": len(deps),
                    }
                )

        return explosion

    # ---------------------------------------------------------
    # FORBIDDEN IMPORT DETECTION
    # ---------------------------------------------------------

    def detect_forbidden_imports(self):

        forbidden_rules = {

            "runtime.system": [
                "runtime.analytics",
                "runtime.research",
                "runtime.evolution",
            ]

        }

        violations = []

        for module, deps in self.runtime_graph.items():

            for layer, forbidden in forbidden_rules.items():

                if module.startswith(layer):

                    for dep in deps:

                        for forbidden_layer in forbidden:

                            if dep.startswith(forbidden_layer):

                                violations.append(
                                    {
                                        "module": module,
                                        "forbidden_dependency": dep,
                                    }
                                )

        return violations

    # ---------------------------------------------------------
    # LAYER VIOLATION DETECTION
    # ---------------------------------------------------------

    def detect_layer_violations(self):

        violations = []

        for module, deps in self.runtime_graph.items():

            if module.startswith("runtime.system"):

                for dep in deps:

                    if dep.startswith("runtime.analytics") or dep.startswith(
                        "runtime.development"
                    ):

                        violations.append(
                            {
                                "module": module,
                                "illegal_dependency": dep,
                            }
                        )

        return violations

    # ---------------------------------------------------------
    # FULL ARCHITECTURE CHECK
    # ---------------------------------------------------------

    def run_guardian(self):

        return {

            "cycles": self.detect_cycles(),

            "dependency_explosions": self.detect_dependency_explosion(),

            "forbidden_imports": self.detect_forbidden_imports(),

            "layer_violations": self.detect_layer_violations(),
        }

    # ---------------------------------------------------------
    # PRINT REPORT
    # ---------------------------------------------------------

    def print_report(self):

        report = self.run_guardian()

        print("\nSAPIANTA Architecture Guardian Report")
        print("-------------------------------------")

        print("\nCycles:")
        for c in report["cycles"]:
            print(" -", c)

        print("\nDependency Explosions:")
        for e in report["dependency_explosions"]:
            print(" -", e["module"], "(", e["dependency_count"], ")")

        print("\nForbidden Imports:")
        for v in report["forbidden_imports"]:
            print(" -", v["module"], "->", v["forbidden_dependency"])

        print("\nLayer Violations:")
        for v in report["layer_violations"]:
            print(" -", v["module"], "->", v["illegal_dependency"])