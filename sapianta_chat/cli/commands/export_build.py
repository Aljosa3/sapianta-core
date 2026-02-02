import json
import os

def export_build(build_plan: dict, target_path: str):
    os.makedirs(os.path.dirname(target_path), exist_ok=True)

    with open(target_path, "w", encoding="utf-8") as fh:
        json.dump(build_plan, fh, indent=2)

    print(f"[BUILD] Exported build plan to {target_path}")
