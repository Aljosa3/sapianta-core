# PATH: sapianta_chat/execution/prompt_renderer.py

import json


class ClaudePromptRenderer:
    """
    Deterministic prompt renderer (v0.17).

    HARD REQUIREMENTS:
    - Output MUST use FILE-based protocol
    - No markdown, no explanations, no prose
    - Any deviation causes HARD build failure
    """

    PROMPT_HEADER = (
        "You are an execution backend.\n"
        "You MUST follow the build plan exactly.\n\n"
        "OUTPUT FORMAT IS STRICT AND MACHINE-READABLE.\n\n"
        "You MUST output ONLY the following format:\n\n"
        "FILE: <relative/path>\n"
        "<file content>\n\n"
        "Repeat FILE blocks for each file.\n\n"
        "FORBIDDEN:\n"
        "- Markdown fences (```)\n"
        "- Explanations or prose\n"
        "- Comments outside FILE blocks\n"
        "- Any text outside FILE blocks\n\n"
        "If you violate this format, the build will FAIL.\n\n"
        "=== SAPIANTA BUILD PLAN START ===\n"
    )

    PROMPT_FOOTER = "\n=== SAPIANTA BUILD PLAN END ===\n"

    @classmethod
    def render(cls, build_plan: dict) -> str:
        # Deterministic JSON rendering (no interpretation)
        plan_json = json.dumps(
            build_plan,
            indent=2,
            sort_keys=True,
            ensure_ascii=False,
        )
        return f"{cls.PROMPT_HEADER}{plan_json}{cls.PROMPT_FOOTER}"
