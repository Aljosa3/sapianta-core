#!/usr/bin/env python3

import os
import sys
import ast

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KERNEL_DIR = os.path.join(PROJECT_ROOT, "sapianta_hoi")

FORBIDDEN_IMPORTS = {
    "random",
    "time",
    "datetime",
    "uuid",
    "requests",
    "socket",
    "subprocess",
    "threading",
    "multiprocessing",
}

FORBIDDEN_ATTRIBUTE_CALLS = {
    ("os", "system"),
    ("os", "popen"),
    ("time", "sleep"),
}

def scan_file(file_path):
    violations = []

    with open(file_path, "r", encoding="utf-8") as f:
        try:
            tree = ast.parse(f.read())
        except SyntaxError:
            return []

    for node in ast.walk(tree):

        # Check imports
        if isinstance(node, ast.Import):
            for alias in node.names:
                root_module = alias.name.split(".")[0]
                if root_module in FORBIDDEN_IMPORTS:
                    violations.append(
                        f"Forbidden import '{root_module}' in {file_path}"
                    )

        if isinstance(node, ast.ImportFrom):
            if node.module:
                root_module = node.module.split(".")[0]
                if root_module in FORBIDDEN_IMPORTS:
                    violations.append(
                        f"Forbidden import '{root_module}' in {file_path}"
                    )

        # Check forbidden attribute calls
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Attribute):
                if isinstance(node.func.value, ast.Name):
                    module_name = node.func.value.id
                    func_name = node.func.attr
                    if (module_name, func_name) in FORBIDDEN_ATTRIBUTE_CALLS:
                        violations.append(
                            f"Forbidden call '{module_name}.{func_name}' in {file_path}"
                        )

        # Check os.environ usage
        if isinstance(node, ast.Attribute):
            if (
                isinstance(node.value, ast.Name)
                and node.value.id == "os"
                and node.attr == "environ"
            ):
                violations.append(
                    f"Forbidden access 'os.environ' in {file_path}"
                )

    return violations


def main():
    all_violations = []

    for root, _, files in os.walk(KERNEL_DIR):
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                violations = scan_file(full_path)
                all_violations.extend(violations)

    if all_violations:
        print("\nKERNEL DETERMINISM VIOLATIONS DETECTED:\n")
        for v in all_violations:
            print(" -", v)
        print("\nDeterminism enforcement failed.")
        sys.exit(1)

    print("Kernel determinism check passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
