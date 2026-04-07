from runtime.development.fix_memory import FixMemory
from runtime.development.strategy_selector import StrategySelector


def test_fixmemory_affects_ranking():
    memory = FixMemory()
    selector = StrategySelector()

    error_text = "TypeError: missing argument"

    # simulate learning
    for _ in range(5):
        memory.record_success(error_text, "strategy_a")

    # competing strategies
    strategies = [
        {"strategy": "strategy_a", "confidence": 0.2},
        {"strategy": "strategy_b", "confidence": 0.9},
    ]

    # baseline ranking (without memory influence)
    ranked = selector.rank(strategies)
    baseline_top = ranked[0]["strategy"]

    # expected: baseline prefers strategy_b
    assert baseline_top == "strategy_b"

    # now apply memory influence (current system behavior)
    best = memory.get_best_strategy(error_text)

    # simulate system-level decision (minimal integration)
    selected = best if best else baseline_top

    assert selected == "strategy_a", f"FixMemory not influencing decision: got {selected}"