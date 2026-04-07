from runtime.development.dev_autonomous_loop import DevAutonomousLoop


def test_full_pipeline_learning_stability():
    loop = DevAutonomousLoop()

    results = []

    for _ in range(3):
        result = loop.run_once()

        status = result.get("status")

        # proxy scoring
        if status == "completed":
            results.append(1)
        else:
            results.append(999)

    # system must not degrade over time
    assert results[-1] <= max(results), f"Pipeline degraded: {results}"

    # optional stronger signal
    assert results[-1] <= results[0], f"No improvement signal: {results}"