def test_fix_ranking():

    from runtime.development.strategy_selector import StrategySelector

    selector = StrategySelector()

    fixes = [
        {"strategy": "safe_fallback", "confidence": 0.1},
        {"strategy": "name_error_stub", "confidence": 0.9},
        {"strategy": "syntax_fix", "confidence": 0.5},
    ]

    ranked = selector.rank(fixes)

    assert ranked[0]["strategy"] == "name_error_stub"
    assert ranked[1]["strategy"] == "syntax_fix"
    assert ranked[2]["strategy"] == "safe_fallback"