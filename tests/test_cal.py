from runtime.development.dev_autonomous_loop import DevAutonomousLoop


def test_cal_generates_and_executes_task():
    loop = DevAutonomousLoop(reset=True)

    result = loop.run_once()

    # preveri da sistem ne crasha
    assert result is not None

    # preveri da CAL pipeline dela
    assert result.get("status") in ["completed", "no_tasks"]

    # če je task izveden, mora imeti strukturo
    if result.get("status") == "completed":
        task = result.get("task")
        assert task is not None
        assert "description" in task
        assert "metadata" in task