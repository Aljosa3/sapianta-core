from runtime.governance.promotion_gate import classify_change


def test_return_change_is_parametric():

    diff = """
- return False
+ return {"success": True}
"""

    result = classify_change(
        ["runtime/development/dev_orchestrator.py"],
        diff
    )

    assert result == "PARAMETRIC"


def test_no_diff_is_cosmetic():

    result = classify_change(
        ["runtime/development/dev_orchestrator.py"]
    )

    assert result == "COSMETIC"