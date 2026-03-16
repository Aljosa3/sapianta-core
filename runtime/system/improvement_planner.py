"""
SAPIANTA Improvement Planner

Generates development improvement tasks based on
system reflection diagnostics.

This is the first step toward autonomous development planning.
"""

from runtime.system.system_reflection_engine import SystemReflectionEngine


class ImprovementPlanner:

    def __init__(self, repo_path="."):
        self.repo_path = repo_path
        self.engine = SystemReflectionEngine(repo_path)

    def analyze(self):
        return self.engine.analyze()

    def generate_tasks(self):

        report = self.analyze()

        tasks = []

        missing_tests = len(report["missing_tests"])
        orphans = len(report["orphans"])
        capability_gaps = len(report["capability_gaps"])
        cycles = len(report["cycles"])
        dependency_explosions = len(report["dependency_explosions"])
        forbidden_imports = len(report["forbidden_imports"])
        layer_violations = len(report["layer_violations"])

        # Missing tests
        if missing_tests > 0:
            tasks.append(
                f"Generate tests for {missing_tests} modules lacking test coverage"
            )

        # Orphan modules
        if orphans > 0:
            tasks.append(
                f"Review {orphans} orphan modules for integration or removal"
            )

        # Capability gaps
        if capability_gaps > 0:
            tasks.append(
                f"Investigate {capability_gaps} potential capability gaps in system architecture"
            )

        # Architecture violations
        if cycles > 0:
            tasks.append(
                f"Resolve {cycles} dependency cycles"
            )

        if layer_violations > 0:
            tasks.append(
                f"Fix {layer_violations} architecture layer violations"
            )

        if forbidden_imports > 0:
            tasks.append(
                f"Remove {forbidden_imports} forbidden imports"
            )

        if dependency_explosions > 0:
            tasks.append(
                f"Reduce {dependency_explosions} dependency explosions"
            )

        return tasks

    def print_plan(self):

        tasks = self.generate_tasks()

        print()
        print("SAPIANTA Improvement Plan")
        print("-------------------------")
        print()

        if not tasks:
            print("System healthy — no improvement tasks detected.")
            return

        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")