from pathlib import Path
from typing import Dict, List

# READ-ONLY canonical view
# - bere modules/
# - bere izpeljano canonical state
# - ne piše
# - ne sklepa


def list_modules(modules_root: Path) -> List[str]:
    if not modules_root.exists() or not modules_root.is_dir():
        return []

    names = []
    for p in sorted(modules_root.iterdir()):
        if p.is_dir():
            names.append(p.name)
    return names


def canonical_view(modules_root: Path, canonical_state: Dict[str, str]) -> Dict[str, Dict[str, str]]:
    """
    Vrne pogled:
    {
      "<module_name>": {
          "exists": "yes|no",
          "status": "<STATUS>|UNKNOWN"
      }
    }
    """
    view = {}

    modules = set(list_modules(modules_root))
    state_keys = set(canonical_state.keys())

    # moduli, ki obstajajo na disku
    for m in modules:
        view[m] = {
            "exists": "yes",
            "status": canonical_state.get(m, "UNKNOWN")
        }

    # kanonični zapisi brez fizičnega modula
    for k in state_keys - modules:
        view[k] = {
            "exists": "no",
            "status": canonical_state[k]
        }

    return view
