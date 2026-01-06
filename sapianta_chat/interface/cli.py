from sapianta_chat.routing import ChatRouter
from sapianta_chat.orchestrator import ChatOrchestrator


class ChatCLI:
    def __init__(self):
        self.router = ChatRouter()
        self.orchestrator = ChatOrchestrator()

    def run_once(self, user_input: str) -> str:
        request = self.router.route(user_input)
        response = self.orchestrator.handle(request)
        return response.response_text


if __name__ == "__main__":
    cli = ChatCLI()
    try:
        while True:
            user_input = input("> ")
            if user_input.lower() in {"exit", "quit"}:
                break
            output = cli.run_once(user_input)
            print(output)
    except KeyboardInterrupt:
        pass
