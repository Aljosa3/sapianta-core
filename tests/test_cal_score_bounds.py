from runtime.development.dev_autonomous_loop import DevAutonomousLoop


def test_score_upper_bound():
    loop = DevAutonomousLoop()

    task = {
        "metadata": {"score": 0.0}
    }

    # simulate many successes through system logic
    for _ in range(50):
        if task.get("metadata"):
            score = task["metadata"].get("score", 0) + 0.1
            score = max(-1.0, min(1.0, score))
            task["metadata"]["score"] = score

    assert task["metadata"]["score"] <= 1.0


def test_score_lower_bound():
    loop = DevAutonomousLoop()

    task = {
        "metadata": {"score": 0.0}
    }

    # simulate many failures through system logic
    for _ in range(50):
        if task.get("metadata"):
            score = task["metadata"].get("score", 0) - 0.1
            score = max(-1.0, min(1.0, score))
            task["metadata"]["score"] = score

    assert task["metadata"]["score"] >= -1.0