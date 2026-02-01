from tests.validation.test_validator_harness import run_test, _write

def setup(root: str):
    # ustvarimo točno tiste poti, ki jih build_plan zahteva
    _write(
        f"{root}/runtime/module_a/main.py",
        "def hello():\n    return 'ok'\n",
    )
    _write(
        f"{root}/runtime/module_b/utils.py",
        "def util():\n    return 42\n",
    )

build_plan = {
    "paths": [
        "runtime/module_a",
        "runtime/module_b",
    ]
}

run_test(
    name="PASS / golden path (fully compliant build)",
    build_plan=build_plan,
    setup_fn=setup,
)
