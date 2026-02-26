#!/usr/bin/env python3
import subprocess
import sys
import re
from enum import IntEnum
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional


# -----------------------------
# Severity Model
# -----------------------------

class Severity(IntEnum):
    COSMETIC = 1
    PARAMETRIC = 2
    STRUCTURAL = 3


@dataclass(frozen=True)
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
    def fail_closed(message: str) -> None:
        print("Promotion Gate v0.2")
        print("Change Classification: STRUCTURAL")
        print(f"Reason: FAIL-CLOSED ({message})")
        sys.exit(1)


# -----------------------------
# Minimal Diff Parser (per-file)
# -----------------------------

_DIFF_HEADER_RE = re.compile(r"^diff --git a/(.+?) b/(.+?)$")


def split_diff_by_file(unified_diff: str) -> Dict[str, List[str]]:
    buckets: Dict[str, List[str]] = {}
    current_file: Optional[str] = None

    for line in unified_diff.splitlines():
        m = _DIFF_HEADER_RE.match(line)
        if m:
            current_file = m.group(2)
            buckets.setdefault(current_file, [])
            continue

        if current_file is not None:
            buckets[current_file].append(line)

    return buckets


def extract_changed_lines(file_lines: List[str]) -> Tuple[List[str], List[str]]:
    removed: List[str] = []
    added: List[str] = []

    for l in file_lines:
        if l.startswith("---") or l.startswith("+++"):
            continue
        if l.startswith("-"):
            removed.append(l[1:])
        elif l.startswith("+"):
            added.append(l[1:])

    return removed, added


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
        "tools/governance/",
        "scripts/check_layer_freeze.py",
    ]

    DOC_EXTENSIONS = (".md", ".rst")
    CONFIG_EXTENSIONS = (".yml", ".yaml", ".json", ".toml")

    def __init__(self, files: List[str], unified_diff: str):
        self.files = files
        self.unified_diff = unified_diff
        self.by_file = split_diff_by_file(unified_diff)
        self.evidence: List[Evidence] = []

    def evaluate(self) -> List[Evidence]:
        self.structural_rules()
        if not self.has_structural():
            self.parametric_rules()
        if not self.evidence:
            self.cosmetic_rules()
        return self._dedupe_evidence(self.evidence)

    @staticmethod
    def _dedupe_evidence(items: List[Evidence]) -> List[Evidence]:
        seen = set()
        out: List[Evidence] = []
        for e in items:
            key = (e.rule_id, e.file, e.severity, e.reason)
            if key not in seen:
                seen.add(key)
                out.append(e)
        return out

    def has_structural(self) -> bool:
        return any(e.severity == Severity.STRUCTURAL for e in self.evidence)

    # -----------------------------
    # STRUCTURAL RULES
    # -----------------------------

    def structural_rules(self) -> None:
        # S1 – Core/Enforcement Tripwire
        for f in self.files:
            for trip in self.CORE_TRIPWIRES:
                if f == trip or f.startswith(trip):
                    self.evidence.append(Evidence(
                        "S1",
                        f,
                        Severity.STRUCTURAL,
                        f"core/enforcement surface modified ({f})"
                    ))
                    break

        # S2 – Public API signature changes (ONLY within sapianta_core/)
        for f, lines in self.by_file.items():
            if not f.startswith("sapianta_core/"):
                continue
            removed, added = extract_changed_lines(lines)
            if any(s.lstrip().startswith(("def ", "class ")) for s in removed + added):
                self.evidence.append(Evidence(
                    "S2",
                    f,
                    Severity.STRUCTURAL,
                    f"public API modified ({f})"
                ))

        # S3 – Export surface changes
        for f, lines in self.by_file.items():
            if not f.startswith("sapianta_core/"):
                continue

            removed, added = extract_changed_lines(lines)

            if f.endswith("__init__.py") and (removed or added):
                self.evidence.append(Evidence(
                    "S3",
                    f,
                    Severity.STRUCTURAL,
                    f"export surface modified ({f})"
                ))
                continue

            def is_all_assignment(s: str) -> bool:
                s2 = s.strip()
                return s2.startswith("__all__") and "=" in s2

            if any(is_all_assignment(s) for s in removed + added):
                self.evidence.append(Evidence(
                    "S3",
                    f,
                    Severity.STRUCTURAL,
                    f"export surface modified (__all__ in {f})"
                ))

        # S4 – Runtime enforcement module changes (policy.py or validator.py)
        for f in self.files:
            if f.startswith("runtime/modules/") and (f.endswith("/policy.py") or f.endswith("/validator.py")):
                self.evidence.append(Evidence(
                    "S4",
                    f,
                    Severity.STRUCTURAL,
                    f"runtime enforcement module modified ({f})"
                ))

    # -----------------------------
    # PARAMETRIC RULES
    # -----------------------------

    def parametric_rules(self) -> None:
        for f, lines in self.by_file.items():
            if not f.endswith(self.CONFIG_EXTENSIONS):
                continue

            removed, added = extract_changed_lines(lines)
            removed_kv = self._extract_simple_kv_pairs(removed)
            added_kv = self._extract_simple_kv_pairs(added)

            for key, old_val in removed_kv.items():
                if key in added_kv and added_kv[key] != old_val:
                    self.evidence.append(Evidence(
                        "P1",
                        f,
                        Severity.PARAMETRIC,
                        f"configuration value modified ({f}: {key} {old_val} -> {added_kv[key]})"
                    ))
                    break

        for f, lines in self.by_file.items():
            if f.startswith("sapianta_core/"):
                continue

            removed, added = extract_changed_lines(lines)

            if any(s.lstrip().startswith(("def ", "class ", "import ", "from ")) for s in removed + added):
                continue

            if self._has_numeric_value_only_change(removed, added):
                self.evidence.append(Evidence(
                    "P2",
                    f,
                    Severity.PARAMETRIC,
                    f"numeric literal modified ({f})"
                ))

    @staticmethod
    def _extract_simple_kv_pairs(lines: List[str]) -> Dict[str, str]:
        out: Dict[str, str] = {}
        for s in lines:
            m = re.match(r"^\s*([A-Za-z0-9_\-\.]+)\s*:\s*(.+?)\s*$", s)
            if not m:
                continue
            out[m.group(1)] = m.group(2)
        return out

    @staticmethod
    def _normalize_numbers(s: str) -> str:
        return re.sub(r"\b\d+(\.\d+)?\b", "<NUM>", s)

    def _has_numeric_value_only_change(self, removed: List[str], added: List[str]) -> bool:
        removed_norm = {self._normalize_numbers(x) for x in removed if re.search(r"\b\d+(\.\d+)?\b", x)}
        added_norm = {self._normalize_numbers(x) for x in added if re.search(r"\b\d+(\.\d+)?\b", x)}
        return len(removed_norm.intersection(added_norm)) > 0

    # -----------------------------
    # COSMETIC RULES
    # -----------------------------

    def cosmetic_rules(self) -> None:
        if self.files and all(f.endswith(self.DOC_EXTENSIONS) or f.startswith("docs/") for f in self.files):
            self.evidence.append(Evidence(
                "C1",
                "documentation",
                Severity.COSMETIC,
                "documentation only"
            ))
            return

        if self._is_comment_whitespace_only():
            self.evidence.append(Evidence(
                "C2",
                "whitespace/comment",
                Severity.COSMETIC,
                "comment/whitespace only"
            ))

    def _is_comment_whitespace_only(self) -> bool:
        for f, lines in self.by_file.items():
            removed, added = extract_changed_lines(lines)
            for s in removed + added:
                s_strip = s.strip()
                if s_strip == "":
                    continue
                if s_strip.startswith("#"):
                    continue
                return False
        return True


# -----------------------------
# Classification / Output
# -----------------------------

def classify(evidence: List[Evidence]) -> Severity:
    if not evidence:
        return Severity.COSMETIC
    return max(e.severity for e in evidence)


def print_report(final: Severity, evidence: List[Evidence]) -> None:
    print("Promotion Gate v0.2")
    print(f"Change Classification: {final.name}")
    print()
    if evidence:
        print("Evidence:")
        def sort_key(e: Evidence):
            return (-int(e.severity), e.rule_id, e.file, e.reason)
        for e in sorted(evidence, key=sort_key):
            print(f" - {e.rule_id}: {e.reason}")
    else:
        print("Evidence: none")
    print()
    print("Approval Required:", "YES" if final == Severity.STRUCTURAL else "NO")


def main() -> None:
    diff_range = sys.argv[1] if len(sys.argv) > 1 else "HEAD~1..HEAD"

    collector = DiffCollector(diff_range)
    files = collector.changed_files()
    diff = collector.unified_diff()

    engine = RuleEngine(files, diff)
    evidence = engine.evaluate()
    final = classify(evidence)

    print_report(final, evidence)


if __name__ == "__main__":
    main()