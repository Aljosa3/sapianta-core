from runtime.development.test_runner import TestRunner
from runtime.development.architecture_guardian import ArchitectureGuardian
from runtime.development.ccs.certification_registry import CertificationRegistry


class CertificationEngine:
    def __init__(self):
        self.registry = CertificationRegistry()
        self.guardian = ArchitectureGuardian()

    def certify(self, file_path):

        # 1. Guardian check (minimal fix: use validate instead of non-existing validate_file)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                code = f.read()
        except Exception:
            self.registry.set_status(file_path, "REJECTED")
            return "REJECTED"

        validation = self.guardian.validate(file_path, code)

        if not validation.get("success", False):
            self.registry.set_status(file_path, "REJECTED")
            return "REJECTED"

        # 2. Test validation (minimal fix: replace invalid import with TestRunner)
        runner = TestRunner(project_root=".", timeout=10)
        diagnostics = runner.run_tests()

        if not diagnostics.success:
            self.registry.set_status(file_path, "REJECTED")
            return "REJECTED"

        # 3. Success
        self.registry.set_status(file_path, "CERTIFIED")
        return "CERTIFIED"