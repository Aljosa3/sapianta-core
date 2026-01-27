# API v0.1 — HDS Preview Endpoint — INIT

STATUS: INIT
SCOPE: Additive API layer only

## Objective
Expose a minimal HTTP endpoint that returns HDS JSON-safe Output v0.4.

## Endpoint
- POST /hds/preview

## Behavior
- Accepts request payload but does not interpret it
- Emits deterministic HDS JSON v0.4
- No state, no memory, no ranking, no adaptation

## Invariants
- HOI retains legitimacy
- HDS never decides
- Audit is passive (stdout)
- Backward compatibility preserved

INIT COMPLETE.
