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


# =========================================================
# 🔥 NEW: DIFF ANALYSIS
# =========================================================

def contains_return_change(diff_text: str) -> bool:

    if not diff_text:
        return False

    lines = diff_text.splitlines()

    for line in lines:
        if line.startswith("+") or line.startswith("-"):
            if "return" in line:
                return True

    return False


# =========================================================
# CLASSIFICATION
# =========================================================

def classify_change(file_list, diff_text=None):

    # 🔥 PRIORITY RULE: LOGIC CHANGE
    if diff_text and contains_return_change(diff_text):
        return "PARAMETRIC"

    level = "COSMETIC"

    for path in file_list:

        for structural in STRUCTURAL_PATHS:
            if path.startswith(structural):
                return "STRUCTURAL"

        for param in PARAMETRIC_PATHS:
            if path.startswith(param):
                level = "PARAMETRIC"

    return level


# =========================================================
# APPROVAL LOGIC
# =========================================================

def requires_approval(level):

    if level == "STRUCTURAL":
        return True

    if level == "PARAMETRIC":
        return True

    return False