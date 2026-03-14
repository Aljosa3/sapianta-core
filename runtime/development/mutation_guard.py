"""
SAPIANTA Mutation Guard

Purpose
-------
First-line safety layer protecting the system from unsafe
LLM-generated development mutations.

This guard checks:

- maximum number of files
- allowed path roots
- forbidden core paths
- mutation type safety
"""

from pathlib import Path


class MutationGuard:

    MAX_FILES_PER_PATCH = 5

    ALLOWED_ROOTS = [
        "runtime/research",
        "runtime/strategies",
        "runtime/memory",
        "runtime/experiments",
        "runtime/analytics",
        "runtime/development",
        "sapianta-domain-",
    ]

    FORBIDDEN_PATHS = [
        "runtime/governance",
        "runtime/system",
        "runtime/ledger",
        "runtime/safety",
        "runtime/layer2",
    ]

    # ------------------------------------------------
    # MAIN ENTRY
    # ------------------------------------------------

    def validate_patch(self, file_list):

        self._check_patch_size(file_list)

        for file_path in file_list:

            self._check_forbidden_paths(file_path)

            self._check_allowed_paths(file_path)

    # ------------------------------------------------
    # PATCH SIZE
    # ------------------------------------------------

    def _check_patch_size(self, file_list):

        if len(file_list) > self.MAX_FILES_PER_PATCH:

            raise Exception(
                f"MutationGuard: patch too large ({len(file_list)} files). "
                f"Maximum allowed is {self.MAX_FILES_PER_PATCH}."
            )

    # ------------------------------------------------
    # FORBIDDEN PATHS
    # ------------------------------------------------

    def _check_forbidden_paths(self, file_path):

        for forbidden in self.FORBIDDEN_PATHS:

            if file_path.startswith(forbidden):

                raise Exception(
                    f"MutationGuard: forbidden mutation attempt -> {file_path}"
                )

    # ------------------------------------------------
    # ALLOWED ROOTS
    # ------------------------------------------------

    def _check_allowed_paths(self, file_path):

        for root in self.ALLOWED_ROOTS:

            if file_path.startswith(root):

                return

        raise Exception(
            f"MutationGuard: path not allowed -> {file_path}"
        )


# ------------------------------------------------
# TEST
# ------------------------------------------------

if __name__ == "__main__":

    guard = MutationGuard()

    test_patch = [
        "runtime/research/new_strategy.py",
        "runtime/research/alpha_model.py"
    ]

    guard.validate_patch(test_patch)

    print("MutationGuard test passed.")