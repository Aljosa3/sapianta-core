from .sink import RuntimeTraceSink
from .types import RuntimeTraceRecord


class ConsoleTraceSink(RuntimeTraceSink):
    """
    Simple console trace sink (development only).
    """

    def emit(self, record: RuntimeTraceRecord) -> None:
        print(
            f"[TRACE] decision={record.decision} "
            f"reason={record.reason} source={record.source}"
        )
