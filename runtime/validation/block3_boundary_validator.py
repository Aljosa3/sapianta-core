# /home/pisarna/work/sapianta/sapianta_system/runtime/validation/block3_boundary_validator.py

import re


class Block3BoundaryViolation(Exception):
    pass


class Block3BoundaryValidator:

    # Forbidden patterns in Explanation (normative language)
    EXPLANATION_FORBIDDEN = [
        r"\brecommend\b",
        r"\bshould\b",
        r"\bprobably\b",
        r"\bconsider\b",
        r"\bsuggest\b",
        r"\bmaybe\b",
        r"\bi think\b",
        r"\bin my opinion\b",
        r"\bit would be better\b",
    ]

    # Forbidden patterns in Deliberation (deterministic causality claims)
    DELIBERATION_FORBIDDEN = [
        r"\brule\s+[a-zA-Z0-9_-]+\b",
        r"\btriggered\b",
        r"\bthreshold\b",
        r"\bpolicy requires\b",
        r"\bengine decided because\b",
        r"\bdeterministic proof\b",
        r"\baccording to rule\b",
    ]

    @staticmethod
    def _check_patterns(text: str, patterns: list, context: str):
        lower_text = text.lower()

        for pattern in patterns:
            if re.search(pattern, lower_text):
                raise Block3BoundaryViolation(
                    f"[Block3BoundaryViolation] {context} contains forbidden pattern: {pattern}"
                )

    @classmethod
    def validate_explanation(cls, explanation_text: str):
        cls._check_patterns(
            explanation_text,
            cls.EXPLANATION_FORBIDDEN,
            context="Explanation"
        )

    @classmethod
    def validate_deliberation(cls, deliberation_text: str):
        cls._check_patterns(
            deliberation_text,
            cls.DELIBERATION_FORBIDDEN,
            context="Deliberation"
        )