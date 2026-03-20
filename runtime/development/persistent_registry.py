import json
import os
import hashlib
from typing import Dict, Any, Tuple


REGISTRY_PATH = "runtime/development/.function_registry.json"


def _stable_serialize(data: Any) -> str:
    """Deterministic serialization"""
    return json.dumps(data, sort_keys=True, separators=(",", ":"))


def _hash(data: Any) -> str:
    return hashlib.sha256(_stable_serialize(data).encode()).hexdigest()


class PersistentRegistry:

    def __init__(self):
        self.function_map: Dict[str, Any] = {}
        self.dependency_graph: Dict[str, Any] = {}
        self.snapshot_hash: str = ""

    # -------------------------------------------------
    # LOAD / SAVE
    # -------------------------------------------------

    def load(self) -> bool:
        if not os.path.exists(REGISTRY_PATH):
            return False

        with open(REGISTRY_PATH, "r") as f:
            data = json.load(f)

        self.function_map = data.get("function_map", {})
        self.dependency_graph = data.get("dependency_graph", {})
        self.snapshot_hash = data.get("snapshot_hash", "")

        return True

    def save(self):
        data = {
            "function_map": self.function_map,
            "dependency_graph": self.dependency_graph,
            "snapshot_hash": self.compute_hash()
        }

        os.makedirs(os.path.dirname(REGISTRY_PATH), exist_ok=True)

        with open(REGISTRY_PATH, "w") as f:
            json.dump(data, f, indent=2, sort_keys=True)

    # -------------------------------------------------
    # HASHING
    # -------------------------------------------------

    def compute_hash(self) -> str:
        return _hash({
            "function_map": self.function_map,
            "dependency_graph": self.dependency_graph
        })

    # -------------------------------------------------
    # UPDATE
    # -------------------------------------------------

    def update(self, function_map: Dict, dependency_graph: Dict):
        self.function_map = function_map
        self.dependency_graph = dependency_graph
        self.snapshot_hash = self.compute_hash()

    # -------------------------------------------------
    # DIFF ENGINE
    # -------------------------------------------------

    def diff(self, new_function_map: Dict, new_dependency_graph: Dict) -> Dict[str, Any]:
        old_funcs = set(self.function_map.keys())
        new_funcs = set(new_function_map.keys())

        added = list(new_funcs - old_funcs)
        removed = list(old_funcs - new_funcs)

        changed = []

        for fn in old_funcs & new_funcs:
            if _hash(self.function_map[fn]) != _hash(new_function_map[fn]):
                changed.append(fn)

        dep_changed = _hash(self.dependency_graph) != _hash(new_dependency_graph)

        return {
            "added": sorted(added),
            "removed": sorted(removed),
            "changed": sorted(changed),
            "dependency_changed": dep_changed,
            "has_changes": bool(added or removed or changed or dep_changed)
        }