import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MODULES_DIR = REPO_ROOT / "modules"


def main():
    if not MODULES_DIR.exists():
        return  # no modules, nothing to check

    invalid = []

    for module_dir in MODULES_DIR.iterdir():
        if not module_dir.is_dir():
            continue

        manifest = module_dir / ".module_builder_manifest"
        if not manifest.exists():
            invalid.append(module_dir.name)

    if invalid:
        print("CI GUARD FAIL:")
        print("Modules without Module Builder manifest detected:")
        for name in invalid:
            print(f" - {name}")
        sys.exit(1)


if __name__ == "__main__":
    main()
