"""
Base interface for real modules in SAPIANTA.

A real module:
- interfaces with an external system
- performs IO or data exchange
- does NOT interpret meaning
- does NOT make decisions
"""


class BaseModuleInterface:
    name = "base_module_interface"

    def __init__(self, trace):
        self.trace = trace

    def run(self, context):
        """
        Execute the module.

        Must be implemented by subclasses.
        """
        raise NotImplementedError(
            "Real modules must implement the run(context) method."
        )
