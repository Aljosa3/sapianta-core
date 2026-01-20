from typing import TypedDict, List
from srs.module_builder.schema import ModuleSpec


class ValidationResult(TypedDict):
    ok: bool
    errors: List[str]


def validate_igl(spec: ModuleSpec) -> ValidationResult:
    raise NotImplementedError("IGL validation not implemented")
