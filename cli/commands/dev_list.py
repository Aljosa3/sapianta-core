"""
SAPIANTA CLI — List Development Tasks

Displays tasks tracked in DevTaskRegistry.
"""

from runtime.development.dev_task_registry import DevTaskRegistry


# ---------------------------------------------------------
# FORMATTER (human-readable output + normalization)
# ---------------------------------------------------------

def format_task(t):

    # -----------------------------
    # normalize fields
    # -----------------------------
    goal = t.get("goal") or t.get("idea") or "unknown"

    task_id = t.get("id")
    if not task_id:
        task_id = "no-id"

    priority = t.get("priority")
    if not priority:
        priority = "-"

    task_type = t.get("task_type", "task")

    # skrajšaj ID za preglednost
    short_id = task_id[:8] if isinstance(task_id, str) else "no-id"

    return f"[{short_id}] {goal} (p={priority}) | {task_type}"


# ---------------------------------------------------------
# CLI ENTRYPOINT
# ---------------------------------------------------------

def run(args):

    registry = DevTaskRegistry()

    active = registry.get_active_tasks()
    completed = registry.get_completed_tasks()
    rejected = registry.get_rejected_tasks()

    # -----------------------------
    # optional limit
    # -----------------------------
    limit = None

    for i, arg in enumerate(args):
        if arg == "--limit" and i + 1 < len(args):
            try:
                limit = int(args[i + 1])
            except:
                pass

    if limit:
        active = active[:limit]
        completed = completed[:limit]
        rejected = rejected[:limit]

    # -----------------------------
    # print
    # -----------------------------
    print("\nSAPIANTA Development Tasks")
    print("--------------------------")

    print(f"\nACTIVE TASKS ({len(active)})")
    if not active:
        print("- none")
    else:
        for t in active:
            print(f"- {format_task(t)}")

    print(f"\nCOMPLETED TASKS ({len(completed)})")
    if not completed:
        print("- none")
    else:
        for t in completed:
            print(f"- {format_task(t)}")

    print(f"\nREJECTED TASKS ({len(rejected)})")
    if not rejected:
        print("- none")
    else:
        for t in rejected:
            print(f"- {format_task(t)}")