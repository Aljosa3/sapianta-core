from tests.validation.test_validator_harness import run_test, _write


def setup(root: str):
    _write(
        f"{root}/runtime/module_a/main.py",
        "import openai\nprint('nope')\n",
    )

build_plan = {
    "paths": [
        "runtime/module_a",
    ]
}

run_test(
    name="FAIL / forbidden import",
    build_plan=build_plan,
    setup_fn=setup,
)
