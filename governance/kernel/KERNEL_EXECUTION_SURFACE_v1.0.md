# SAPIANTA — KERNEL EXECUTION SURFACE v1.0

Status: LOCKED
Applies from: v1.2.1

---

## Canonical Execution Entry

Module:
sapianta_hoi.execution

Function:
execute(event_type: str, initial_state: str = "INITIAL")

---

## Execution Flow

execute()
  → SessionController.dispatch()
      → runtime_stub.execute_event()

---

## Guarantees

- Deterministic execution
- No I/O
- No network
- No advisory logic
- No boundary logic
- No integration logic

---

## Governance Constraint

No other public execution entry-point is permitted.

All execution must pass through:
sapianta_hoi.execution.execute
