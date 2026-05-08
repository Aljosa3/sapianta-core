import re
from pathlib import Path


class TestIntentExtractor:

    @staticmethod
    def extract(test_dir="runtime/development/generated"):
        results = []

        test_path = Path(test_dir)

        if not test_path.exists():
            return results

        for file in test_path.glob("test_*.py"):
            try:
                content = file.read_text()
            except Exception:
                continue

            matches = re.findall(
                r"assert\s+(\w+)\((.*?)\)\s*==\s*(\d+)",
                content
            )

            for func, args, expected in matches:
                try:
                    args_list = [int(x.strip()) for x in args.split(",")]
                    results.append({
                        "function": func,
                        "args": args_list,
                        "expected": int(expected)
                    })
                except Exception:
                    continue

        return results
