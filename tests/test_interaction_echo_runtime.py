from runtime.interaction_registry import INTERACTION_REGISTRY


def test_interaction_echo_runtime():
    handler = INTERACTION_REGISTRY["interaction.echo"]
    payload = {"a": 1, "b": [1, 2, 3]}

    assert handler(payload) == payload
