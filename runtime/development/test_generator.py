# PATH: sapianta_system/runtime/development/test_generator.py

"""
SAPIANTA Automated Test Generator

Generates pytest skeleton tests for modules
that currently lack test coverage.

Pipeline:

SystemReflectionEngine
        ↓
missing_tests
        ↓
pytest skeleton generation
"""

from pathlib import Path

from runtime.system.system_reflection_engine import SystemReflectionEngine


class TestGenerator:

    def __init__(self, repo_path="."):

        self.repo_path = Path(repo_path)
        self.engine = SystemReflectionEngine(repo_path)

    # ---------------------------------------------------------
    # FIND MODULES WITHOUT TESTS
    # ---------------------------------------------------------

    def get_missing_test_modules(self):

        report = self.engine.analyze()

        return report["missing_tests"]

    # ---------------------------------------------------------
    # GENERATE TEST FILE CONTENT
    # ---------------------------------------------------------

    def generate_test_content(self, module_path):

        # remove module prefix if present
        if module_path.startswith("module:"):
            module_path = module_path.replace("module:", "")

        safe_name = module_path.replace(".", "_")

        content = f"""
import importlib


def test_import_{safe_name}():

    module_path = "{module_path}"

    module = importlib.import_module(module_path)

    assert module is not None


def test_placeholder_{safe_name}():
    # TODO: implement real test
    assert True
"""

        return content.strip()

    # ---------------------------------------------------------
    # GENERATE TEST FILE
    # ---------------------------------------------------------

    def generate_test_file(self, module_path):

        module_path = str(module_path)

        if module_path.startswith("module:"):
            module_path = module_path.replace("module:", "")

        safe_name = module_path.replace(".", "_")

        test_file_name = f"test_{safe_name}.py"

        tests_dir = self.repo_path / "tests"
        tests_dir.mkdir(exist_ok=True)

        test_path = tests_dir / test_file_name

        content = self.generate_test_content(module_path)

        with open(test_path, "w") as f:
            f.write(content)

        return str(test_path)

    # ---------------------------------------------------------
    # GENERATE TESTS FOR ALL MISSING MODULES
    # ---------------------------------------------------------

    def generate_all_tests(self, limit=None):

        modules = self.get_missing_test_modules()

        if limit:
            modules = modules[:limit]

        generated = []

        for module in modules:

            try:

                test_file = self.generate_test_file(module)

                generated.append(test_file)

            except Exception as e:

                print(f"Failed to generate test for {module}: {e}")

        return generated

    # ---------------------------------------------------------
    # CLI REPORT
    # ---------------------------------------------------------

    def print_generation_report(self, limit=5):

        modules = self.get_missing_test_modules()

        print("\nSAPIANTA Test Generation")
        print("------------------------")

        print(f"\nModules lacking tests: {len(modules)}")

        print(f"\nGenerating tests (limit={limit})...\n")

        generated = self.generate_all_tests(limit=limit)

        for g in generated:
            print("Generated:", g)