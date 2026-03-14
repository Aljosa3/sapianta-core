"""
SAPIANTA Promotion Gate

Classifies development changes and determines
whether human approval is required.

Classification levels

COSMETIC
PARAMETRIC
STRUCTURAL
"""

STRUCTURAL_PATHS = [
    "runtime/system",
    "runtime/engine",
    "runtime/governance"
]

PARAMETRIC_PATHS = [
    "runtime/strategies",
    "runtime/analytics"
]


def classify_change(file_list):

    level = "COSMETIC"

    for path in file_list:

        for structural in STRUCTURAL_PATHS:

            if path.startswith(structural):
                return "STRUCTURAL"

        for param in PARAMETRIC_PATHS:

            if path.startswith(param):
                level = "PARAMETRIC"

    return level


def requires_approval(level):

    if level == "STRUCTURAL":
        return True

    if level == "PARAMETRIC":
        return True

    return False