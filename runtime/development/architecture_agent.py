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
- enforces deterministic JSON architecture contract
- extracts DEVELOPMENT REQUEST from enriched prompts
"""

import os
import json
from datetime import datetime, UTC


class ArchitectureAgent:

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

    def __init__(self, system_knowledge=None, repo_root="runtime"):

        self.system_knowledge = system_knowledge
        self.repo_root = repo_root
        self.repo_map = self._scan_repo()

    def _scan_repo(self):

        repo_map = {}

        for root, dirs, files in os.walk(self.repo_root):

            modules = []

            for file in files:
                if file.endswith(".py"):
                    modules.append(file)

            repo_map[root] = modules

        return repo_map

    def _extract_request(self, context: str) -> str:

        marker = "DEVELOPMENT REQUEST"

        if marker not in context:
            return context.strip()

        _, tail = context.split(marker, 1)

        tail = tail.strip()

        lines = tail.splitlines()

        cleaned = []
        for line in lines:
            if set(line.strip()) == {"-"}:
                continue
            cleaned.append(line)

        return "\n".join(cleaned).strip()

    def _module_exists(self, path):
        return os.path.exists(path)

    def _filter_paths(self, paths):

        filtered = []

        for path in paths:

            if any(path.startswith(fp) for fp in self.FORBIDDEN_PATHS):
                continue

            if any(path.startswith(ap) for ap in self.ALLOWED_PREFIXES):
                filtered.append(path)

        return filtered

    def _detect_domain(self, request):

        ctx = request.lower()

        if "test" in ctx or "pipeline" in ctx:
            return "development"

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

        return "development"

    def _generate_module_name(self, request):

        ctx = request.lower()

        if "test pipeline" in ctx:
            return "test_pipeline.py"

        if "test" in ctx:
            return "test_module.py"

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

        if "optimizer" in ctx:
            return "optimizer.py"

        return "generated_module.py"

    def _build_module_path(self, domain, module):
        return f"runtime/{domain}/{module}"

    def _validate_contract(self, proposal):

        required = [
            "description",
            "files_to_create",
            "files_to_modify"
        ]

        for key in required:
            if key not in proposal:
                raise Exception(
                    f"ArchitectureAgent: missing required field '{key}'"
                )

        if not isinstance(proposal["files_to_create"], list):
            raise Exception("files_to_create must be list")

        if not isinstance(proposal["files_to_modify"], list):
            raise Exception("files_to_modify must be list")

        return proposal

    # ---------------------------------------------------------
    # SELF-HEALING PROPOSAL (NOVO)
    # ---------------------------------------------------------

    def propose(self, context: str):

        if self.system_knowledge:
            _ = self.system_knowledge.build_knowledge()

        request = self._extract_request(context)

        # ----------------------------------------
        # FIRST ATTEMPT (normal logic)
        # ----------------------------------------

        proposal = self._build_proposal(request)

        # ----------------------------------------
        # RETRY (simplified logic)
        # ----------------------------------------

        if not proposal["files_to_create"] and not proposal["files_to_modify"]:

            print("[ARCH] Empty architecture → retry simplified logic")

            simplified_request = f"implement minimal {request}"

            proposal = self._build_proposal(simplified_request)

        # ----------------------------------------
        # HARD FAILSAFE
        # ----------------------------------------

        if not proposal["files_to_create"] and not proposal["files_to_modify"]:

            print("[ARCH] Hard fallback → forcing minimal output")

            safe_name = request.lower().replace(" ", "_")[:40]

            proposal = {
                "description": f"Forced architecture for: {request}",
                "files_to_create": [
                    f"runtime/development/generated/{safe_name}.py"
                ],
                "files_to_modify": []
            }

        return self._validate_contract(proposal)

    # ---------------------------------------------------------
    # CORE BUILDER (ločeno za retry reuse)
    # ---------------------------------------------------------

    def _build_proposal(self, request):

        domain = self._detect_domain(request)
        module = self._generate_module_name(request)
        module_path = self._build_module_path(domain, module)

        files_to_create = []

        if not self._module_exists(module_path):
            files_to_create.append(module_path)

        proposal = {
            "description": request,
            "files_to_create": self._filter_paths(files_to_create),
            "files_to_modify": [],
            "generated_at": datetime.now(UTC).isoformat()
        }

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

    proposal = agent.propose("""
SYSTEM CONTEXT
--------------
runtime/development
runtime/analytics

DEVELOPMENT REQUEST
-------------------
implement test pipeline
""")

    print("\nArchitecture Proposal:\n")
    print("Description:", proposal["description"])

    print("\nFiles to create:")
    for m in proposal["files_to_create"]:
        print("-", m)