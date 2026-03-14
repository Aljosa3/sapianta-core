"""
SAPIANTA Autonomous Research Cycle

Coordinates continuous strategy evolution.

Pipeline:

Strategy Optimizer
    ↓
Experiment Runner
    ↓
Evaluation
    ↓
Evolution Log
"""

from datetime import datetime, UTC

from runtime.research.strategy_optimizer import optimize_strategies
from runtime.system.evolution_log import EvolutionLog


class AutonomousResearchCycle:

    def __init__(self):

        self.evolution_log = EvolutionLog()

    # ---------------------------------------------------------
    # RUN ONE EVOLUTION STEP
    # ---------------------------------------------------------

    def run_cycle(self):

        print("\nSAPIANTA Autonomous Research Cycle")
        print("----------------------------------")

        # -------------------------------------------------
        # Run strategy optimizer
        # -------------------------------------------------

        best_strategy = optimize_strategies(20)

        print("\nBest strategy discovered:")
        print(best_strategy.__name__)

        # -------------------------------------------------
        # Record evolution event
        # -------------------------------------------------

        self.evolution_log.record(
            "strategy_generation_completed",
            {
                "timestamp": datetime.now(UTC).isoformat(),
                "best_strategy": best_strategy.__name__,
            }
        )

        return best_strategy


# ---------------------------------------------------------
# TEST ENTRYPOINT
# ---------------------------------------------------------

if __name__ == "__main__":

    cycle = AutonomousResearchCycle()

    strategy = cycle.run_cycle()

    print("\nCycle completed.")
    print("Best strategy:", strategy.__name__)