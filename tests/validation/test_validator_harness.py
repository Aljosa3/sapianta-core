import os
import shutil
import tempfile

from sapianta_chat.validation.build_validator import BuildValidator

FORBIDDEN_FILES = {".md"}
FORBIDDEN_IMPORTS = {"openai", "requests", "subprocess"}


def _write(path: str, content: str = ""):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def run_test(name: str, build_plan: dict, setup_fn):
    print(f"\n=== TEST: {name} ===")

    tmp = tempfile.mkdtemp(prefix="validator_test_")

    try:
        setup_fn(tmp)

        validator = BuildValidator(
            build_plan=build_plan,
            generated_root=tmp,
            forbidden_files=FORBIDDEN_FILES,
            forbidden_imports=FORBIDDEN_IMPORTS,
        )

        result = validator.validate()

        print(f"STATUS: {result.status}")
        for err in result.errors:
            print(f" - {err}")

    finally:
        shutil.rmtree(tmp)
