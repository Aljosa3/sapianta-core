#!/usr/bin/env python3

import os
import sys
import ast

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LAYER_MAP = {
    "sapianta_hoi": 0,
    "sapianta_boundary": 1,
    "sapianta_advisory": 2,
    "sapianta_audit": 2,
    "sapianta_validation": 2,
    "sapianta_regression": 2,
    "sapianta_integration": 3,
    "sapianta_cli": 3,
}

def determine_layer(module_path):
    for prefix, layer in LAYER_MAP.items():
        if module_path.startswith(prefix):
            return layer
    return None

def extract_imports(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            tree = ast.parse(f.read())
        except SyntaxError:
            return []

    imports = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.append(node.module)

    return imports

def scan():
    violations = []

    for root, _, files in os.walk(PROJECT_ROOT):
        for file in files:
            if not file.endswith(".py"):
                continue

            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, PROJECT_ROOT)
            module_path = rel_path.replace(os.sep, ".").rstrip(".py")

            current_layer = determine_layer(module_path)
            if current_layer is None:
                continue

            imports = extract_imports(full_path)

            for imp in imports:
                target_layer = determine_layer(imp)
                if target_layer is None:
                    continue

                # Illegal upward import
                if target_layer > current_layer:
                    violations.append(
                        f"Illegal import: {module_path} (Layer {current_layer}) "
                        f"-> {imp} (Layer {target_layer})"
                    )

    return violations

def main():
    violations = scan()

    if violations:
        print("\nKERNEL LAYER DEPENDENCY VIOLATIONS DETECTED:\n")
        for v in violations:
            print(" -", v)
        print("\nDependency model violation.")
        sys.exit(1)

    print("Layer dependency check passed.")
    sys.exit(0)

if __name__ == "__main__":
    main()
