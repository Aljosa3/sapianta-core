from runtime.development.auto_fix_engine import AutoFixEngine


def test_type_error_multiple_values(tmp_path):

    file = tmp_path / "mod.py"

    file.write_text(
        "def f(a):\n    return a\n",
        encoding="utf-8"
    )

    engine = AutoFixEngine()

    failure_info = {
        "error": "TypeError: f() got multiple values for argument 'a'",
        "file": str(file)
    }

    fixes = engine.generate_fixes(failure_info)

    # 🔥 UPDATED: support multiple strategies
    multi_fixes = [
        f for f in fixes
        if f.get("strategy") in [
            "type_error_multiple_values_fix_function",
            "type_error_multiple_values_fix_callsite",
            "type_error_multiple_values_fix_function_fallback"
        ]
    ]

    assert multi_fixes, "No multiple-values fix generated"

    fix = multi_fixes[0]

    # 🔥 only validate function-based fixes
    if fix["strategy"] != "type_error_multiple_values_fix_callsite":
        assert "a=None" in fix["code"]