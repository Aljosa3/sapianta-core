"""
SAPIANTA Idea Detector

Detects development ideas inside discuss sessions
and converts them into development tasks.
"""

TRIGGERS = [
    "implement",
    "add feature",
    "create module",
    "add command",
    "build",
    "implement this",
]


def detect_idea(text: str):

    text = text.lower()

    for trigger in TRIGGERS:
        if trigger in text:
            return True

    return False