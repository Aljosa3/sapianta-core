# PATH: sapianta_system/runtime/system/repository_intelligence.py

"""
SAPIANTA Repository Intelligence Engine

Provides repository-level architectural reasoning.

This module analyzes the architecture graph and detects:

- orphan modules
- missing tests
- layer violations
- capability gaps

This is the first repo-aware reasoning layer for the
SAPIANTA AI Software Factory.
"""

from pathlib import Path
from collections import defaultdict

from runtime.system.architecture_graph import ArchitectureGraph


class RepositoryIntelligence:

    def __init__(self, root):

        self.root = Path(root)

        self.graph_engine = ArchitectureGraph(self.root)

        self.graph = self.graph_engine.build_graph()

        self.runtime_graph = self.graph_engine.runtime_dependencies()

    # ---------------------------------------------------------
    # ORPHAN MODULE DETECTION
    # ---------------------------------------------------------

    def detect_orphan_modules(self):

        referenced = set()

        for deps in self.runtime_graph.values():
            for d in deps:
                referenced.add(d)

        orphans = []

        for module in self.runtime_graph:

            if module not in referenced:
                orphans.append(module)

        return sorted(orphans)

    # ---------------------------------------------------------
    # MISSING TEST DETECTION
    # ---------------------------------------------------------

    def detect_missing_tests(self):

        missing = []

        tests_dir = self.root / "tests"

        for module in self.runtime_graph:

            name = module.split(".")[-1]

            test_file = tests_dir / f"test_{name}.py"

            if not test_file.exists():
                missing.append(module)

        return sorted(missing)

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
    # CAPABILITY GAP DETECTION
    # ---------------------------------------------------------

    def detect_capability_gaps(self):

        clusters = defaultdict(list)

        for module in self.runtime_graph:

            parts = module.split(".")

            if len(parts) >= 3:

                capability = parts[2]

                clusters[capability].append(module)

        gaps = []

        for capability, modules in clusters.items():

            if len(modules) == 1:

                gaps.append(
                    {
                        "capability": capability,
                        "modules": modules,
                        "suggestion": f"expand capability '{capability}'",
                    }
                )

        return gaps

    # ---------------------------------------------------------
    # FULL ANALYSIS
    # ---------------------------------------------------------

    def analyze_repository(self):

        return {

            "orphans": self.detect_orphan_modules(),

            "missing_tests": self.detect_missing_tests(),

            "layer_violations": self.detect_layer_violations(),

            "capability_gaps": self.detect_capability_gaps(),
        }

    # ---------------------------------------------------------
    # PRINT REPORT
    # ---------------------------------------------------------

    def print_report(self):

        report = self.analyze_repository()

        print("\nSAPIANTA Repository Intelligence Report")
        print("---------------------------------------")

        print("\nOrphan Modules:")
        for m in report["orphans"]:
            print(" -", m)

        print("\nMissing Tests:")
        for m in report["missing_tests"]:
            print(" -", m)

        print("\nLayer Violations:")
        for v in report["layer_violations"]:
            print(" -", v["module"], "->", v["illegal_dependency"])

        print("\nCapability Gaps:")
        for g in report["capability_gaps"]:
            print(" -", g["capability"], ":", g["modules"])