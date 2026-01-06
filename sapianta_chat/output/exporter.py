from pathlib import Path
from sapianta_chat.models import ChatResponse
from sapianta_chat.output import CLIOutputRenderer


class OutputExporter:
    def __init__(self):
        self.renderer = CLIOutputRenderer()

    def export(
        self,
        response: ChatResponse,
        path: str,
        mode: str = "markdown",
        detail: str = "full",
    ) -> None:
        if mode not in {"markdown", "json"}:
            raise ValueError("Export mode must be 'markdown' or 'json'")

        content = self.renderer.render(
            response,
            mode=mode,
            detail=detail,
        )

        target = Path(path)
        target.write_text(content, encoding="utf-8")
