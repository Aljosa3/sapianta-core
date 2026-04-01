def test_ftl_targets_correct_file():

    from runtime.development.auto_fix_engine import AutoFixEngine

    engine = AutoFixEngine()

    failure_info = {
        "success": False,
        "error": "assert add(2, 3) == 10",
        "test_output": "",
        "file": "runtime/development/generated/test_add_failure.py"
    }

    fixes = engine.generate_fixes(failure_info)

    # mora obstajati fix za add
    assert any(f.get("function") == "add" for f in fixes)

    # 🔥 KLJUČNO: file NE SME biti test file
    for f in fixes:
        if f.get("function") == "add":
            assert "test_" not in f.get("file", ""), f"Wrong target file: {f.get('file')}"