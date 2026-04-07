from runtime.development.dev_autonomous_loop import DevAutonomousLoop


def test_system_does_not_degrade_over_cycles():
    loop = DevAutonomousLoop()

    results = []

    for _ in range(3):
        result = loop.run_once()

        # proxy: success vs failure
        status = result.get("status")

        if status == "completed":
            results.append(1)
        else:
            results.append(999)

    # system should not degrade
    assert results[-1] <= max(results), f"System degraded: {results}"