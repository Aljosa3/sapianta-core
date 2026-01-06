from sapianta_chat.routing import ChatRouter
from sapianta_chat.orchestrator import ChatOrchestrator
from sapianta_chat.output import CLIOutputRenderer


class ChatCLI:
    def __init__(self):
        self.router = ChatRouter()
        self.orchestrator = ChatOrchestrator()
        self.renderer = CLIOutputRenderer()
        self.mode = "text"

    def run_once(self, user_input: str) -> str:
        request = self.router.route(user_input)
        response = self.orchestrator.handle(request)
        return self.renderer.render(response, mode=self.mode)

    def handle_command(self, user_input: str) -> bool:
        if user_input.startswith(":mode"):
            parts = user_input.split()
            if len(parts) == 2 and parts[1] in {"text", "markdown", "json"}:
                self.mode = parts[1]
                print(f"(mode set to {self.mode})")
            else:
                print("Usage: :mode text|markdown|json")
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
