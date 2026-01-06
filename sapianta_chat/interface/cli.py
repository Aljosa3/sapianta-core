from sapianta_chat.routing import ChatRouter
from sapianta_chat.orchestrator import ChatOrchestrator
from sapianta_chat.output import CLIOutputRenderer, OutputExporter


class ChatCLI:
    def __init__(self):
        self.router = ChatRouter()
        self.orchestrator = ChatOrchestrator()
        self.renderer = CLIOutputRenderer()
        self.exporter = OutputExporter()

        self.mode = "text"
        self.detail = "full"
        self._last_response = None

    def run_once(self, user_input: str) -> str:
        request = self.router.route(user_input)
        response = self.orchestrator.handle(request)
        self._last_response = response
        return self.renderer.render(
            response,
            mode=self.mode,
            detail=self.detail,
        )

    def handle_command(self, user_input: str) -> bool:
        if user_input.startswith(":mode"):
            parts = user_input.split()
            if len(parts) == 2 and parts[1] in {"text", "markdown", "json"}:
                self.mode = parts[1]
                print(f"(mode set to {self.mode})")
            else:
                print("Usage: :mode text|markdown|json")
            return True

        if user_input.startswith(":detail"):
            parts = user_input.split()
            if len(parts) == 2 and parts[1] in {"short", "normal", "full"}:
                self.detail = parts[1]
                print(f"(detail set to {self.detail})")
            else:
                print("Usage: :detail short|normal|full")
            return True

        if user_input.startswith(":export"):
            parts = user_input.split(maxsplit=2)
            if len(parts) != 3:
                print("Usage: :export markdown|json <path>")
                return True

            if self._last_response is None:
                print("Nothing to export yet.")
                return True

            mode, path = parts[1], parts[2]
            try:
                self.exporter.export(
                    self._last_response,
                    path=path,
                    mode=mode,
                    detail=self.detail,
                )
                print(f"(exported {mode} to {path})")
            except Exception as e:
                print(f"Export failed: {e}")

            return True

        return False


if __name__ == "__main__":
    cli = ChatCLI()
    try:
        while True:
            user_input = input("> ")
            if user_input.lower() in {"exit", "quit"}:
                break

            if cli.handle_command(user_input):
                continue

            output = cli.run_once(user_input)
            print(output)

    except KeyboardInterrupt:
        pass
