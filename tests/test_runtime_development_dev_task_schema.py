from runtime.development.dev_task_schema import validate_task


def test_dev_task_schema_validation():

    task = {
        "task_type": "implementation",
        "idea": "create replay performance test",
        "source": "sapianta_discuss",
    }

    assert validate_task(task)