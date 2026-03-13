"""
SAPIANTA System Map

Provides system self-awareness.

Tracks:
- modules
- capabilities
- architecture layers
"""

from pathlib import Path
from runtime.system.architecture_graph import ArchitectureGraph


PROJECT_ROOT = Path(__file__).resolve().parents[2]


class SystemMap:

    def __init__(self):

        self.runtime_path = PROJECT_ROOT / "runtime"

    # ---------------------------------------------------------
    # MODULE DISCOVERY
    # ---------------------------------------------------------

    def discover_modules(self):

        modules = []

        for p in self.runtime_path.rglob("*.py"):

            modules.append(str(p.relative_to(PROJECT_ROOT)))

        return sorted(modules)

    # ---------------------------------------------------------
    # CAPABILITY DETECTION
    # ---------------------------------------------------------

    def capabilities(self):

        modules = self.discover_modules()

        caps = []

        for m in modules:

            if "strategy_optimizer" in m:
                caps.append("strategy_optimization")

            if "experiment_runner" in m:
                caps.append("experiment_execution")

            if "market_simulator" in m:
                caps.append("market_simulation")

            if "regime_analyzer" in m:
                caps.append("regime_analysis")

            if "strategy_registry" in m:
                caps.append("strategy_memory")

            if "experiment_database" in m:
                caps.append("experiment_memory")

            # NEW CAPABILITIES
            if "portfolio_engine" in m:
                caps.append("portfolio_engine")

            if "regime_detector" in m:
                caps.append("regime_detection")

        return sorted(list(set(caps)))

    # ---------------------------------------------------------
    # MISSING CAPABILITIES
    # ---------------------------------------------------------

    def missing_capabilities(self):

        required = [
            "strategy_optimization",
            "experiment_execution",
            "market_simulation",
            "regime_analysis",
            "strategy_memory",
            "experiment_memory",
            "portfolio_engine",
            "regime_detection",
        ]

        existing = self.capabilities()

        return sorted([c for c in required if c not in existing])

    # ---------------------------------------------------------
    # ARCHITECTURE GRAPH
    # ---------------------------------------------------------

    def architecture(self):

        graph = ArchitectureGraph(self.runtime_path)

        return graph.build_graph()


# ---------------------------------------------------------
# TEST
# ---------------------------------------------------------

if __name__ == "__main__":

    sm = SystemMap()

    print("\nModules:")
    print(sm.discover_modules())

    print("\nCapabilities:")
    print(sm.capabilities())

    print("\nMissing:")
    print(sm.missing_capabilities())

    print("\nArchitecture:")

    arch = sm.architecture()

    for module, deps in arch.items():

        runtime_deps = [d for d in deps if d.startswith("runtime")]

        if runtime_deps:

            print("\n", module)

            for d in sorted(runtime_deps):

                print("   ->", d)