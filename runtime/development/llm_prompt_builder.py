"""
LLM Prompt Builder (Deterministic Layer)

Purpose:
- standardize prompt structure
- improve output consistency
- reduce randomness
"""


class LLMPromptBuilder:

    def build(self, task: dict) -> str:
        goal = task.get("goal", "").strip()

        return f"""
You are a deterministic Python code generator.

STRICT RULES:
- return ONLY valid Python code
- no explanations
- no markdown
- no comments outside code
- no filesystem access
- no subprocess, exec, eval
- no dynamic imports
- function must be deterministic

OUTPUT REQUIREMENTS:
- define at least one function
- function must be runnable
- no syntax errors
- minimal implementation

TASK:
{goal}
"""