from runtime.development.discuss_dev_bridge import DiscussDevBridge


def test_bridge_creates_task():

    bridge = DiscussDevBridge()

    task = bridge.create_dev_task("create replay performance test")

    assert task["task_type"] == "implementation"
    assert task["source"] == "sapianta_discuss"