# PATH: tests/conftest.py

import sys
from pathlib import Path
import pytest

# =====================================================
# PATH SETUP (obstoječe - ohranjeno)
# =====================================================

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

# =====================================================
# DEV ORCHESTRATOR FIXTURE (NOVO)
# =====================================================

from runtime.development.dev_orchestrator import DevelopmentOrchestrator


@pytest.fixture
def dev_orchestrator():
    return DevelopmentOrchestrator()