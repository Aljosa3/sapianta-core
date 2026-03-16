"""
SAPIANTA Architecture Agent

Purpose
-------
Generates architecture blueprints and architecture proposals
for new system capabilities.

Repo-aware ArchitectureAgent:
- scans repository structure
- detects architectural domains
- proposes architecture-compliant modules
- enforces guardrails

Pipeline

Capability Gap / Strategic Context
        ↓
Repository Scan
        ↓
Architecture Reasoning
        ↓
Module Design
        ↓
Development Blueprint
"""

import os
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
        "runtime/risk",
        "sapianta-domain-"
    ]

    # ---------------------------------------------------------
    # INIT
    # ---------------------------------------------------------

    def __init__(self, system_knowledge=None, repo_root="runtime"):

        self.system_knowledge = system_knowledge
        self.repo_root = repo_root

        # build repository map
        self.repo_map = self._scan_repo()

    # ---------------------------------------------------------
    # REPOSITORY SCAN
    # ---------------------------------------------------------

    def _scan_repo(self):

        repo_map = {}

        for root, dirs, files in os.walk(self.repo_root):

            modules = []

            for file in files:
                if file.endswith(".py"):
                    modules.append(file)

            repo_map[root] = modules

        return repo_map

    # ---------------------------------------------------------
    # CHECK MODULE EXISTENCE
    # ---------------------------------------------------------

    def _module_exists(self, path):

        return os.path.exists(path)

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
    # DOMAIN DETECTION
    # ---------------------------------------------------------

    def _detect_domain(self, context):

        ctx = context.lower()

        if "regime" in ctx or "market" in ctx:
            return "analytics"

        if "memory" in ctx or "history" in ctx:
            return "memory"

        if "strategy" in ctx:
            return "strategies"

        if "risk" in ctx:
            return "risk"

        if "portfolio" in ctx:
            return "portfolio"

        if "research" in ctx:
            return "research"

        return "analytics"

    # ---------------------------------------------------------
    # MODULE NAME GENERATION
    # ---------------------------------------------------------

    def _generate_module_name(self, context):

        ctx = context.lower()

        if "regime" in ctx:
            return "regime_detector.py"

        if "memory" in ctx:
            return "strategy_memory.py"

        if "risk" in ctx:
            return "risk_engine.py"

        if "portfolio" in ctx:
            return "portfolio_engine.py"

        if "signal" in ctx:
            return "signal_engine.py"

        return "module.py"

    # ---------------------------------------------------------
    # BUILD MODULE PATH
    # ---------------------------------------------------------

    def _build_module_path(self, domain, module):

        return f"runtime/{domain}/{module}"

    # ---------------------------------------------------------
    # CONTEXT MODE (from sapianta discuss)
    # ---------------------------------------------------------

    def propose(self, context: str):

        """
        Generate architecture proposal from discussion context.
        """

        if self.system_knowledge:
            _ = self.system_knowledge.build_knowledge()

        domain = self._detect_domain(context)

        module = self._generate_module_name(context)

        module_path = self._build_module_path(domain, module)

        files_to_create = []

        # avoid duplicates
        if not self._module_exists(module_path):
            files_to_create.append(module_path)

        proposal = {
            "description": context,
            "files_to_create": files_to_create,
            "files_to_modify": [],
            "reason": "ArchitectureAgent repo-aware proposal"
        }

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
                "runtime/analytics/regime_detector.py",
                "runtime/analytics/regime_classifier.py",
                "runtime/analytics/regime_features.py"
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
# LOCAL TEST
# ---------------------------------------------------------

if __name__ == "__main__":

    agent = ArchitectureAgent()

    proposal = agent.propose("add regime detection engine")

    print("\nArchitecture Proposal:\n")

    print("Description:", proposal["description"])

    print("\nFiles to create:")

    for m in proposal["files_to_create"]:
        print("-", m)