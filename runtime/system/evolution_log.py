"""
SAPIANTA Evolution Log

Tracks the evolution of the system over time.

Records:
- new modules
- new capabilities
- architecture changes
- experiment outcomes
"""

import json
from datetime import datetime, UTC
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]

LOG_FILE = PROJECT_ROOT / "runtime/system/evolution_history.json"


class EvolutionLog:

    def __init__(self):

        if not LOG_FILE.exists():

            with open(LOG_FILE, "w") as f:

                json.dump([], f)

    # ---------------------------------------------------------
    # LOAD
    # ---------------------------------------------------------

    def load(self):

        with open(LOG_FILE) as f:

            return json.load(f)

    # ---------------------------------------------------------
    # SAVE
    # ---------------------------------------------------------

    def save(self, data):

        with open(LOG_FILE, "w") as f:

            json.dump(data, f, indent=2)

    # ---------------------------------------------------------
    # RECORD EVENT
    # ---------------------------------------------------------

    def record(self, event_type, payload):

        history = self.load()

        event = {

            "timestamp": datetime.now(UTC).isoformat(),

            "event": event_type,

            "payload": payload
        }

        history.append(event)

        self.save(history)

    # ---------------------------------------------------------
    # QUICK HELPERS
    # ---------------------------------------------------------

    def module_created(self, module):

        self.record(

            "module_created",

            {"module": module}

        )

    def capability_added(self, capability):

        self.record(

            "capability_added",

            {"capability": capability}

        )


# ---------------------------------------------------------
# TEST
# ---------------------------------------------------------

if __name__ == "__main__":

    log = EvolutionLog()

    log.module_created("runtime/portfolio/portfolio_engine.py")

    log.capability_added("portfolio_engine")

    print("\nEvolution event recorded.")