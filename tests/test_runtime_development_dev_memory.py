from runtime.development.dev_memory import DevMemory


def test_dev_memory_records():

    memory = DevMemory()

    task = {
        "task_type": "implementation",
        "idea": "add feature x",
    }

    memory.record_completed(task)

    stats = memory.stats()

    assert stats["completed"] == 1
    assert stats["failed"] == 0
    assert stats["blocked"] == 0