"""
SAPIANTA Plan Engine

Generates structured multi-step plans from a high-level goal.
"""


class PlanEngine:

    def generate_plan(self, goal: str):

        # 🔥 V1: deterministic simple decomposition
        # (kasneje pride LLM / intelligent planner)

        base = goal.lower().replace(" ", "_")

        return [
            {
                "goal": f"{goal} - logging module",
                "priority": 1,
                "file_hint": f"{base}_logging"
            },
            {
                "goal": f"{goal} - config system",
                "priority": 1,
                "file_hint": f"{base}_config"
            },
            {
                "goal": f"{goal} - validation module",
                "priority": 1,
                "file_hint": f"{base}_validation"
            },
            {
                "goal": f"{goal} - error handling",
                "priority": 1,
                "file_hint": f"{base}_error"
            },
            {
                "goal": f"{goal} - file processing",
                "priority": 1,
                "file_hint": f"{base}_file"
            },
        ]