import json
from datetime import datetime

class CertificationRegistry:
    def __init__(self, path="runtime/development/ccs/cert_registry.json"):
        self.path = path
        self._data = self._load()

    def _load(self):
        try:
            with open(self.path, "r") as f:
                return json.load(f)
        except:
            return {}

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self._data, f, indent=2)

    def set_status(self, file_path, status):
        self._data[file_path] = {
            "status": status,
            "timestamp": datetime.utcnow().isoformat()
        }
        self.save()

    def get_status(self, file_path):
        return self._data.get(file_path)