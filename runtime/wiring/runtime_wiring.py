from pathlib import Path

from runtime.engine.dry_run_engine import DryRunEngine
from runtime.adapters.cli_adapter import CLIRuntimeAdapter
from runtime.adapters.execution_intent_adapter import ExecutionIntentAdapter
from runtime.models.runtime_context import RuntimeContext

from runtime.module_discovery import discover_modules


MODULES_ROOT = Path("modules")


class RuntimeWiring:
    """
    Povezuje runtime komponente v enoten dry-run tok.

    Pred kakršnimkoli runtime zagonom se izvede
    obvezna Module Builder admission validacija
    nad vsemi moduli v /modules.
    """

    def __init__(self):
        # 🔒 HARD GOVERNANCE ENFORCEMENT (DISCOVERY PHASE)
        for _module_dir in discover_modules(MODULES_ROOT):
            pass  # discovery is enforcement-only

        self.intent_adapter = ExecutionIntentAdapter()
        self.engine = DryRunEngine()
        self.cli = CLIRuntimeAdapter()
        self.context = RuntimeContext()

    def run_dry_run(self, raw_input, pretty=False):
        """
        Izvede celoten dry-run tok in vrne CLI izpis.
        """
        execution_intent = self.intent_adapter.adapt(raw_input)
        dry_run_result = self.engine.evaluate(execution_intent, self.context)

        if pretty:
            return self.cli.render_pretty(dry_run_result)

        return self.cli.render(dry_run_result)
