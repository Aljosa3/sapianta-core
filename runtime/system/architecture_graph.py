"""
SAPIANTA Architecture Graph

Builds a structural map of the runtime architecture
by analyzing module imports.

This provides architectural self-awareness for SAPIANTA.
"""

import ast
from pathlib import Path


class ArchitectureGraph:

    def __init__(self, root):

        self.root = Path(root)
        self.graph = {}

    # ---------------------------------------------------------
    # MODULE SCAN
    # ---------------------------------------------------------

    def scan_modules(self):

        for p in self.root.rglob("*.py"):

            module = self._module_name(p)

            imports = self._extract_imports(p)

            self.graph[module] = imports

    # ---------------------------------------------------------
    # MODULE NAME
    # ---------------------------------------------------------

    def _module_name(self, path):

        rel = path.relative_to(self.root)

        module = "runtime." + str(rel).replace("/", ".").replace(".py", "")

        return module

    # ---------------------------------------------------------
    # IMPORT EXTRACTION
    # ---------------------------------------------------------

    def _extract_imports(self, path):

        imports = []

        try:

            with open(path, "r", encoding="utf-8") as f:

                node = ast.parse(f.read())

        except Exception:

            # fail-safe parsing
            return imports

        for item in ast.walk(node):

            if isinstance(item, ast.Import):

                for name in item.names:
                    imports.append(name.name)

            elif isinstance(item, ast.ImportFrom):

                if item.module:
                    imports.append(item.module)

        return imports

    # ---------------------------------------------------------
    # BUILD GRAPH
    # ---------------------------------------------------------

    def build_graph(self):

        self.scan_modules()

        return self.graph

    # ---------------------------------------------------------
    # RUNTIME DEPENDENCIES
    # ---------------------------------------------------------

    def runtime_dependencies(self):

        if not self.graph:
            self.build_graph()

        runtime_graph = {}

        for module, deps in self.graph.items():

            runtime_graph[module] = [
                d for d in deps if d.startswith("runtime")
            ]

        return runtime_graph

    # ---------------------------------------------------------
    # PRINT GRAPH
    # ---------------------------------------------------------

    def print_graph(self):

        runtime_graph = self.runtime_dependencies()

        for module in sorted(runtime_graph):

            deps = runtime_graph[module]

            if deps:

                print(module)

                for d in sorted(deps):

                    print("   ->", d)