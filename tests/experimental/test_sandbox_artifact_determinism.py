# tests/experimental/test_sandbox_artifact_determinism.py

from experimental.sandbox_poc.artifact_builder import build_artifact


def test_artifact_determinism():
    prompt = "test prompt"
    response = "test response"
    diff = "test diff"
    scope = "NON_STRUCTURAL"
    iteration = 1

    artifact_1 = build_artifact(
        prompt_text=prompt,
        response_text=response,
        diff_text=diff,
        declared_scope=scope,
        iteration=iteration,
    )

    artifact_2 = build_artifact(
        prompt_text=prompt,
        response_text=response,
        diff_text=diff,
        declared_scope=scope,
        iteration=iteration,
    )

    # Entire artifact must be identical
    assert artifact_1 == artifact_2

    # Hash must be identical
    assert artifact_1["artifact_hash"] == artifact_2["artifact_hash"]