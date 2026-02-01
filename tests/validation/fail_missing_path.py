from tests.validation.test_validator_harness import run_test

def setup(root: str):
    # namenoma ničesar ne ustvarimo
    pass

build_plan = {
    "paths": [
        "runtime/module_a",
        "runtime/module_b",  # MANJKA
    ]
}

run_test(
    name="FAIL / missing expected path",
    build_plan=build_plan,
    setup_fn=setup,
)
