class CLIRuntimeAdapter:
    """
    Pretvori runtime rezultate v strukturiran CLI izpis.
    """

    def render(self, dry_run_result):
        return {
            "type": "DRY_RUN_RESULT",
            "status": (
                dry_run_result.status.value
                if dry_run_result.status is not None
                else None
            ),
            "details": dry_run_result.details,
            "meta": {
                "rendered_by": "CLIRuntimeAdapter",
                "version": "30A"
            }
        }

    def render_pretty(self, dry_run_result):
        lines = []
        lines.append("─" * 40)
        lines.append(" SAPIANTA · DRY-RUN RESULT")
        lines.append("─" * 40)
        lines.append(f"STATUS   : {dry_run_result.status.value}")
        lines.append(f"DETAILS  : {dry_run_result.details}")
        lines.append("─" * 40)
        return "\n".join(lines)
