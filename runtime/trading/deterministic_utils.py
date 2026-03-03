"""
Deterministic utility functions for governance-bound trading engine.
All functions must be deterministic and replay-safe.
"""

import hashlib
import json
import numpy as np
from types import MappingProxyType


def deterministic_normalize(obj):
    """
    Recursively normalize object for deterministic serialization.

    - Sorts dict keys
    - Normalizes lists and tuples
    - Converts numpy scalars to native Python types

    Args:
        obj: Object to normalize

    Returns:
        Deterministically normalized representation
    """

    if isinstance(obj, dict):
        return {k: deterministic_normalize(obj[k]) for k in sorted(obj.keys())}

    elif isinstance(obj, (list, tuple)):
        return [deterministic_normalize(item) for item in obj]

    elif isinstance(obj, (np.integer, np.floating)):
        return obj.item()

    else:
        return obj


def stable_hash(obj) -> str:
    """
    Compute deterministic SHA256 hash of object.

    - Canonical JSON serialization
    - Sorted keys
    - No whitespace differences
    - UTF-8 encoded

    Args:
        obj: Object to hash (must be JSON-serializable after normalization)

    Returns:
        SHA256 hash as hexadecimal string
    """

    normalized = deterministic_normalize(obj)

    canonical = json.dumps(
        normalized,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False
    )

    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def freeze_config(obj):
    """
    Recursively convert dict to immutable MappingProxyType.
    Lists are converted to tuples.
    This protects runtime config from mutation.
    """

    if isinstance(obj, dict):
        return MappingProxyType({k: freeze_config(v) for k, v in obj.items()})

    elif isinstance(obj, list):
        return tuple(freeze_config(i) for i in obj)

    else:
        return obj