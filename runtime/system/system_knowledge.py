"""
SAPIANTA System Knowledge Engine

Purpose
-------
Build a persistent self-model of the SAPIANTA system.

The module collects system structure information using:

- SystemMap
- ArchitectureGraph

and produces a structured knowledge representation
stored as system_state.json.

This enables:

- architecture awareness
- capability gap detection
- autonomous development reasoning
- Dev Orchestrator integration
"""

import json
import os
from datetime import datetime, UTC

from runtime.system.system_map import SystemMap
from runtime.system.architecture_graph import ArchitectureGraph


SYSTEM_STATE_PATH = os.path.join(
    os.path.dirname(__file__),
    "system_state.json"
)


class SystemKnowledge:

    def __init__(self):

        self.system_map = SystemMap()

        runtime_root = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")
        )

        self.arch_graph = ArchitectureGraph(runtime_root)

    # ---------------------------------------------------------
    # Core Knowledge Builder
    # ---------------------------------------------------------

    def build_knowledge(self):

        modules = self.system_map.discover_modules()

        capabilities = self.system_map.capabilities()

        missing = self.system_map.missing_capabilities()

        architecture = self.arch_graph.build_graph()

        core_systems = self.detect_core_systems(modules)

        layers = self.detect_layers(modules)

        system_state = {
            "generated_at": datetime.now(UTC).isoformat(),

            "modules": modules,

            "capabilities": capabilities,

            "missing_capabilities": missing,

            "architecture": architecture,

            "core_systems": core_systems,

            "layers": layers
        }

        return system_state

    # ---------------------------------------------------------
    # Core System Detection
    # ---------------------------------------------------------

    def detect_core_systems(self, modules):

        core_keywords = [
            "decision_spine",
            "experiment_engine",
            "experiment_runner",
            "evolution_engine",
            "strategy_optimizer",
            "policy_engine",
            "ledger_writer"
        ]

        detected = []

        for m in modules:

            for k in core_keywords:

                if k in m:
                    detected.append(m)

        return sorted(list(set(detected)))

    # ---------------------------------------------------------
    # Layer Detection
    # ---------------------------------------------------------

    def detect_layers(self, modules):

        layers = {
            "engine": [],
            "research": [],
            "evolution": [],
            "analytics": [],
            "development": [],
            "domains": [],
            "system": []
        }

        for m in modules:

            if "runtime.engine" in m:
                layers["engine"].append(m)

            elif "runtime.research" in m:
                layers["research"].append(m)

            elif "runtime.evolution" in m:
                layers["evolution"].append(m)

            elif "runtime.analytics" in m:
                layers["analytics"].append(m)

            elif "runtime.development" in m:
                layers["development"].append(m)

            elif "runtime.domains" in m:
                layers["domains"].append(m)

            elif "runtime.system" in m:
                layers["system"].append(m)

        return layers

    # ---------------------------------------------------------
    # Persistence
    # ---------------------------------------------------------

    def save(self, state):

        with open(SYSTEM_STATE_PATH, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2)

    # ---------------------------------------------------------
    # Load Knowledge
    # ---------------------------------------------------------

    @staticmethod
    def load():

        if not os.path.exists(SYSTEM_STATE_PATH):
            raise RuntimeError("system_state.json not found")

        with open(SYSTEM_STATE_PATH, encoding="utf-8") as f:
            return json.load(f)


# ---------------------------------------------------------
# CLI ENTRYPOINT
# ---------------------------------------------------------

def main():

    print("SAPIANTA System Knowledge Engine")
    print("--------------------------------")

    sk = SystemKnowledge()

    state = sk.build_knowledge()

    sk.save(state)

    print("System state generated.")
    print("Modules:", len(state["modules"]))
    print("Capabilities:", state["capabilities"])
    print("Missing:", state["missing_capabilities"])

    print("Saved to:")
    print(SYSTEM_STATE_PATH)


if __name__ == "__main__":
    main()