from runtime.development.strategy_selector import StrategySelector


def test_select_fallback():
    selector = StrategySelector()

    result = selector.select({"score": 0.2})

    assert result == "fallback"


def test_select_standard():
    selector = StrategySelector()

    result = selector.select({"score": 0.8})

    assert result == "standard"


def test_select_default_score():
    selector = StrategySelector()

    result = selector.select({})

    assert result == "fallback"  # default score = 0