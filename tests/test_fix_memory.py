from runtime.development.fix_memory import FixMemory


def test_fix_memory_learns_best_strategy():
    memory = FixMemory()

    error_text = "TypeError: missing argument"

    # simulate success history
    for _ in range(5):
        memory.record_success(error_text, "strategy_a")

    for _ in range(2):
        memory.record_success(error_text, "strategy_b")

    best = memory.get_best_strategy(error_text)

    assert best == "strategy_a", f"Expected strategy_a, got {best}"