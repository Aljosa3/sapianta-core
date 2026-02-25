#!/usr/bin/env python3

import subprocess
import sys
import re
from enum import IntEnum
from dataclasses import dataclass
from typing import List


# -----------------------------
# Severity Model
# -----------------------------

class Severity(IntEnum):
    COSMETIC = 1
    PARAMETRIC = 2
    STRUCTURAL = 3


@dataclass
class Evidence:
    rule_id: str
    file: str
    severity: Severity
    reason: str


# -----------------------------
# Diff Collector
# -----------------------------

class DiffCollector:

    def __init__(self, diff_range: str = "HEAD~1..HEAD"):
        self.diff_range = diff_range

    def changed_files(self) -> List[str]:
        result = subprocess.run(
            ["git", "diff", "--name-only", self.diff_range],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            self.fail_closed("git diff --name-only failed")
        return [f for f in result.stdout.strip().split("\n") if f]

    def unified_diff(self) -> str:
        result = subprocess.run(
            ["git", "diff", "--unified=0", self.diff_range],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            self.fail_closed("git diff --unified=0 failed")
        return result.stdout

    @staticmethod
    def fail_closed(message):
        print("Promotion Gate v0.2")
        print("Change Classification: STRUCTURAL")
        print(f"Reason: FAIL-CLOSED ({message})")
        sys.exit(1)


# -----------------------------
# Rule Engine
# -----------------------------

class RuleEngine:

    CORE_TRIPWIRES = [
        "sapianta_core/",
        "runtime/layers/",
        "runtime/validation/",
        "governance/constitution/",
        "governance/phases/",
        "scripts/check_layer_freeze.py",
    ]

    DOC_EXTENSIONS = (".md", ".rst")

    CONFIG_EXTENSIONS = (".yml", ".yaml", ".json", ".toml")

    def __init__(self, files: List[str], diff: str):
        self.files = files
        self.diff = diff
        self.evidence: List[Evidence] = []

    def evaluate(self):
        self.structural_rules()
        if not self.has_structural():
            self.parametric_rules()
        if not self.evidence:
            self.cosmetic_rules()

        return self.evidence

    # -----------------------------
    # Structural Rules
    # -----------------------------

    def structural_rules(self):
        for f in self.files:
            for trip in self.CORE_TRIPWIRES:
                if f.startswith(trip):
                    self.evidence.append(Evidence(
                        "S1",
                        f,
                        Severity.STRUCTURAL,
                        f"core/lifecycle surface modified ({f})"
                    ))

        # Public API signature detection
        for line in self.diff.splitlines():
            if line.startswith(("+def ", "-def ", "+class ", "-class ")):
                if any(f.startswith("sapianta_core/") for f in self.files):
                    self.evidence.append(Evidence(
                        "S2",
                        "sapianta_core",
                        Severity.STRUCTURAL,
                        "public API modified"
                    ))

        # __all__ export detection
        if "__all__" in self.diff:
            self.evidence.append(Evidence(
                "S3",
                "export surface",
                Severity.STRUCTURAL,
                "export surface modified"
            ))

    def has_structural(self):
        return any(e.severity == Severity.STRUCTURAL for e in self.evidence)

    # -----------------------------
    # Parametric Rules
    # -----------------------------

    def parametric_rules(self):

        # Config file value change
        for f in self.files:
            if f.endswith(self.CONFIG_EXTENSIONS):
                if re.search(r"-\s*.*:\s*[\d\.]+", self.diff) and re.search(r"\+\s*.*:\s*[\d\.]+", self.diff):
                    self.evidence.append(Evidence(
                        "P1",
                        f,
                        Severity.PARAMETRIC,
                        "configuration value modified"
                    ))

        # Numeric literal change in non-core
        if re.search(r"-.*\d+.*\n\+.*\d+.*", self.diff):
            if not self.has_structural():
                self.evidence.append(Evidence(
                    "P2",
                    "numeric_literal",
                    Severity.PARAMETRIC,
                    "numeric literal modified"
                ))

    # -----------------------------
    # Cosmetic Rules
    # -----------------------------

    def cosmetic_rules(self):

        # Docs only
        if all(f.endswith(self.DOC_EXTENSIONS) or f.startswith("docs/") for f in self.files):
            self.evidence.append(Evidence(
                "C1",
                "documentation",
                Severity.COSMETIC,
                "documentation only"
            ))
            return

        # Comment / whitespace only
        lines = [l for l in self.diff.splitlines() if l.startswith(("+", "-"))]
        meaningful = [
            l for l in lines
            if not re.match(r"[+-]\s*(#.*)?$", l)
        ]

        if not meaningful:
            self.evidence.append(Evidence(
                "C2",
                "whitespace/comment",
                Severity.COSMETIC,
                "comment/whitespace only"
            ))


# -----------------------------
# Classification
# -----------------------------

def classify(evidence: List[Evidence]):

    if not evidence:
        return Severity.COSMETIC

    return max(e.severity for e in evidence)


# -----------------------------
# CLI
# -----------------------------

def main():

    diff_range = sys.argv[1] if len(sys.argv) > 1 else "HEAD~1..HEAD"

    collector = DiffCollector(diff_range)
    files = collector.changed_files()
    diff = collector.unified_diff()

    engine = RuleEngine(files, diff)
    evidence = engine.evaluate()

    final = classify(evidence)

    print("Promotion Gate v0.2")
    print(f"Change Classification: {final.name}")
    print()

    if evidence:
        print("Evidence:")
        for e in evidence:
            print(f" - {e.rule_id}: {e.reason}")
    else:
        print("Evidence: none")

    print()
    print("Approval Required:", "YES" if final == Severity.STRUCTURAL else "NO")


if __name__ == "__main__":
    main()