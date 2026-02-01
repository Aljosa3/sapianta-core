from typing import List
from sapianta_chat.validation.build_validator import ValidationResult

class RepairPlanGenerator:
    """
    Generates a human-readable repair plan.
    Does NOT modify code.
    """

    def __init__(self, issues: List[str]):
        self.issues = issues

    @classmethod
    def from_validation(cls, result: ValidationResult):
        return cls(result.errors)

    def print_plan(self):
        if not self.issues:
            return

        print("[REPAIR-PLAN] Suggested actions:")
        for issue in self.issues:
            print(f" * Review and fix: {issue}")
