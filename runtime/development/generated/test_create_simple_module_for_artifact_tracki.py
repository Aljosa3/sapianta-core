
from create_simple_module_for_artifact_tracki import CreateSimpleModuleForArtifactTracki


def test_basic():
    instance = CreateSimpleModuleForArtifactTracki()
    result = instance.run({})
    assert result is not None
