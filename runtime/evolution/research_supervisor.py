"""
SAPIANTA Research Supervisor

Purpose
-------
Supervises autonomous research cycles without requiring
manual execution of each underlying module.

The supervisor coordinates:

- generation_manager
- autonomous_cycle
- evolution_log
- optional portfolio capability awareness

It is the first step from isolated research utilities
toward a continuously orchestrated autonomous research system.
"""

from datetime import datetime, UTC

from runtime.evolution.generation_manager import GenerationManager
from runtime.system.evolution_log import EvolutionLog
from runtime.system.system_knowledge import SystemKnowledge


class ResearchSupervisor:

    def __init__(self, population_size=20, survivors=5, generations=10):

        self.population_size = population_size
        self.survivors = survivors
        self.generations = generations

        self.manager = GenerationManager(
            population_size=population_size,
            survivors=survivors
        )

        self.evolution_log = EvolutionLog()
        self.system_knowledge = SystemKnowledge()

    # ---------------------------------------------------------
    # CAPABILITY CHECK
    # ---------------------------------------------------------

    def system_ready(self):

        state = self.system_knowledge.build_knowledge()
        self.system_knowledge.save(state)

        capabilities = state.get("capabilities", [])

        required = [
            "experiment_execution",
            "strategy_optimization",
            "strategy_memory"
        ]

        missing = [c for c in required if c not in capabilities]

        return {
            "ready": len(missing) == 0,
            "missing": missing,
            "capabilities": capabilities
        }

    # ---------------------------------------------------------
    # RUN SUPERVISED RESEARCH SESSION
    # ---------------------------------------------------------

    def run_session(self):

        print("\nSAPIANTA Research Supervisor")
        print("----------------------------")

        readiness = self.system_ready()

        if not readiness["ready"]:
            print("\nSystem not ready for autonomous research.")
            print("Missing capabilities:", readiness["missing"])

            self.evolution_log.record(
                "research_supervisor_blocked",
                {
                    "timestamp": datetime.now(UTC).isoformat(),
                    "missing_capabilities": readiness["missing"]
                }
            )
            return None

        print("\nSystem readiness check passed.")
        print("Capabilities:")

        for c in readiness["capabilities"]:
            print("-", c)

        print("\nLaunching supervised evolutionary search...")

        best_strategy = self.manager.evolve(generations=self.generations)

        strategy_name = getattr(best_strategy, "__name__", str(best_strategy))

        result = {
            "timestamp": datetime.now(UTC).isoformat(),
            "population_size": self.population_size,
            "survivors": self.survivors,
            "generations": self.generations,
            "best_strategy": strategy_name,
        }

        self.evolution_log.record(
            "research_session_completed",
            result
        )

        print("\nResearch session completed.")
        print("Best strategy:", strategy_name)

        return result

    # ---------------------------------------------------------
    # CONTINUOUS LOOP
    # ---------------------------------------------------------

    def run_continuous(self, sessions=3):

        print("\nSAPIANTA Continuous Research Supervisor")
        print("---------------------------------------")

        history = []

        for i in range(sessions):

            print(f"\n=== Research Session {i + 1} / {sessions} ===")

            result = self.run_session()

            if result is None:
                print("\nSupervisor stopped.")
                break

            history.append(result)

        self.evolution_log.record(
            "continuous_research_completed",
            {
                "timestamp": datetime.now(UTC).isoformat(),
                "sessions_completed": len(history),
                "history": history
            }
        )

        return history


# ---------------------------------------------------------
# PUBLIC API FOR AUTONOMY CONTROLLER
# ---------------------------------------------------------

def run_research_session():

    supervisor = ResearchSupervisor(
        population_size=20,
        survivors=5,
        generations=10
    )

    result = supervisor.run_session()

    if result is None:
        return None

    return {
        "strategy": result["best_strategy"],
        "score": None
    }


# ---------------------------------------------------------
# CLI ENTRYPOINT
# ---------------------------------------------------------

def main():

    supervisor = ResearchSupervisor(
        population_size=20,
        survivors=5,
        generations=10
    )

    supervisor.run_session()


if __name__ == "__main__":

    main()