# PATH: sapianta_system/runtime/system/system_reflection_engine.py

"""
SAPIANTA System Reflection Engine

Combines architecture graph analysis, repository intelligence,
and architecture guardian checks into a unified system
self-awareness layer.

Capabilities:

- repository analysis
- architecture risk detection
- capability gap detection
- architecture health scoring
"""

from pathlib import Path

from runtime.system.architecture_graph import ArchitectureGraph
from runtime.system.repository_intelligence import RepositoryIntelligence
from runtime.system.architecture_guardian import ArchitectureGuardian


class SystemReflectionEngine:

    def __init__(self, root):

        self.root = Path(root)

        self.graph_engine = ArchitectureGraph(self.root)
        self.repo_intelligence = RepositoryIntelligence(self.root)
        self.guardian = ArchitectureGuardian(self.root)

    # ---------------------------------------------------------
    # SYSTEM ANALYSIS
    # ---------------------------------------------------------

    def analyze_system(self):

        repo_report = self.repo_intelligence.analyze_repository()
        guardian_report = self.guardian.run_guardian()

        report = {

            "orphans": repo_report.get("orphans", []),

            "missing_tests": repo_report.get("missing_tests", []),

            "capability_gaps": repo_report.get("capability_gaps", []),

            "cycles": guardian_report.get("cycles", []),

            "dependency_explosions": guardian_report.get(
                "dependency_explosions", []
            ),

            "forbidden_imports": guardian_report.get("forbidden_imports", []),

            "layer_violations": guardian_report.get("layer_violations", []),
        }

        report["health_score"] = self.calculate_health_score(report)

        return report

    # ---------------------------------------------------------
    # HEALTH SCORE
    # ---------------------------------------------------------

    def calculate_health_score(self, report):

        score = 100

        score -= len(report["missing_tests"]) * 0.5
        score -= len(report["orphans"]) * 0.2
        score -= len(report["capability_gaps"]) * 0.3
        score -= len(report["cycles"]) * 5
        score -= len(report["dependency_explosions"]) * 2
        score -= len(report["forbidden_imports"]) * 5
        score -= len(report["layer_violations"]) * 5

        if score < 0:
            score = 0

        return round(score, 2)

    # ---------------------------------------------------------
    # PRINT REPORT
    # ---------------------------------------------------------

    def print_report(self):

        report = self.analyze_system()

        print("\nSAPIANTA System Reflection Report")
        print("---------------------------------")

        print("\nArchitecture Health Score:", report["health_score"])

        print("\nMissing Tests:", len(report["missing_tests"]))
        print("Orphan Modules:", len(report["orphans"]))
        print("Capability Gaps:", len(report["capability_gaps"]))

        print("\nCycles:", len(report["cycles"]))
        print("Dependency Explosions:", len(report["dependency_explosions"]))
        print("Forbidden Imports:", len(report["forbidden_imports"]))
        print("Layer Violations:", len(report["layer_violations"]))