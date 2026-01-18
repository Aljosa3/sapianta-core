"""
Context Carrier for SAPIANTA — CODEBASE_INIT.

The Context object is a passive data container.
It carries information through the runtime flow
without making decisions or interpretations.
"""


class Context:
    def __init__(self):
        # internal storage for arbitrary data
        self._data = {}

    def set(self, key, value):
        """
        Store a value in the context.
        No validation, no interpretation.
        """
        self._data[key] = value

    def get(self, key, default=None):
        """
        Retrieve a value from the context.
        Returns default if key is not present.
        """
        return self._data.get(key, default)

    def items(self):
        """
        Return all stored context items.
        """
        return self._data.items()

    def __repr__(self):
        return f"<Context keys={list(self._data.keys())}>"
