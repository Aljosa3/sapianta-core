from runtime.development.strategy_selector import StrategySelector


def test_strategy_selection():

    selector = StrategySelector()

    low = selector.select({"score": 0.2})
    high = selector.select({"score": 0.8})

    assert low == "fallback"
    assert high == "standard"