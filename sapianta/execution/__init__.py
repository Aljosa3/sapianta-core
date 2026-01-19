"""
Execution domain package.

Contains execution gates, decision/result types,
and execution adapters.

This package does not decide.
It only controls and performs (or simulates) execution.
"""

from .gate import ExecutionGate
from .types import ExecutionDecision, ExecutionResult
from .dry_run import DryRunExecutionAdapter

__all__ = [
    "ExecutionGate",
    "ExecutionDecision",
    "ExecutionResult",
    "DryRunExecutionAdapter",
]
