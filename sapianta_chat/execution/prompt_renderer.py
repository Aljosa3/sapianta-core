import json


class ClaudePromptRenderer:
    """
    Deterministic prompt renderer.

    - No interpretation
    - No reformatting of plan content
    - Stable output for identical input
    """

    PROMPT_HEADER = (
        "You are an execution backend.\n"
        "You MUST follow the build plan exactly.\n"
        "Do NOT add explanations.\n"
        "Do NOT validate.\n"
        "Do NOT fix errors.\n"
        "Return ONLY the generated content.\n\n"
        "=== SAPIANTA BUILD PLAN START ===\n"
    )

    PROMPT_FOOTER = "\n=== SAPIANTA BUILD PLAN END ===\n"

    @classmethod
    def render(cls, build_plan: dict) -> str:
        plan_json = json.dumps(build_plan, indent=2, sort_keys=True)
        return f"{cls.PROMPT_HEADER}{plan_json}{cls.PROMPT_FOOTER}"
