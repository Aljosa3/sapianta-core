"""
SAPIANTA Development Metrics

Telemetry module for monitoring the autonomous development system.
"""

import json
import os
import time


METRICS_FILE = os.path.join(
    os.path.dirname(__file__),
    "dev_metrics.json"
)


class DevMetrics:

    def __init__(self):

        self._ensure_file()

        with open(METRICS_FILE, "r") as f:
            self.data = json.load(f)

    def _ensure_file(self):

        if not os.path.exists(METRICS_FILE):

            data = {
                "tasks_processed": 0,
                "tasks_completed": 0,
                "tasks_failed": 0,
                "tasks_blocked": 0,
                "total_execution_time": 0.0
            }

            with open(METRICS_FILE, "w") as f:
                json.dump(data, f, indent=2)

    def _persist(self):

        with open(METRICS_FILE, "w") as f:
            json.dump(self.data, f, indent=2)

    def record_cycle(self, status: str, execution_time: float):

        self.data["tasks_processed"] += 1
        self.data["total_execution_time"] += execution_time

        if status == "completed":
            self.data["tasks_completed"] += 1

        elif status == "failed":
            self.data["tasks_failed"] += 1

        elif status == "blocked":
            self.data["tasks_blocked"] += 1

        self._persist()

    def get_metrics(self):

        data = dict(self.data)

        # Backward compatibility with reconcile-generated metrics
        processed = data.get("tasks_processed", data.get("processed", 0))

        completed = data.get("tasks_completed", data.get("completed", 0))
        failed = data.get("tasks_failed", data.get("failed", 0))
        blocked = data.get("tasks_blocked", data.get("blocked", 0))

        total_execution_time = data.get("total_execution_time", 0)

        data["tasks_processed"] = processed
        data["tasks_completed"] = completed
        data["tasks_failed"] = failed
        data["tasks_blocked"] = blocked
        data["total_execution_time"] = total_execution_time

        if processed > 0:
            data["success_rate"] = completed / processed
            data["avg_execution_time"] = total_execution_time / processed
        else:
            data["success_rate"] = 0
            data["avg_execution_time"] = 0

        return data