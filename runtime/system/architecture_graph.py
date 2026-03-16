"""
SAPIANTA Architecture Graph

Repository Intelligence Engine for SAPIANTA.

Builds a structural architecture graph of the repository by:

- scanning Python modules
- extracting import dependencies
- mapping modules to packages
- mapping modules to architectural layers
- inferring basic system capabilities

This provides architectural self-awareness for SAPIANTA
and enables repo-aware reasoning for ArchitectureAgent.
"""

import ast
import json
from pathlib import Path
from dataclasses import dataclass, asdict


# ---------------------------------------------------------
# GRAPH NODES
# ---------------------------------------------------------


@dataclass(frozen=True)
class GraphNode:

    node_id: str
    node_type: str
    name: str
    path: str | None = None
    metadata: dict | None = None


@dataclass(frozen=True)
class GraphEdge:

    source: str
    edge_type: str
    target: str
    metadata: dict | None = None


# ---------------------------------------------------------
# ARCHITECTURE GRAPH
# ---------------------------------------------------------


class ArchitectureGraph:

    def __init__(self, root):

        self.root = Path(root).resolve()

        if not self.root.exists():
            raise RuntimeError(f"Repository root does not exist: {self.root}")

        self.modules = {}
        self.packages = {}
        self.layers = {}
        self.capabilities = {}

        self.edges = set()

        self.module_index = {}

        self.graph = {}

    # ---------------------------------------------------------
    # BUILD GRAPH
    # ---------------------------------------------------------

    def build_graph(self):

        py_files = self._scan_modules()

        self._index_modules(py_files)

        self._create_layers()

        self._attach_modules()

        self._extract_dependencies(py_files)

        self._infer_capabilities(py_files)

        return self._to_dict()

    # ---------------------------------------------------------
    # SCAN MODULES
    # ---------------------------------------------------------

    def _scan_modules(self):

        excluded = {
            ".git",
            "__pycache__",
            ".venv",
            "venv",
            ".pytest_cache",
            "dist",
            "build",
        }

        files = []

        for p in self.root.rglob("*.py"):

            if any(x in p.parts for x in excluded):
                continue

            files.append(p)

        return sorted(files)

    # ---------------------------------------------------------
    # MODULE INDEX
    # ---------------------------------------------------------

    def _index_modules(self, py_files):

        for p in py_files:

            rel = p.relative_to(self.root)

            module = self._module_name(rel)

            module_id = f"module:{module}"

            node = GraphNode(
                node_id=module_id,
                node_type="module",
                name=module,
                path=str(rel),
                metadata={"init": p.name == "__init__.py"},
            )

            self.modules[module_id] = node

            self.module_index[module] = module_id

            pkg = self._package_name(module)

            if pkg:

                pkg_id = f"package:{pkg}"

                if pkg_id not in self.packages:

                    self.packages[pkg_id] = GraphNode(
                        node_id=pkg_id,
                        node_type="package",
                        name=pkg,
                        path=str(Path(*pkg.split("."))),
                    )

    # ---------------------------------------------------------
    # LAYER DETECTION
    # ---------------------------------------------------------

    def _create_layers(self):

        layers = [
            "runtime",
            "governance",
            "cli",
            "domains",
            "core",
            "tests",
        ]

        for layer in layers:

            layer_id = f"layer:{layer}"

            self.layers[layer_id] = GraphNode(
                node_id=layer_id,
                node_type="layer",
                name=layer,
                path=layer,
            )

    # ---------------------------------------------------------
    # ATTACH MODULES
    # ---------------------------------------------------------

    def _attach_modules(self):

        for module_id, node in self.modules.items():

            module = node.name

            pkg = self._package_name(module)

            if pkg:

                pkg_id = f"package:{pkg}"

                if pkg_id in self.packages:

                    self._add_edge(module_id, "belongs_to", pkg_id)

            if node.path:

                first = Path(node.path).parts[0]

                layer_id = f"layer:{first}"

                if layer_id in self.layers:

                    self._add_edge(module_id, "located_in_layer", layer_id)

    # ---------------------------------------------------------
    # IMPORT EXTRACTION
    # ---------------------------------------------------------

    def _extract_dependencies(self, py_files):

        for p in py_files:

            rel = p.relative_to(self.root)

            source = self._module_name(rel)

            source_id = f"module:{source}"

            try:

                tree = ast.parse(p.read_text(encoding="utf-8"))

            except Exception:

                continue

            imports = self._collect_imports(tree)

            for imp in imports:

                target = self._resolve_module(imp)

                if not target:
                    continue

                self._add_edge(source_id, "imports", target)

                self._add_edge(source_id, "depends_on", target)

    # ---------------------------------------------------------
    # IMPORT COLLECTOR
    # ---------------------------------------------------------

    def _collect_imports(self, tree):

        imports = set()

        for node in ast.walk(tree):

            if isinstance(node, ast.Import):

                for name in node.names:
                    imports.add(name.name)

            elif isinstance(node, ast.ImportFrom):

                if node.module:
                    imports.add(node.module)

        return imports

    # ---------------------------------------------------------
    # INTERNAL MODULE RESOLUTION
    # ---------------------------------------------------------

    def _resolve_module(self, name):

        if name in self.module_index:
            return self.module_index[name]

        init_candidate = f"{name}.__init__"

        if init_candidate in self.module_index:
            return self.module_index[init_candidate]

        for m in sorted(self.module_index.keys(), key=len, reverse=True):

            if name.startswith(m + "."):
                return self.module_index[m]

        return None

    # ---------------------------------------------------------
    # CAPABILITY INFERENCE
    # ---------------------------------------------------------

    def _infer_capabilities(self, py_files):

        keywords = {
            "graph": "repo_intelligence",
            "repository": "repo_intelligence",
            "context": "repo_intelligence",
            "generator": "module_generation",
            "sanitize": "code_sanitization",
            "validator": "validation",
            "test": "testing",
            "orchestrator": "orchestration",
            "agent": "agentic_coordination",
            "policy": "policy_engine",
            "ledger": "ledger",
            "regime": "regime_detection",
            "strategy": "strategy_logic",
        }

        for p in py_files:

            rel = p.relative_to(self.root)

            module = self._module_name(rel)

            module_id = f"module:{module}"

            tokens = module.replace(".", "_").split("_")

            for token in tokens:

                if token in keywords:

                    cap = keywords[token]

                    cap_id = f"capability:{cap}"

                    if cap_id not in self.capabilities:

                        self.capabilities[cap_id] = GraphNode(
                            node_id=cap_id,
                            node_type="capability",
                            name=cap,
                        )

                    self._add_edge(module_id, "implements", cap_id)

    # ---------------------------------------------------------
    # SERIALIZATION
    # ---------------------------------------------------------

    def _to_dict(self):

        packages = [asdict(x) for x in sorted(self.packages.values(), key=lambda n: n.node_id)]
        modules = [asdict(x) for x in sorted(self.modules.values(), key=lambda n: n.node_id)]
        layers = [asdict(x) for x in sorted(self.layers.values(), key=lambda n: n.node_id)]
        capabilities = [asdict(x) for x in sorted(self.capabilities.values(), key=lambda n: n.node_id)]

        edges = []

        for s, t, d in sorted(self.edges):

            edges.append({
                "source": s,
                "edge_type": t,
                "target": d
            })

        return {
            "graph_version": "1.0",
            "root": str(self.root),
            "packages": packages,
            "modules": modules,
            "layers": layers,
            "capabilities": capabilities,
            "edges": edges
        }

    # ---------------------------------------------------------
    # EDGE ADD
    # ---------------------------------------------------------

    def _add_edge(self, source, edge_type, target):

        self.edges.add((source, edge_type, target))

    # ---------------------------------------------------------
    # MODULE NAME
    # ---------------------------------------------------------

    def _module_name(self, rel_path):

        return ".".join(rel_path.with_suffix("").parts)

    # ---------------------------------------------------------
    # PACKAGE NAME
    # ---------------------------------------------------------

    def _package_name(self, module):

        parts = module.split(".")

        if len(parts) <= 1:
            return ""

        if parts[-1] == "__init__":
            return ".".join(parts[:-1])

        return ".".join(parts[:-1])

    # ---------------------------------------------------------
    # RUNTIME DEPENDENCIES
    # ---------------------------------------------------------

    def runtime_dependencies(self):

        graph = self.build_graph()

        runtime_graph = {}

        for e in graph["edges"]:

            if e["edge_type"] != "depends_on":
                continue

            src = e["source"]
            dst = e["target"]

            if "runtime." not in src:
                continue

            runtime_graph.setdefault(src, []).append(dst)

        return runtime_graph

    # ---------------------------------------------------------
    # PRINT GRAPH
    # ---------------------------------------------------------

    def print_graph(self):

        deps = self.runtime_dependencies()

        for module in sorted(deps):

            print(module)

            for d in sorted(deps[module]):

                print("   ->", d)

    # ---------------------------------------------------------
    # SAVE JSON
    # ---------------------------------------------------------

    def save_json(self, path="architecture_graph.json"):

        graph = self.build_graph()

        with open(path, "w", encoding="utf-8") as f:

            json.dump(graph, f, indent=2, sort_keys=True)

        return path


# ---------------------------------------------------------
# CLI ENTRY
# ---------------------------------------------------------

if __name__ == "__main__":

    g = ArchitectureGraph(Path.cwd())

    graph = g.build_graph()

    print("Architecture graph built.")

    g.print_graph()