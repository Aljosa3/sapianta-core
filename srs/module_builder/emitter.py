from typing import TypedDict, Dict
from srs.module_builder.schema import ModuleSpec


class EmittedArtifacts(TypedDict):
    paths: Dict[str, str]


def emit_module(spec: ModuleSpec) -> EmittedArtifacts:
    raise NotImplementedError("Module emission not implemented")
