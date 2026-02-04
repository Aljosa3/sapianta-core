# test_validator_v020_module_graph.py
#
# SAPIANTA v0.20
# Canonical validation tests for Module Graph Pass
#
# LOCATION:
#   /home/pisarna/sapianta_system/tests/validation/
#
# PURPOSE:
# - Validates v0.20 multi-file module support
# - Covers PASS + HARD FAIL scenarios
# - Integrated with existing validation test suite
#
# EXECUTION:
#   python tests/validation/test_validator_v020_module_graph.py
#   ali preko obstoječega run_validation.sh
#
# EXIT CODES:
#   0 = all tests behaved as expected
#   1 = unexpected PASS or FAIL


from sapianta_chat.validation.validator_pipeline_v020 import (
    ValidatorPipelineV020,
    ValidationHardFail,
)


# ---------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------

def run_test(name: str, files: dict, should_pass: bool) -> bool:
    print(f"\n=== {name} ===")
    try:
        ValidatorPipelineV020(files).run()
        if should_pass:
            print("RESULT: PASS (as expected)")
            return True
        else:
            print("RESULT: UNEXPECTED PASS ❌")
            return False
    except ValidationHardFail as e:
        if should_pass:
            print(f"RESULT: UNEXPECTED FAIL ❌ → {e}")
            return False
        else:
            print(f"RESULT: HARD FAIL (as expected) → {e}")
            return True


# ---------------------------------------------------------------------
# Test cases (aligned with PHASE_v0.20_TEST_MATRIX.md)
# ---------------------------------------------------------------------

def test_v020_pass_valid_multifile() -> bool:
    files = {
        "proof_multifile_v020/core.py": (
            "import utils\n"
            "import logic\n"
        ),
        "proof_multifile_v020/utils.py": (
            "import logic\n"
        ),
        "proof_multifile_v020/logic.py": (
            "# no imports\n"
        ),
    }
    return run_test(
        "TC-PASS-01 — VALID MULTI-FILE MODULE",
        files,
        should_pass=True,
    )


def test_v020_fail_circular_dependency() -> bool:
    files = {
        "proof_multifile_v020/core.py": "import utils\n",
        "proof_multifile_v020/utils.py": "import logic\n",
        "proof_multifile_v020/logic.py": "import core\n",
    }
    return run_test(
        "TC-FAIL-01 — CIRCULAR DEPENDENCY",
        files,
        should_pass=False,
    )


def test_v020_fail_out_of_module_import() -> bool:
    files = {
        "proof_multifile_v020/core.py": "import external_lib\n",
        "proof_multifile_v020/utils.py": "# no imports\n",
        "proof_multifile_v020/logic.py": "# no imports\n",
    }
    return run_test(
        "TC-FAIL-02 — OUT-OF-MODULE IMPORT",
        files,
        should_pass=False,
    )


def test_v020_fail_phantom_file_import() -> bool:
    files = {
        "proof_multifile_v020/core.py": "import missing\n",
        "proof_multifile_v020/utils.py": "# no imports\n",
        "proof_multifile_v020/logic.py": "# no imports\n",
    }
    return run_test(
        "TC-FAIL-03 — PHANTOM FILE IMPORT",
        files,
        should_pass=False,
    )


# ---------------------------------------------------------------------
# Optional standalone runner (kept for symmetry with existing tests)
# ---------------------------------------------------------------------

def main() -> None:
    results = [
        test_v020_pass_valid_multifile(),
        test_v020_fail_circular_dependency(),
        test_v020_fail_out_of_module_import(),
        test_v020_fail_phantom_file_import(),
    ]

    if all(results):
        print("\n✅ ALL v0.20 VALIDATOR TESTS PASSED")
        raise SystemExit(0)
    else:
        print("\n❌ VALIDATOR TEST FAILURE DETECTED")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
