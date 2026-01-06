import json
from sapianta_chat.models import ChatResponse


class CLIOutputRenderer:
    def render(self, response: ChatResponse, mode: str = "text") -> str:
        if mode == "markdown":
            return self._render_markdown(response)
        if mode == "json":
            return self._render_json(response)
        return self._render_text(response)

    def _render_text(self, response: ChatResponse) -> str:
        lines = []
        lines.append(response.response_text)

        metadata = response.metadata or {}
        plan = metadata.get("plan")

        if plan and plan.get("steps"):
            lines.append("")
            lines.append("Načrt (konceptualno):")
            for idx, step in enumerate(plan["steps"], start=1):
                lines.append(f"{idx}. {step.get('title', '')}")
                desc = step.get("description")
                if desc:
                    lines.append(f"   - {desc}")

        return "\n".join(lines)

    def _render_markdown(self, response: ChatResponse) -> str:
        lines = []
        lines.append("### Odgovor")
        lines.append("")
        lines.append(response.response_text)

        metadata = response.metadata or {}
        plan = metadata.get("plan")

        if plan and plan.get("steps"):
            lines.append("")
            lines.append("### Načrt (konceptualno)")
            for idx, step in enumerate(plan["steps"], start=1):
                lines.append(f"{idx}. **{step.get('title', '')}**")
                desc = step.get("description")
                if desc:
                    lines.append(f"   - {desc}")

        return "\n".join(lines)

    def _render_json(self, response: ChatResponse) -> str:
        payload = {
            "response_text": response.response_text,
            "response_type": response.response_type,
            "metadata": response.metadata,
        }
        return json.dumps(payload, indent=2, ensure_ascii=False)
