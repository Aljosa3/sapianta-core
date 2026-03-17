"""
SAPIANTA Development Memory

Stores historical outcomes of development tasks.

Purpose:
Allow the development system to learn from past
successes and failures.
"""


class DevMemory:
    """
    Simple in-memory development history.
    """

    def __init__(self):

        self.completed = []
        self.failed = []
        self.blocked = []

    def record_completed(self, task: dict):

        self.completed.append(task)

    def record_failed(self, task: dict):

        self.failed.append(task)

    def record_blocked(self, task: dict):

        self.blocked.append(task)

    def get_completed(self):

        return list(self.completed)

    def get_failed(self):

        return list(self.failed)

    def get_blocked(self):

        return list(self.blocked)

    def stats(self):

        return {
            "completed": len(self.completed),
            "failed": len(self.failed),
            "blocked": len(self.blocked),
        }