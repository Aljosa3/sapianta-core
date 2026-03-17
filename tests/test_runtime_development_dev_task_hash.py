from runtime.development.dev_task_hash import compute_task_hash, is_duplicate


def test_task_hash_is_deterministic():

    task = {
        "task_type": "implementation",
        "idea": "Add replay benchmark",
        "source": "sapianta_discuss",
    }

    h1 = compute_task_hash(task)
    h2 = compute_task_hash(task)

    assert h1 == h2


def test_duplicate_detection():

    task = {
        "task_type": "implementation",
        "idea": "Add replay benchmark",
        "source": "sapianta_discuss",
    }

    task_hash = compute_task_hash(task)

    existing = {task_hash}

    assert is_duplicate(task, existing)