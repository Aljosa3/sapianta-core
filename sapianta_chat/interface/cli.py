# PATH: sapianta_chat/interface/cli.py

from sapianta_chat.output.renderer import CLIOutputRenderer
from sapianta_chat.output.exporter import OutputExporter
from sapianta_chat.wiring import delegate_to_hoi

from sapianta_chat.interface.cli_proposal_gate import proposal_gate
from sapianta_chat.output.build_plan_exporter import export_build_plan


class ChatCLI:
    def __init__(self):
        self.renderer = CLIOutputRenderer()
        self.exporter = OutputExporter()

        self.mode = "text"
        self.detail = "full"
        self._last_response = None

    def run_once(self, user_input: str) -> str:
        response = delegate_to_hoi(user_input)
        response = proposal_gate(response)

        self._last_response = response

        return self.renderer.render(
            response,
            mode=self.mode,
            detail=self.detail,
        )

    # ---------------- COMMANDS ----------------

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

        if user_input.startswith(":export-build"):
            parts = user_input.split(maxsplit=1)
            if len(parts) != 2:
                print("Usage: :export-build <path>")
                return True

            if self._last_response is None:
                print("No build proposal to export.")
                return True

            try:
                export_build_plan(
                    reviewed_response=self._last_response,
                    path=parts[1],
                )
                print(f"(build plan exported to {parts[1]})")
            except Exception as e:
                print(f"Export failed: {e}")

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

        if user_input == ":state":
            self._print_state()
            return True

        return False

    # ---------------- STATE ----------------

    def _print_state(self) -> None:
        print("=== SAPIANTA STATE (read-only) ===")
        print(f"Mode: {self.mode}")
        print(f"Detail: {self.detail}")

        if self._last_response is None:
            print("Last response: NO")
            return

        print("Last response: YES")

    # ---------------- MAIN ----------------


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
