class ModuleBuilder:
    def __init__(self, canon: dict):
        self.canon = canon

    def prepare(self, request: dict) -> dict:
        return prepare_build_task(request, self.canon)


def prepare_build_task(request: dict, canon: dict) -> dict:
    return {
        "instruction": (
            "Generate Python module code ONLY. "
            "Follow CanonRules strictly. "
            "Do NOT add documentation. Do NOT modify existing files."
        ),
        "canon": canon,
        "request": request,
        "constraints": [
            "No new .md files",
            "No runtime entry points",
            "No imports of wiring.py",
        ],
    }
