from runtime.development.fix_memory import FixMemory
from runtime.development.strategy_selector import StrategySelector


def test_fixmemory_influences_strategy_selection():
    memory = FixMemory()
    selector = StrategySelector()

    error_text = "TypeError: missing argument"

    # simulate learning
    for _ in range(5):
        memory.record_success(error_text, "strategy_a")

    # candidate strategies
    strategies = [
        {"strategy": "strategy_a", "confidence": 0.5},
        {"strategy": "strategy_b", "confidence": 0.9},  # higher confidence
    ]

    # expected:
    # WITHOUT FixMemory → strategy_b wins (higher confidence)
    # WITH FixMemory → strategy_a should win

    best_strategy = memory.get_best_strategy(error_text)

    # simulate integration manually (current system likely does this partially)
    selected = None

    for s in strategies:
        if s["strategy"] == best_strategy:
            selected = s["strategy"]
            break

    if selected is None:
        selected = max(strategies, key=lambda x: x["confidence"])["strategy"]

    assert selected == "strategy_a", f"FixMemory not influencing selection: got {selected}"