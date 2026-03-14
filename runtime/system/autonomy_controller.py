"""
SAPIANTA Autonomy Controller

Central orchestrator for autonomous system cycles.

Responsibilities
----------------
- monitor system capabilities
- launch research sessions
- evaluate results
- promote best strategies
- maintain system loop

This is the first step toward full system autonomy.
"""

import time

from runtime.evolution.research_supervisor import run_research_session


class AutonomyController:

    def __init__(self):

        self.cycle = 0
        self.active = True

    def observe_system(self):

        print("\nObserving system state...")

        capabilities = [
            "experiment_execution",
            "experiment_memory",
            "market_simulation",
            "portfolio_engine",
            "regime_analysis",
            "regime_detection",
            "strategy_memory",
            "strategy_optimization"
        ]

        print("Capabilities detected:")

        for cap in capabilities:
            print("-", cap)

        return True

    def launch_research(self):

        print("\nLaunching autonomous research session...\n")

        result = run_research_session()

        return result

    def evaluate_result(self, result):

        print("\nEvaluating research result...")

        if result is None:
            print("No result returned.")
            return False

        strategy = result.get("strategy")
        score = result.get("score")

        print("Best strategy:", strategy)
        print("Score:", score)

        return True

    def run_cycle(self):

        print("\n==============================")
        print("SAPIANTA AUTONOMY CYCLE", self.cycle)
        print("==============================")

        system_ready = self.observe_system()

        if not system_ready:
            print("System not ready.")
            return

        result = self.launch_research()

        self.evaluate_result(result)

        self.cycle += 1

    def run(self):

        print("\nSAPIANTA AUTONOMY CONTROLLER")
        print("----------------------------")

        while self.active:

            self.run_cycle()

            print("\nCycle completed.")
            print("Sleeping before next cycle...\n")

            time.sleep(5)


def main():

    controller = AutonomyController()
    controller.run()


if __name__ == "__main__":
    main()