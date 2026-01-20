from srs.module_builder.builder import build_module
from srs.module_builder.schema import ModuleSpec
from srs.module_builder.errors import ModuleBuilderError


def guarded_build(spec: ModuleSpec):
    """
    Claude Code MUST call this function.
    Any failure propagates and stops execution.
    """
    try:
        return build_module(spec)
    except ModuleBuilderError:
        raise
