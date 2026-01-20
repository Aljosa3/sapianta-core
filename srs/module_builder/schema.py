from typing import TypedDict, Dict


class ModuleSpec(TypedDict):
    module_id: str
    module_name: str
    module_version: str
    layer: str
    files: Dict[str, str]


def check_schema(spec: ModuleSpec) -> None:
    raise NotImplementedError("Schema validation not implemented")
