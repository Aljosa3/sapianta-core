from runtime.development.dev_task_registry import DevTaskRegistry


def test_registry_task_lifecycle():

    registry = DevTaskRegistry(reset=True)

    task = {
        "task_type": "implementation",
        "idea": "add replay performance benchmark",
        "source": "sapianta_discuss",
    }

    registry.add_task(task)

    assert len(registry.get_active_tasks()) == 1

    registry.complete_task(task)

    assert len(registry.get_active_tasks()) == 0
    assert len(registry.get_completed_tasks()) == 1