"""
SAPIANTA Capability Planner

Plans development order using capability dependencies.

This module ensures that capabilities are developed
in a valid architectural order.

Example

portfolio_engine
        ↓
risk_engine
        ↓
analytics
"""

import json
import os


DEPENDENCY_FILE = os.path.join(
    os.path.dirname(__file__),
    "capability_dependencies.json"
)


class CapabilityPlanner:

    def __init__(self):

        if not os.path.exists(DEPENDENCY_FILE):
            raise RuntimeError("capability_dependencies.json missing")

        with open(DEPENDENCY_FILE, encoding="utf-8") as f:
            self.dependencies = json.load(f)

    # ---------------------------------------------------------
    # BUILD DEVELOPMENT PLAN
    # ---------------------------------------------------------

    def plan(self, capability):

        """
        Returns ordered development list
        respecting capability dependencies.
        """

        plan = []

        self._resolve(capability, plan)

        return plan

    # ---------------------------------------------------------
    # DEPENDENCY RESOLUTION
    # ---------------------------------------------------------

    def _resolve(self, capability, plan):

        if capability not in self.dependencies:
            plan.append(capability)
            return

        deps = self.dependencies[capability]["depends_on"]

        for d in deps:

            if d not in plan:
                self._resolve(d, plan)

        if capability not in plan:
            plan.append(capability)


# ---------------------------------------------------------
# TEST
# ---------------------------------------------------------

if __name__ == "__main__":

    planner = CapabilityPlanner()

    plan = planner.plan("portfolio_engine")

    print("\nCapability Development Plan:\n")

    for p in plan:
        print("-", p)