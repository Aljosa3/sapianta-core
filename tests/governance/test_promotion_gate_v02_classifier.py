import importlib.util
from pathlib import Path

import pytest


# -----------------------------
# Load promotion_gate_v02.py as a module (no package required)
# -----------------------------

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools" / "governance" / "promotion_gate_v02.py"


def load_pg02():
    spec = importlib.util.spec_from_file_location("promotion_gate_v02", MODULE_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(mod)
    return mod


PG = load_pg02()


# -----------------------------
# Helpers to build minimal unified diffs
# -----------------------------

def make_unified_diff(file_path: str, removed=None, added=None) -> str:
    """
    Create a minimal unified diff chunk for a single file.
    Our parser only needs:
      - "diff --git a/... b/..."
      - +/- lines
    """
    removed = removed or []
    added = added or []

    lines = []
    lines.append(f"diff --git a/{file_path} b/{file_path}")
    lines.append("index 0000000..1111111 100644")
    lines.append(f"--- a/{file_path}")
    lines.append(f"+++ b/{file_path}")
    lines.append("@@ -1,0 +1,0 @@")
    for r in removed:
        lines.append(f"-{r}")
    for a in added:
        lines.append(f"+{a}")
    lines.append("")  # trailing newline
    return "\n".join(lines)


def classify(files, unified_diff):
    engine = PG.RuleEngine(files, unified_diff)
    evidence = engine.evaluate()
    final = PG.classify(evidence)
    return final, evidence


def evidence_ids(evidence):
    return [e.rule_id for e in evidence]


# -----------------------------
# Tests
# -----------------------------

def test_structural_S1_tripwire_tools_governance():
    files = ["tools/governance/promotion_gate_v02.py"]
    diff = make_unified_diff(
        "tools/governance/promotion_gate_v02.py",
        removed=["x = 1"],
        added=["x = 2"],
    )
    final, ev = classify(files, diff)
    assert final == PG.Severity.STRUCTURAL
    assert "S1" in evidence_ids(ev)


def test_structural_S2_public_api_signature_in_sapianta_core():
    files = ["sapianta_core/validator.py"]
    diff = make_unified_diff(
        "sapianta_core/validator.py",
        removed=["def old_api(x):"],
        added=["def new_api(x):"],
    )
    final, ev = classify(files, diff)
    assert final == PG.Severity.STRUCTURAL
    assert "S2" in evidence_ids(ev)


def test_structural_S3_export_surface_init_py_change():
    files = ["sapianta_core/__init__.py"]
    diff = make_unified_diff(
        "sapianta_core/__init__.py",
        removed=["from .validator import validate"],
        added=["from .validator import validate, validate_v2"],
    )
    final, ev = classify(files, diff)
    assert final == PG.Severity.STRUCTURAL
    assert "S3" in evidence_ids(ev)


def test_structural_S3_export_surface_all_assignment():
    files = ["sapianta_core/mod.py"]
    diff = make_unified_diff(
        "sapianta_core/mod.py",
        removed=["__all__ = ['a']"],
        added=["__all__ = ['a', 'b']"],
    )
    final, ev = classify(files, diff)
    assert final == PG.Severity.STRUCTURAL
    assert "S3" in evidence_ids(ev)


def test_no_false_positive_S3_on_plain_mention_outside_core():
    files = ["src/foo.py"]
    diff = make_unified_diff(
        "src/foo.py",
        removed=["text = '__all__ is mentioned here'"],
        added=["text = '__all__ is still mentioned here'"],
    )
    final, ev = classify(files, diff)
    # Not structural: should not match S3 since it's outside sapianta_core
    assert final != PG.Severity.STRUCTURAL
    assert "S3" not in evidence_ids(ev)


def test_parametric_P1_config_value_change_yaml():
    files = ["runtime/domains/credit/policy.yaml"]
    diff = make_unified_diff(
        "runtime/domains/credit/policy.yaml",
        removed=["max_dti: 0.35"],
        added=["max_dti: 0.40"],
    )
    final, ev = classify(files, diff)
    assert final == PG.Severity.PARAMETRIC
    assert "P1" in evidence_ids(ev)


def test_parametric_P2_numeric_value_only_change_non_core():
    files = ["runtime/domains/credit/thresholds.py"]
    diff = make_unified_diff(
        "runtime/domains/credit/thresholds.py",
        removed=["max_age = 65"],
        added=["max_age = 67"],
    )
    final, ev = classify(files, diff)
    assert final == PG.Severity.PARAMETRIC
    assert "P2" in evidence_ids(ev)


def test_cosmetic_C1_docs_only():
    files = ["docs/README.md"]
    diff = make_unified_diff(
        "docs/README.md",
        removed=["Old text"],
        added=["New text"],
    )
    final, ev = classify(files, diff)
    assert final == PG.Severity.COSMETIC
    assert "C1" in evidence_ids(ev)


def test_cosmetic_C2_comment_whitespace_only():
    files = ["src/example.py"]
    diff = make_unified_diff(
        "src/example.py",
        removed=["# old comment", ""],
        added=["# new comment", ""],
    )
    final, ev = classify(files, diff)
    assert final == PG.Severity.COSMETIC
    assert "C2" in evidence_ids(ev)


def test_structural_beats_parametric_when_both_present():
    # Tripwire file changed + config changed -> STRUCTURAL must win
    files = [
        "tools/governance/promotion_gate_v02.py",
        "runtime/domains/credit/policy.yaml",
    ]
    diff = (
        make_unified_diff(
            "tools/governance/promotion_gate_v02.py",
            removed=["x = 1"],
            added=["x = 2"],
        )
        + "\n"
        + make_unified_diff(
            "runtime/domains/credit/policy.yaml",
            removed=["max_dti: 0.35"],
            added=["max_dti: 0.40"],
        )
    )
    final, ev = classify(files, diff)
    assert final == PG.Severity.STRUCTURAL
    assert "S1" in evidence_ids(ev)

    # -----------------------------
# Fail-Closed Test (DiffCollector)
# -----------------------------

def test_fail_closed_on_git_diff_error(monkeypatch, capsys):
    """
    If git diff returns non-zero exit code,
    classifier MUST fail closed and classify as STRUCTURAL.
    """

    class DummyResult:
        def __init__(self):
            self.returncode = 1
            self.stdout = ""
            self.stderr = "fatal error"

    def fake_run(*args, **kwargs):
        return DummyResult()

    # Patch subprocess.run inside module
    monkeypatch.setattr(PG.subprocess, "run", fake_run)

    collector = PG.DiffCollector("HEAD~1..HEAD")

    with pytest.raises(SystemExit) as exc:
        collector.changed_files()

    # Exit code must be 1
    assert exc.value.code == 1

    captured = capsys.readouterr()

    assert "Change Classification: STRUCTURAL" in captured.out
    assert "FAIL-CLOSED" in captured.out
