# runtime/development/integrity_validator.py

import os
import re


class IntegrityValidator:
    INVALID_PATTERN = re.compile(r"[\n\r\t]")

    def validate_path(self, path: str):
        if not path:
            raise ValueError("Empty path not allowed")

        if self.INVALID_PATTERN.search(path):
            raise ValueError(f"Invalid characters in path: {path}")

        normalized = os.path.normpath(path)

        if normalized.startswith(".."):
            raise ValueError(f"Path escapes project root: {path}")

        return normalized

    def validate_fix(self, fix: dict):
        """
        Expect fix = { 'path': ..., 'content': ... }
        """
        if "path" not in fix or "content" not in fix:
            raise ValueError("Fix must contain path and content")

        fix["path"] = self.validate_path(fix["path"])

        return fix