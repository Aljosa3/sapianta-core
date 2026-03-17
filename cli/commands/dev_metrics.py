"""
SAPIANTA CLI — Development Metrics

Displays runtime metrics for the development pipeline.
"""

from runtime.development.dev_metrics import DevMetrics


def run() -> None:

    metrics = DevMetrics()

    data = metrics.get_metrics()

    processed = data.get("tasks_processed", 0)
    completed = data.get("tasks_completed", 0)
    failed = data.get("tasks_failed", 0)
    blocked = data.get("tasks_blocked", 0)
    total_time = data.get("total_execution_time", 0)

    if processed == 0:
        print("\nNo development metrics recorded.")
        return

    success_rate = (completed / processed) * 100 if processed else 0
    avg_time = total_time / processed if processed else 0

    print("\nSAPIANTA Development Metrics")
    print("-----------------------------")

    print(f"Tasks processed: {processed}")
    print(f"Completed: {completed}")
    print(f"Failed: {failed}")
    print(f"Blocked: {blocked}")
    print(f"Success rate: {success_rate:.2f}%")
    print(f"Avg execution time: {avg_time:.4f}s")