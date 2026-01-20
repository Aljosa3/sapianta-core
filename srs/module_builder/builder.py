from srs.module_builder.schema import ModuleSpec
from srs.module_builder.emitter import EmittedArtifacts


def build_module(spec: ModuleSpec) -> EmittedArtifacts:
    raise NotImplementedError("Module Builder orchestration not implemented")
