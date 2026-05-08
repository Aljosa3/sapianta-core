from runtime.development.ccs.certification_engine import CertificationEngine
from pathlib import Path


def test_ccs_rejects_without_test_evidence(tmp_path):

    file_path = tmp_path / "good.py"

    file_path.write_text(
        "def add(a, b):\n    return a + b\n"
    )

    engine = CertificationEngine()

    status = engine.certify(str(file_path))

    assert status == "REJECTED"


def test_ccs_rejected(tmp_path):

    file_path = tmp_path / "bad.py"

    file_path.write_text(
        "def add(a, b)\n    return a + b\n"  # SyntaxError
    )

    engine = CertificationEngine()

    status = engine.certify(str(file_path))

    assert status == "REJECTED"
