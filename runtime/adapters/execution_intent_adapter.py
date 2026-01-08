from runtime.models.execution_intent import ExecutionIntent


class ExecutionIntentAdapter:
    """
    Adapter med zunanjim vnosom in ExecutionIntent modelom.
    """

    def adapt(self, raw_input):
        """
        Pretvori surov vhod v ExecutionIntent.
        """
        return ExecutionIntent(payload=raw_input)
