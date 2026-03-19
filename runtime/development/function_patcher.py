import re


class FunctionPatcher:

    # ------------------------------------------------
    # FUNCTION REPLACEMENT (EXISTING, STABLE)
    # ------------------------------------------------
    @staticmethod
    def replace_function(code: str, function_name: str, new_function_code: str) -> str:
        """
        Deterministic function replacement using indentation parsing.

        Fixes:
        - removes entire old function block
        - prevents 'return outside function'
        - avoids partial overwrite bugs
        """

        lines = code.split("\n")

        start_idx = None
        indent = None

        # --------------------------------------------
        # FIND FUNCTION START
        # --------------------------------------------
        for i, line in enumerate(lines):
            if re.match(rf"\s*def {function_name}\s*\(", line):
                start_idx = i
                indent = len(line) - len(line.lstrip())
                break

        # --------------------------------------------
        # FUNCTION NOT FOUND → APPEND SAFELY
        # --------------------------------------------
        if start_idx is None:
            return code.rstrip() + "\n\n" + new_function_code.rstrip() + "\n"

        # --------------------------------------------
        # FIND FUNCTION END (STRICT INDENT LOGIC)
        # --------------------------------------------
        end_idx = start_idx + 1

        for i in range(start_idx + 1, len(lines)):
            line = lines[i]

            if not line.strip():
                continue

            current_indent = len(line) - len(line.lstrip())

            if current_indent <= indent:
                break

            end_idx = i + 1

        # --------------------------------------------
        # SAFETY: REMOVE ORPHAN RETURNS (GLOBAL LEVEL)
        # --------------------------------------------
        cleaned_lines = []

        for i, line in enumerate(lines):
            if (
                i > start_idx
                and line.strip().startswith("return")
                and (len(line) - len(line.lstrip()) == 0)
            ):
                continue

            cleaned_lines.append(line)

        lines = cleaned_lines

        # --------------------------------------------
        # BUILD NEW CODE
        # --------------------------------------------
        new_function_lines = new_function_code.rstrip().split("\n")

        new_lines = (
            lines[:start_idx]
            + new_function_lines
            + lines[end_idx:]
        )

        return "\n".join(new_lines).rstrip() + "\n"

    # ------------------------------------------------
    # 🔥 CLASS-AWARE METHOD REPLACEMENT (NEW)
    # ------------------------------------------------
    @staticmethod
    def replace_method_in_class(
        code: str,
        class_name: str,
        method_name: str,
        new_method_code: str
    ) -> str:
        """
        Replace method inside a specific class using indentation parsing.
        Deterministic, no AST.
        """

        lines = code.split("\n")

        class_start = None
        class_indent = None

        # --------------------------------------------
        # FIND CLASS
        # --------------------------------------------
        for i, line in enumerate(lines):
            if re.match(rf"\s*class {class_name}\b", line):
                class_start = i
                class_indent = len(line) - len(line.lstrip())
                break

        if class_start is None:
            return code  # class not found → no-op

        # --------------------------------------------
        # FIND METHOD INSIDE CLASS
        # --------------------------------------------
        method_start = None
        method_indent = None

        for i in range(class_start + 1, len(lines)):
            line = lines[i]

            if not line.strip():
                continue

            current_indent = len(line) - len(line.lstrip())

            # left class block
            if current_indent <= class_indent:
                break

            if re.match(rf"\s*def {method_name}\s*\(", line):
                method_start = i
                method_indent = current_indent
                break

        if method_start is None:
            return code  # method not found → no-op

        # --------------------------------------------
        # FIND METHOD END
        # --------------------------------------------
        method_end = method_start + 1

        for i in range(method_start + 1, len(lines)):
            line = lines[i]

            if not line.strip():
                continue

            current_indent = len(line) - len(line.lstrip())

            if current_indent <= method_indent:
                break

            method_end = i + 1

        # --------------------------------------------
        # INDENT NEW METHOD CORRECTLY
        # --------------------------------------------
        indent_spaces = " " * method_indent

        new_method_lines = [
            indent_spaces + line if line.strip() else line
            for line in new_method_code.strip().split("\n")
        ]

        # --------------------------------------------
        # REPLACE METHOD
        # --------------------------------------------
        new_lines = (
            lines[:method_start]
            + new_method_lines
            + lines[method_end:]
        )

        return "\n".join(new_lines).rstrip() + "\n"