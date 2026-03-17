from runtime.development.dev_task_planner import DevTaskPlanner


def test_task_prioritization():

    planner = DevTaskPlanner()

    tasks = [
        {
            "task_type": "implementation",
            "idea": "add feature x"
        },
        {
            "task_type": "bugfix",
            "idea": "fix replay crash"
        }
    ]

    ordered = planner.prioritize(tasks)

    assert ordered[0]["task_type"] == "bugfix"