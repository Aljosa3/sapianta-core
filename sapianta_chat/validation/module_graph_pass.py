# module_graph_pass.py
#
# SAPIANTA v0.20
# Validator phase: Module Graph Pass
#
# LOCKED BY:
# - PHASE_v0.20_MULTI_FILE_MODULE_LOCK.md
# - PHASE_v0.20_NEGATIVE_PROOF_WALKTHROUGH.md
# - PHASE_v0.20_IMPLEMENTATION_CHECKLIST.md
#
# This file implements ONLY structural validation.
# No runtime logic. No fixes. No heuristics.


from typing import Dict, List, Set
import ast


class ModuleGraphValidationError(Exception):
    """Hard-fail exception for module graph validation."""
    pass


class ModuleGraphPass:
    """
    Implements the v0.20 Module Graph Pass.

    Input:
        files: Dict[str, str]
            Mapping of FILE path -> file content

    Output:
        PASS: returns None
        FAIL: raises ModuleGraphValidationError
    """

    def __init__(self, files: Dict[str, str]) -> None:
        self.files = files
        self.module_root: str | None = None
        self.file_index: Set[str] = set()
        self.dependency_graph: Dict[str, Set[str]] = {}

    # ------------------------------------------------------------------
    # Phase 1 — Module Boundary Resolution
    # ------------------------------------------------------------------

    def _resolve_module_root(self) -> None:
        paths = list(self.files.keys())
        if not paths:
            raise ModuleGraphValidationError("No FILE blocks provided")

        split_paths = [path.split("/") for path in paths]
        common_parts = []

        for parts in zip(*split_paths):
            if all(p == parts[0] for p in parts):
                common_parts.append(parts[0])
            else:
                break

        if not common_parts:
            raise ModuleGraphValidationError("No common module root")

        self.module_root = "/".join(common_parts)

        for path in paths:
            if not path.startswith(self.module_root):
                raise ModuleGraphValidationError(
                    f"FILE outside module root: {path}"
                )

    # ------------------------------------------------------------------
    # Phase 2 — File Index Construction
    # ------------------------------------------------------------------

    def _build_file_index(self) -> None:
        for path in self.files.keys():
            if path in self.file_index:
                raise ModuleGraphValidationError(
                    f"Duplicate FILE path detected: {path}"
                )
            self.file_index.add(path)

    # ------------------------------------------------------------------
    # Phase 3 — Import Extraction (syntax-level only)
    # ------------------------------------------------------------------

    def _extract_imports(self, path: str, content: str) -> List[str]:
        try:
            tree = ast.parse(content)
        except SyntaxError as e:
            raise ModuleGraphValidationError(
                f"Syntax error in file {path}: {e}"
            )

        imports: List[str] = []

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for name in node.names:
                    imports.append(name.name)
            elif isinstance(node, ast.ImportFrom):
                if node.module is None:
                    raise ModuleGraphValidationError(
                        f"Non-static import in file {path}"
                    )
                imports.append(node.module)

        return imports

    # ------------------------------------------------------------------
    # Phase 4 — Module Boundary Enforcement
    # ------------------------------------------------------------------

    def _resolve_import_target(self, importer_path: str, module_name: str) -> str:
        """
        Maps an import name to a FILE path.
        Only simple module-level imports are allowed.
        """
        if "." in module_name:
            module_name = module_name.split(".")[0]

        candidate = f"{self.module_root}/{module_name}.py"

        if candidate not in self.file_index:
            raise ModuleGraphValidationError(
                f"Import outside module or missing file: {module_name} "
                f"(from {importer_path})"
            )

        return candidate

    # ------------------------------------------------------------------
    # Phase 5 — Dependency Graph Construction
    # ------------------------------------------------------------------

    def _build_dependency_graph(self) -> None:
        for path, content in self.files.items():
            self.dependency_graph[path] = set()
            imports = self._extract_imports(path, content)

            for module_name in imports:
                target = self._resolve_import_target(path, module_name)
                self.dependency_graph[path].add(target)

    # ------------------------------------------------------------------
    # Phase 6 — Cycle Detection (DAG check)
    # ------------------------------------------------------------------

    def _detect_cycles(self) -> None:
        visited: Set[str] = set()
        stack: Set[str] = set()

        def visit(node: str) -> None:
            if node in stack:
                raise ModuleGraphValidationError(
                    f"Circular dependency detected at {node}"
                )
            if node in visited:
                return

            visited.add(node)
            stack.add(node)

            for dep in self.dependency_graph.get(node, []):
                visit(dep)

            stack.remove(node)

        for node in self.dependency_graph:
            visit(node)

    # ------------------------------------------------------------------
    # Public entrypoint
    # ------------------------------------------------------------------

    def run(self) -> None:
        """
        Executes the full Module Graph Pass.
        PASS: returns None
        FAIL: raises ModuleGraphValidationError
        """
        self._resolve_module_root()
        self._build_file_index()
        self._build_dependency_graph()
        self._detect_cycles()
