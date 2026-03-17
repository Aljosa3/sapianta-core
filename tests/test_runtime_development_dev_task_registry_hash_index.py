from runtime.development.dev_task_registry_hash_index import DevTaskRegistryHashIndex


def test_hash_index_add_and_detect():

    index = DevTaskRegistryHashIndex()

    task = {
        "task_type": "implementation",
        "idea": "Add replay benchmark",
        "source": "sapianta_discuss",
    }

    assert not index.has_task(task)

    index.add_task(task)

    assert index.has_task(task)


def test_hash_index_remove():

    index = DevTaskRegistryHashIndex()

    task = {
        "task_type": "implementation",
        "idea": "Add replay benchmark",
        "source": "sapianta_discuss",
    }

    index.add_task(task)

    assert index.has_task(task)

    index.remove_task(task)

    assert not index.has_task(task)