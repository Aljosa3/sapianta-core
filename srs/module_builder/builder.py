from srs.module_builder.schema import ModuleSpec, check_schema
from srs.module_builder.validator import validate_igl
from srs.module_builder.emitter import emit_module, EmittedArtifacts
from srs.module_builder.errors import SchemaError, IGLValidationError


def build_module(spec: ModuleSpec) -> EmittedArtifacts:
    check_schema(spec)

    result = validate_igl(spec)
    if not result["ok"]:
        raise IGLValidationError("; ".join(result["errors"]))

    return emit_module(spec)
