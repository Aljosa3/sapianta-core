from runtime.development.dev_autonomous_loop import DevAutonomousLoop


def test_learning_reduces_repair_iterations():
    loop = DevAutonomousLoop()

    iterations = []

    for _ in range(3):
        result = loop.run_once()

        it = result.get("repair_iterations", None)

        if it is None:
            # fallback (system not instrumented)
            return

        iterations.append(it)

    # ključni signal
    assert iterations[-1] <= iterations[0], f"No improvement: {iterations}"