import importlib
import inspect
from typing import List, Dict

from sapianta_chat.cli.pipeline_integrity import REQUIRED_MODULES


class ModuleObligationProposal:
    """
    Advisory-only analysis.
    Does NOT modify REQUIRED_MODULES.
    """

    def __init__(self, candidate_modules: List[str]):
        self.candidate_modules = candidate_modules

    def analyze(self) -> List[Dict]:
        """
        Returns proposal list with:
        - module
        - suggested_status (REQUIRED / NON-REQUIRED)
        - reasons
        """
        proposals = []

        for module_path in self.candidate_modules:
            reasons = []
            suggested = "NON-REQUIRED"

            # already required → skip proposal
            if module_path in REQUIRED_MODULES:
                continue

            try:
                module = importlib.import_module(module_path)
            except Exception as e:
                proposals.append({
                    "module": module_path,
                    "suggested_status": "NON-REQUIRED",
                    "reasons": [f"Module not importable: {e}"],
                })
                continue

            # Heuristic 1: imported by REQUIRED module
            for req in REQUIRED_MODULES:
                try:
                    req_mod = importlib.import_module(req)
                    source = inspect.getsource(req_mod)
                    if module_path in source:
                        suggested = "REQUIRED"
                        reasons.append(
                            f"Imported or referenced by REQUIRED module: {req}"
                        )
                except Exception:
                    continue

            # Heuristic 2: contains hard-gate semantics
            if hasattr(module, "sys") or "exit(" in inspect.getsource(module):
                suggested = "REQUIRED"
                reasons.append("Contains hard-stop / exit semantics")

            if not reasons:
                reasons.append("Module not part of mandatory execution path")

            proposals.append({
                "module": module_path,
                "suggested_status": suggested,
                "reasons": reasons,
            })

        return proposals
