"""
SAPIANTA Architecture Agent

Purpose
-------
Generates architecture blueprints and architecture proposals
for new system capabilities.

The agent supports two reasoning modes:

1. Capability Mode
   Used by autonomous development when a capability gap is detected.

2. Context Mode
   Used by sapianta discuss when human strategic direction
   is converted into an architecture proposal.

Guardrails
----------
ArchitectureAgent never proposes mutations in immutable
core layers of the SAPIANTA system.

Pipeline

Capability Gap / Strategic Context
        ↓
Architecture Reasoning
        ↓
Module Design
        ↓
Development Blueprint
"""

from datetime import datetime, UTC


class ArchitectureAgent:

    # ---------------------------------------------------------
    # Guardrails
    # ---------------------------------------------------------

    FORBIDDEN_PATHS = [
        "runtime/system",
        "runtime/governance",
        "runtime/ledger",
        "runtime/safety",
        "runtime/layer2",
    ]

    ALLOWED_PREFIXES = [
        "runtime/research",
        "runtime/strategies",
        "runtime/memory",
        "runtime/experiments",
        "runtime/analytics",
        "runtime/development",
        "runtime/portfolio",
        "runtime/market",
        "runtime/risk",
        "sapianta-domain-"
    ]

    def __init__(self, system_knowledge=None):

        # optional dependency
        self.system_knowledge = system_knowledge

    # ---------------------------------------------------------
    # Guardrail filtering
    # ---------------------------------------------------------

    def _filter_paths(self, paths):

        filtered = []

        for path in paths:

            forbidden = False

            for fp in self.FORBIDDEN_PATHS:

                if path.startswith(fp):
                    forbidden = True
                    break

            if forbidden:
                continue

            allowed = False

            for ap in self.ALLOWED_PREFIXES:

                if path.startswith(ap):
                    allowed = True
                    break

            if allowed:
                filtered.append(path)

        return filtered

    # ---------------------------------------------------------
    # CONTEXT MODE (from sapianta discuss)
    # ---------------------------------------------------------

    def propose(self, context: str):

        """
        Generate architecture proposal from discussion context.
        """

        context_lower = context.lower()

        # optional system introspection
        if self.system_knowledge:
            _ = self.system_knowledge.build_knowledge()

        if "memory" in context_lower:

            proposal = {
                "description": "Add strategy memory persistence",
                "files_to_create": [
                    "runtime/memory/strategy_memory.py"
                ],
                "files_to_modify": [],
                "reason": "Strategies require persistent memory."
            }

        elif "market regime" in context_lower or "regime detection" in context_lower:

            proposal = {
                "description": "Add market regime detection engine",
                "files_to_create": [
                    "runtime/market/regime_engine.py"
                ],
                "files_to_modify": [],
                "reason": "Strategies require regime awareness."
            }

        elif "risk" in context_lower:

            proposal = {
                "description": "Add portfolio risk engine",
                "files_to_create": [
                    "runtime/risk/risk_engine.py"
                ],
                "files_to_modify": [],
                "reason": "Risk management capability missing."
            }

        elif "portfolio" in context_lower:

            proposal = {
                "description": "Add portfolio allocation engine",
                "files_to_create": [
                    "runtime/portfolio/portfolio_engine.py"
                ],
                "files_to_modify": [],
                "reason": "Portfolio allocation capability missing."
            }

        else:

            proposal = {
                "description": "No architecture change proposed",
                "files_to_create": [],
                "files_to_modify": [],
                "reason": "Context not recognized by ArchitectureAgent"
            }

        # apply guardrails
        proposal["files_to_create"] = self._filter_paths(
            proposal["files_to_create"]
        )

        proposal["files_to_modify"] = self._filter_paths(
            proposal["files_to_modify"]
        )

        proposal["generated_at"] = datetime.now(UTC).isoformat()

        return proposal

    # ---------------------------------------------------------
    # CAPABILITY MODE
    # ---------------------------------------------------------

    def design_capability(self, capability):

        """
        Converts capability gaps into architecture blueprints.
        """

        if capability == "portfolio_engine":

            blueprint = self._portfolio_architecture()

        elif capability == "regime_detection":

            blueprint = self._regime_architecture()

        else:

            blueprint = self._generic_architecture(capability)

        blueprint["modules"] = self._filter_paths(blueprint["modules"])

        return blueprint

    # ---------------------------------------------------------
    # PORTFOLIO ARCHITECTURE
    # ---------------------------------------------------------

    def _portfolio_architecture(self):

        return {
            "generated_at": datetime.now(UTC).isoformat(),
            "capability": "portfolio_engine",
            "modules": [
                "runtime/portfolio/portfolio_engine.py",
                "runtime/portfolio/position_sizer.py",
                "runtime/portfolio/allocation_strategy.py"
            ],
            "description": "Portfolio allocation and position sizing system."
        }

    # ---------------------------------------------------------
    # REGIME ARCHITECTURE
    # ---------------------------------------------------------

    def _regime_architecture(self):

        return {
            "generated_at": datetime.now(UTC).isoformat(),
            "capability": "regime_detection",
            "modules": [
                "runtime/market/regime_detector.py",
                "runtime/market/regime_classifier.py",
                "runtime/market/regime_features.py"
            ],
            "description": "Market regime detection and classification system."
        }

    # ---------------------------------------------------------
    # GENERIC CAPABILITY
    # ---------------------------------------------------------

    def _generic_architecture(self, capability):

        return {
            "generated_at": datetime.now(UTC).isoformat(),
            "capability": capability,
            "modules": [
                f"runtime/development/{capability}.py"
            ],
            "description": "Generic capability module."
        }


# ---------------------------------------------------------
# TEST
# ---------------------------------------------------------

if __name__ == "__main__":

    agent = ArchitectureAgent()

    blueprint = agent.design_capability("regime_detection")

    print("\nArchitecture Blueprint:\n")

    print("Capability:", blueprint["capability"])

    print("Modules:")

    for m in blueprint["modules"]:
        print("-", m)