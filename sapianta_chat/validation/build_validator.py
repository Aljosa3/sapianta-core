from dataclasses import dataclass
from typing import List, Dict, Set
import os

@dataclass(frozen=True)
class ValidationResult:
    status: str  # "PASS" | "FAIL"
    errors: List[str]


class BuildValidator:
    """
    Validator Hook
    - NO fixing
    - NO side effects
    - Deterministic PASS / FAIL
    """

    def __init__(
        self,
        build_plan: Dict,
        generated_root: str,
        forbidden_files: Set[str],
        forbidden_imports: Set[str],
    ):
        self.build_plan = build_plan
        self.generated_root = generated_root
        self.forbidden_files = forbidden_files
        self.forbidden_imports = forbidden_imports

    def validate(self) -> ValidationResult:
        errors: List[str] = []

        errors += self._check_structure()
        errors += self._check_files()
        errors += self._check_imports()

        if errors:
            return ValidationResult(status="FAIL", errors=errors)

        return ValidationResult(status="PASS", errors=[])

    def _check_structure(self) -> List[str]:
        errors = []
        expected_paths = set(self.build_plan.get("paths", []))

        for path in expected_paths:
            abs_path = os.path.join(self.generated_root, path)
            if not os.path.exists(abs_path):
                errors.append(f"Missing path: {path}")

        return errors

    def _check_files(self) -> List[str]:
        """
        Enforces forbidden file policy based on file suffixes
        (e.g. '.md' forbids all Markdown files).
        """
        errors = []

        for root, _, files in os.walk(self.generated_root):
            for f in files:
                for forbidden in self.forbidden_files:
                    if f.endswith(forbidden):
                        rel = os.path.relpath(
                            os.path.join(root, f),
                            self.generated_root
                        )
                        errors.append(f"Forbidden file detected: {rel}")

        return errors

    def _check_imports(self) -> List[str]:
        errors = []

        for root, _, files in os.walk(self.generated_root):
            for f in files:
                if not f.endswith(".py"):
                    continue

                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as fh:
                    for line_no, line in enumerate(fh, 1):
                        for forbidden in self.forbidden_imports:
                            if forbidden in line:
                                rel = os.path.relpath(path, self.generated_root)
                                errors.append(
                                    f"Forbidden import '{forbidden}' in {rel}:{line_no}"
                                )

        return errors
