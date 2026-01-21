from typing import TypedDict, List, Any


class ModuleSpec(TypedDict):
    module_id: str
    layer: str
    capabilities: List[str]
    interfaces: List[str]


REQUIRED_KEYS = {
    "module_id": str,
    "layer": str,
    "capabilities": list,
    "interfaces": list,
}


def check_schema(spec: Any) -> None:
    """
    Minimal structural schema validation.
    No defaults.
    No coercion.
    No interpretation.
    """

    if not isinstance(spec, dict):
        raise TypeError("ModuleSpec must be a dict")

    for key, expected_type in REQUIRED_KEYS.items():
        if key not in spec:
            raise KeyError(f"Missing required key: {key}")

        if not isinstance(spec[key], expected_type):
            raise TypeError(
                f"Invalid type for key '{key}': expected {expected_type.__name__}"
            )

    # Explicitly forbid extra keys
    for key in spec.keys():
        if key not in REQUIRED_KEYS:
            raise KeyError(f"Unexpected key in ModuleSpec: {key}")
