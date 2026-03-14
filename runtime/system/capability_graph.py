"""
SAPIANTA Capability Graph

Purpose
-------
Represents the system capability structure.

The graph tracks:

- existing capabilities
- capability dependencies
- capability gaps

This module enables autonomous capability discovery.
"""

import os


class CapabilityGraph:

    def __init__(self):

        self.capabilities = {}

    # ------------------------------------------------
    # Build capability graph
    # ------------------------------------------------

    def build(self, repo_root="runtime"):

        """
        Scan runtime directory and build capability graph.
        """

        capabilities = {}

        for root, dirs, files in os.walk(repo_root):

            for f in files:

                if not f.endswith(".py"):
                    continue

                path = os.path.join(root, f)

                capability = self._extract_capability(path)

                if capability not in capabilities:

                    capabilities[capability] = []

                capabilities[capability].append(path)

        self.capabilities = capabilities

        return capabilities

    # ------------------------------------------------
    # Extract capability name
    # ------------------------------------------------

    def _extract_capability(self, path):

        parts = path.split("/")

        if len(parts) < 3:
            return "core"

        return parts[1]

    # ------------------------------------------------
    # Check capability
    # ------------------------------------------------

    def has_capability(self, capability):

        return capability in self.capabilities

    # ------------------------------------------------
    # Detect missing capabilities
    # ------------------------------------------------

    def detect_missing(self, expected):

        missing = []

        for c in expected:

            if c not in self.capabilities:
                missing.append(c)

        return missing


# ------------------------------------------------
# TEST
# ------------------------------------------------

if __name__ == "__main__":

    graph = CapabilityGraph()

    graph.build()

    print("\nDetected capabilities:\n")

    for c in graph.capabilities:

        print(c)