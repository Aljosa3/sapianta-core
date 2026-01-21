"""
IO Adapter Module for SAPIANTA — REAL_MODULE_INTERFACE_INIT.

This module represents a real-world interface point.
It does not interpret data or perform validation.
"""


from sapianta.modules.base_interface import BaseModuleInterface


class IOAdapter(BaseModuleInterface):
    name = "io_adapter"

    def run(self, context):
        self.trace.record("io_adapter.run.start")

        # simulate external interaction (no real IO yet)
        context.set("io_status", "connected")

        self.trace.record("io_adapter.run.end")
