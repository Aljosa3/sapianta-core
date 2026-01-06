import json
from sapianta_chat.models import ChatResponse


class CLIOutputRenderer:
    def render(
        self,
        response: ChatResponse,
        mode: str = "text",
        detail: str = "full",
    ) -> str:
        if mode == "markdown":
            return self._render_markdown(response, detail)
        if mode == "json":
            return self._render_json(response, detail)
        return self._render_text(response, detail)

    # ---------- TEXT ----------

    def _render_text(self, response: ChatResponse, detail: str) -> str:
        lines = []
        lines.append(response.response_text)

        if detail == "short":
            return "\n".join(lines)

        metadata = response.metadata or {}
        plan = metadata.get("plan")

        if detail in {"normal", "full"} and plan and plan.get("steps"):
            lines.append("")
            lines.append("Načrt (konceptualno):")

            for idx, step in enumerate(plan["steps"], start=1):
                title = step.get("title", "")
                lines.append(f"{idx}. {title}")

                if detail == "full":
                    desc = step.get("description")
                    if desc:
                        lines.append(f"   - {desc}")

        return "\n".join(lines)

    # ---------- MARKDOWN ----------

    def _render_markdown(self, response: ChatResponse, detail: str) -> str:
        lines = []
        lines.append("### Odgovor")
        lines.append("")
        lines.append(response.response_text)

        if detail == "short":
            return "\n".join(lines)

        metadata = response.metadata or {}
        plan = metadata.get("plan")

        if detail in {"normal", "full"} and plan and plan.get("steps"):
            lines.append("")
            lines.append("### Načrt (konceptualno)")

            for idx, step in enumerate(plan["steps"], start=1):
                title = step.get("title", "")
                lines.append(f"{idx}. **{title}**")

                if detail == "full":
                    desc = step.get("description")
                    if desc:
                        lines.append(f"   - {desc}")

        return "\n".join(lines)

    # ---------- JSON ----------

    def _render_json(self, response: ChatResponse, detail: str) -> str:
        payload = {
            "response_text": response.response_text,
            "response_type": response.response_type,
            "metadata": {},
        }

        metadata = response.metadata or {}
        plan = metadata.get("plan")

        if detail == "short":
            payload["metadata"] = {}
        elif detail == "normal":
            if plan and plan.get("steps"):
                payload["metadata"]["plan"] = {
                    "steps": [{"title": s.get("title")} for s in plan["steps"]]
                }
        else:  # full
            payload["metadata"] = metadata

        return json.dumps(payload, indent=2, ensure_ascii=False)
