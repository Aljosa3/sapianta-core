from runtime.engine.dry_run_engine import DryRunEngine
from runtime.adapters.cli_adapter import CLIRuntimeAdapter
from runtime.adapters.execution_intent_adapter import ExecutionIntentAdapter
from runtime.models.runtime_context import RuntimeContext


class RuntimeWiring:
    """
    Povezuje runtime komponente v enoten dry-run tok.
    """

    def __init__(self):
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
