"""
SAPIANTA Approval CLI (registry-based)
"""

from datetime import datetime, UTC


def approve():
    try:
        from runtime.development.dev_task_registry import DevTaskRegistry

        registry = DevTaskRegistry()

        # 🔥 dobi taske ki čakajo
        if not hasattr(registry, "get_tasks_by_state"):
            print("[APPROVAL] Registry does not support states")
            return

        waiting = registry.get_tasks_by_state("waiting_approval")

        if not waiting:
            print("[APPROVAL] No pending approvals")
            return

        # 🔥 FIX: vzemi NAJNOVEJŠI task (ne prvega!)
        task = waiting[-1]

        print("[APPROVAL] APPROVED:")
        print(task)

        # 🔥 pravilni update state-a
        registry.update_task_state(task, "approved")

        # dodatni metadata
        task["approved"] = True
        task["approved_at"] = datetime.now(UTC).isoformat()

        registry._persist()

        print("[APPROVAL] Task marked as approved")

    except Exception as e:
        print("[APPROVAL] Failed:", str(e))


def reject():
    try:
        from runtime.development.dev_task_registry import DevTaskRegistry

        registry = DevTaskRegistry()

        waiting = registry.get_tasks_by_state("waiting_approval")

        if not waiting:
            print("[APPROVAL] No pending approvals")
            return

        # 🔥 enak fix tudi tukaj
        task = waiting[-1]

        print("[APPROVAL] REJECTED:")
        print(task)

        registry.update_task_state(task, "failed")

    except Exception as e:
        print("[APPROVAL] Failed:", str(e))


def run(args):
    if not args:
        print("[APPROVAL] Usage: approve | reject")
        return

    command = args[0]

    if command == "approve":
        approve()
    elif command == "reject":
        reject()
    else:
        print("[APPROVAL] Unknown command")