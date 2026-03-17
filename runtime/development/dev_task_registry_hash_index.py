"""
SAPIANTA Development Task Registry Hash Index

Provides fast lookup of development task hashes.

Purpose:
Enable O(1) duplicate detection for development tasks.
"""

from typing import Set

from runtime.development.dev_task_hash import compute_task_hash


class DevTaskRegistryHashIndex:
    """
    Maintains a set of task hashes for fast duplicate detection.
    """

    def __init__(self):
        self._hashes: Set[str] = set()

    def add_task(self, task: dict) -> str:
        """
        Add a task hash to the index.
        """
        task_hash = compute_task_hash(task)
        self._hashes.add(task_hash)
        return task_hash

    def has_task(self, task: dict) -> bool:
        """
        Check if a task already exists in the index.
        """
        task_hash = compute_task_hash(task)
        return task_hash in self._hashes

    def remove_task(self, task: dict) -> None:
        """
        Remove a task from the index.
        """
        task_hash = compute_task_hash(task)
        if task_hash in self._hashes:
            self._hashes.remove(task_hash)

    def size(self) -> int:
        """
        Number of indexed tasks.
        """
        return len(self._hashes)