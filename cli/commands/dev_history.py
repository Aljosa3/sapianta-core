"""
SAPIANTA Development History Command

Displays execution history from DevMetrics (execution_log)
with filtering support.
"""

from runtime.development.dev_metrics import DevMetrics
from datetime import datetime


# ---------------------------------------------------------
# FORMATTER
# ---------------------------------------------------------

def format_entry(entry):

    goal = entry.get("goal", "unknown")

    task_id = entry.get("task_id") or "no-id"
    short_id = task_id[:8] if isinstance(task_id, str) else "no-id"

    status = entry.get("status", "-")
    exec_time = round(entry.get("execution_time", 0), 4)

    # timestamp
    ts = entry.get("timestamp")
    try:
        time_str = datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        time_str = "unknown"

    # error (če obstaja)
    error_msg = ""
    error = entry.get("error")

    if error:
        stderr = error.get("stderr", "")
        error_msg = f" | error: {stderr[:60]}"

    return f"[{time_str}] [{short_id}] {goal} | {status} | {exec_time}s{error_msg}"


# ---------------------------------------------------------
# CLI ENTRYPOINT
# ---------------------------------------------------------

def run(args):

    metrics = DevMetrics()
    data = metrics.get_metrics()

    log = data.get("execution_log", [])

    print()
    print("SAPIANTA Execution History")
    print("--------------------------")

    if not log:
        print("No execution history available.")
        print()
        return

    # -----------------------------
    # DEFAULTS
    # -----------------------------
    limit = 10
    mode = "all"

    # -----------------------------
    # ARG PARSING (robustno)
    # -----------------------------
    if args:
        for i, arg in enumerate(args):

            if arg.isdigit():
                limit = int(arg)

            elif arg == "--failed":
                mode = "failed"

            elif arg == "--slow":
                mode = "slow"

            elif arg == "--limit" and i + 1 < len(args):
                try:
                    limit = int(args[i + 1])
                except:
                    pass

    # -----------------------------
    # FILTERING
    # -----------------------------
    entries = log

    if mode == "failed":
        entries = [e for e in log if e.get("status") == "failed"]

    elif mode == "slow":
        entries = [e for e in log if e.get("execution_time", 0) > 0.05]

    # -----------------------------
    # ORDER (latest first)
    # -----------------------------
    entries = list(reversed(entries))

    # -----------------------------
    # LIMIT
    # -----------------------------
    entries = entries[:limit]

    # -----------------------------
    # OUTPUT
    # -----------------------------
    for entry in entries:
        print(f"- {format_entry(entry)}")

    print()
    print(f"Showing {len(entries)} entries (mode={mode}, limit={limit}).")
    print()