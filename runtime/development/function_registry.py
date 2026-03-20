"""
SAPIANTA Function Registry (E Phase)

Purpose:
- index all functions in project
- enable fast lookup (no rglob per call)
- provide dependency graph

Design:
- deterministic
- read-only scan
- cached in memory
"""

import re
from pathlib import Path
from typing import Dict, List


class FunctionRegistry:

    def __init__(self, project_root: Path = Path(".")):
        self.project_root = project_root
        self.function_map: Dict[str, str] = {}
        self.dependency_graph: Dict[str, List[str]] = {}

    # ================================================================
    # BUILD REGISTRY
    # ================================================================

    def build(self):

        self.function_map.clear()
        self.dependency_graph.clear()

        for py_file in self.project_root.rglob("*.py"):

            if "__pycache__" in str(py_file):
                continue

            try:
                content = py_file.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue

            module_path = py_file.with_suffix("")
            module_str = str(module_path).replace("/", ".").replace("\\", ".")

            if module_str.startswith("."):
                module_str = module_str[1:]

            functions = self._extract_functions(content)
            calls = self._extract_function_calls(content)

            # store functions
            for func in functions:
                self.function_map[func] = module_str

            # store dependencies
            self.dependency_graph[module_str] = calls

    # ================================================================
    # LOOKUP
    # ================================================================

    def find_function(self, name: str):

        return self.function_map.get(name)

    def get_dependencies(self, module: str):

        return self.dependency_graph.get(module, [])

    # ================================================================
    # EXTRACTORS
    # ================================================================

    def _extract_functions(self, content: str) -> List[str]:

        matches = re.findall(r"def (\w+)\(", content)
        return list(set(matches))

    def _extract_function_calls(self, content: str) -> List[str]:

        matches = re.findall(r"(\w+)\(", content)

        # filter obvious noise
        blacklist = {"if", "for", "while", "return", "print"}

        return [m for m in set(matches) if m not in blacklist]