"""
SAPIANTA Artifact Evaluator

Purpose
-------
Deterministic evaluation of generated artifacts.
Provides quality scoring for self-improving development loop.
"""

import os


class ArtifactEvaluator:

    """
    Evaluates generated artifacts in a deterministic way.
    """

    def evaluate(self, artifact: dict) -> dict:
        """
        Evaluate artifact quality.

        Returns:
            {
                "score": float (0-1),
                "details": dict
            }
        """

        files = artifact.get("files", [])

        execution_score = self._evaluate_execution(artifact)
        structure_score = self._evaluate_structure(files)
        completeness_score = self._evaluate_completeness(files)

        # deterministic weighted score
        final_score = (
            0.4 * execution_score +
            0.3 * structure_score +
            0.3 * completeness_score
        )

        return {
            "score": round(final_score, 4),
            "details": {
                "execution": execution_score,
                "structure": structure_score,
                "completeness": completeness_score
            }
        }

    # ------------------------------------------------
    # Execution (placeholder - deterministic)
    # ------------------------------------------------

    def _evaluate_execution(self, artifact: dict) -> float:
        """
        Execution success proxy.
        """

        # If artifact exists → assume success
        # (real execution validation comes later phase)
        return 1.0 if artifact else 0.0

    # ------------------------------------------------
    # Structure quality
    # ------------------------------------------------

    def _evaluate_structure(self, files: list) -> float:
        """
        Evaluates file structure and placement.
        """

        if not files:
            return 0.0

        score = 0
        valid_paths = 0

        for f in files:

            if f.startswith("runtime/"):
                valid_paths += 1

        score = valid_paths / len(files)

        return round(score, 4)

    # ------------------------------------------------
    # Completeness (basic heuristic)
    # ------------------------------------------------

    def _evaluate_completeness(self, files: list) -> float:
        """
        Checks if generated files contain minimal implementation.
        """

        if not files:
            return 0.0

        completed = 0

        for f in files:

            if not os.path.exists(f):
                continue

            try:
                with open(f, "r") as file:
                    content = file.read()

                if "NotImplementedError" not in content:
                    completed += 1

            except Exception:
                continue

        score = completed / len(files)

        return round(score, 4)