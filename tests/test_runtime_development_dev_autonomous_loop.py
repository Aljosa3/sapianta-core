from runtime.development.dev_autonomous_loop import DevAutonomousLoop


def test_autonomous_loop_basic():

    loop = DevAutonomousLoop()

    task = {
        "task_type": "implementation",
        "idea": "add experimental feature",
        "source": "sapianta_discuss",
    }

    status = loop.submit_task(task)

    assert status == "registered"

    result = loop.run_once()

    assert result["status"] in ["completed", "needs_review"]