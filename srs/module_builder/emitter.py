from typing import TypedDict, Dict
from pathlib import Path

from srs.module_builder.schema import ModuleSpec
from srs.module_builder.errors import EmissionError


class EmittedArtifacts(TypedDict):
    paths: Dict[str, str]


MANIFEST_NAME = ".module_builder_manifest"
MANIFEST_CONTENT = "CREATED_BY: SAPIANTA_MODULE_BUILDER\n"


def emit_module(spec: ModuleSpec) -> EmittedArtifacts:
    """
    Minimal emission:
    - creates module directory
    - writes manifest file
    """

    try:
        module_path = Path(spec["module_id"])
        module_path.mkdir(parents=True, exist_ok=False)

        manifest_path = module_path / MANIFEST_NAME
        manifest_path.write_text(MANIFEST_CONTENT)

        return {
            "paths": {
                "module_dir": str(module_path),
                "manifest": str(manifest_path),
            }
        }

    except Exception as exc:
        raise EmissionError(str(exc)) from exc
