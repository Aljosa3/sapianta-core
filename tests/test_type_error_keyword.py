from runtime.development.auto_fix_engine import AutoFixEngine


def test_type_error_unexpected_keyword(tmp_path):

    file = tmp_path / "mod.py"

    file.write_text(
        "def f(a):\n    return a\n",
        encoding="utf-8"
    )

    engine = AutoFixEngine()

    failure_info = {
        "error": "TypeError: f() got an unexpected keyword argument 'b'",
        "file": str(file)
    }

    fixes = engine.generate_fixes(failure_info)

    keyword_fixes = [
        f for f in fixes if f.get("strategy") == "type_error_keyword_fix"
    ]

    assert keyword_fixes, "No keyword fix generated"

    fix = keyword_fixes[0]

    assert "b=None" in fix["code"]