from tests.validation.test_validator_harness import run_test, _write


def setup(root: str):
    _write(
        f"{root}/runtime/module_x/code.py",
        "import subprocess\n",
    )
    _write(
        f"{root}/runtime/module_x/spec.md",
        "illegal doc",
    )

build_plan = {
    "paths": [
        "runtime/module_x",
        "runtime/module_y",  # manjkajoča
    ]
}

run_test(
    name="FAIL / combined structural + policy",
    build_plan=build_plan,
    setup_fn=setup,
)
