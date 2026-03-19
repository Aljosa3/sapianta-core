import re


class FunctionPatcher:

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

            # skip empty lines
            if not line.strip():
                continue

            current_indent = len(line) - len(line.lstrip())

            # end when indentation goes back OR same level
            if current_indent <= indent:
                break

            end_idx = i + 1

        # --------------------------------------------
        # SAFETY: REMOVE TRAILING GARBAGE RETURNS
        # (fix for your exact bug)
        # --------------------------------------------
        cleaned_lines = []

        for i, line in enumerate(lines):
            # skip orphan return outside function
            if i > start_idx and line.strip().startswith("return") and (
                len(line) - len(line.lstrip())
            ) == 0:
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

        # ensure newline at end
        return "\n".join(new_lines).rstrip() + "\n"