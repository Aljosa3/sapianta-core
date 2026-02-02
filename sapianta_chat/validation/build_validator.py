# PATH: sapianta_chat/validation/build_validator.py

from dataclasses import dataclass
from typing import List, Dict, Set
from pathlib import Path


@dataclass(frozen=True)
class ValidationResult:
    status: str  # "PASS" | "FAIL"
    errors: List[str]


class BuildValidator:
    """
    HARD-GATE BUILD VALIDATOR

    Rules:
    - NO fixing
    - NO side effects
    - Deterministic PASS / FAIL
    - Scans ONLY generated_root (never whole repo / venv)
    """

    def __init__(
        self,
        build_plan: Dict,
        generated_root: str,
        forbidden_files: Set[str],
        forbidden_imports: Set[str],
    ):
        self.build_plan = build_plan
        self.generated_root = Path(generated_root).resolve()
        self.forbidden_files = forbidden_files
        self.forbidden_imports = forbidden_imports
        self.errors: List[str] = []

    # ---------- public API ----------

    def validate(self) -> ValidationResult:
        if not self.generated_root.exists():
            return ValidationResult(
                status="FAIL",
                errors=[f"Generated root does not exist: {self.generated_root}"],
            )

        self._check_structure()
        self._check_files_and_imports()

        if self.errors:
            return ValidationResult(status="FAIL", errors=self.errors)

        return ValidationResult(status="PASS", errors=[])

    # ---------- validation steps ----------

    def _check_structure(self) -> None:
        """
        Ensures all expected paths from build_plan exist.
        """
        expected_paths = self.build_plan.get("expected_paths", [])

        for rel_path in expected_paths:
            abs_path = (self.generated_root / rel_path).resolve()
            if not abs_path.exists():
                self.errors.append(f"Missing path: {rel_path}")

    def _check_files_and_imports(self) -> None:
        """
        Scans ONLY generated_root for forbidden files and imports.
        """
        for path in self.generated_root.rglob("*"):
            if not path.is_file():
                continue

            # 🔒 HARD SCOPE GUARD
            if not self._is_within_generated_root(path):
                continue

            self._check_forbidden_file(path)
            self._check_forbidden_imports(path)

    # ---------- checks ----------

    def _check_forbidden_file(self, path: Path) -> None:
        if path.suffix in self.forbidden_files:
            rel = path.relative_to(self.generated_root)
            self.errors.append(f"Forbidden file detected: {rel}")

    def _check_forbidden_imports(self, path: Path) -> None:
        if path.suffix != ".py":
            return

        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            return

        for forbidden in self.forbidden_imports:
            if f"import {forbidden}" in content or f"from {forbidden}" in content:
                rel = path.relative_to(self.generated_root)
                self.errors.append(
                    f"Forbidden import '{forbidden}' in {rel}"
                )

    # ---------- helpers ----------

    def _is_within_generated_root(self, path: Path) -> bool:
        """
        Absolute guarantee that we never scan outside generated_root.
        """
        try:
            path.relative_to(self.generated_root)
            return True
        except ValueError:
            return False
