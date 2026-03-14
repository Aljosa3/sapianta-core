"""
SAPIANTA Capability Gap Detector

Analyzes system_state.json and runtime structure
to identify missing capabilities.

The detector combines:

1. Declared gaps from system_state.json
2. Runtime capability introspection using CapabilityGraph

The module produces development proposals which can later
be passed to the Governed Autonomous Development pipeline.

This is a key component of self-directed system evolution.
"""

import json
import os
from datetime import datetime, UTC

from runtime.system.capability_graph import CapabilityGraph


SYSTEM_STATE_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "system",
    "system_state.json"
)


class CapabilityGapDetector:

    def __init__(self):

        if not os.path.exists(SYSTEM_STATE_PATH):
            raise RuntimeError("system_state.json not found")

        with open(SYSTEM_STATE_PATH, encoding="utf-8") as f:
            self.state = json.load(f)

        self.graph = CapabilityGraph()

    # ---------------------------------------------------------
    # GAP DETECTION
    # ---------------------------------------------------------

    def detect(self):

        declared_missing = self.state.get("missing_capabilities", [])

        # build runtime capability graph
        self.graph.build()

        proposals = []

        for capability in declared_missing:

            # if runtime already has the capability skip it
            if self.graph.has_capability(capability):
                continue

            proposals.append(
                self._build_proposal(capability)
            )

        return proposals

    # ---------------------------------------------------------
    # PROPOSAL BUILDER
    # ---------------------------------------------------------

    def _build_proposal(self, capability):

        priority = self._priority(capability)

        proposal = {

            "generated_at": datetime.now(UTC).isoformat(),

            "type": "development_proposal",

            "capability": capability,

            "priority": priority,

            "recommended_module":
                f"runtime.development.{capability}",

            "description":
                self._description(capability)

        }

        return proposal

    # ---------------------------------------------------------
    # PRIORITY HEURISTIC
    # ---------------------------------------------------------

    def _priority(self, capability):

        high = [
            "portfolio_engine",
            "regime_detection",
            "risk_engine"
        ]

        if capability in high:
            return "HIGH"

        return "MEDIUM"

    # ---------------------------------------------------------
    # DESCRIPTION GENERATOR
    # ---------------------------------------------------------

    def _description(self, capability):

        descriptions = {

            "portfolio_engine":
                "Portfolio construction and capital allocation engine.",

            "regime_detection":
                "Real-time detection of market regimes.",

            "risk_engine":
                "Centralized portfolio risk evaluation engine."
        }

        return descriptions.get(
            capability,
            "Capability not yet implemented."
        )


# ---------------------------------------------------------
# CLI ENTRYPOINT
# ---------------------------------------------------------

def main():

    print("SAPIANTA Capability Gap Detector")
    print("--------------------------------")

    detector = CapabilityGapDetector()

    proposals = detector.detect()

    if not proposals:

        print("No capability gaps detected.")
        return

    print("Development proposals:")
    print()

    for p in proposals:

        print(p["capability"], "→", p["priority"])
        print("  module:", p["recommended_module"])
        print("  description:", p["description"])
        print()


if __name__ == "__main__":
    main()