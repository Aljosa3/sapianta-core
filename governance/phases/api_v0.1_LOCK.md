# API v0.1 — HDS Preview Endpoint — LOCK

STATUS: LOCKED
DATE: 2026-01-27

## Endpoint
POST /hds/preview

## Guarantees
- Stateless execution
- Deterministic output
- Returns HDS JSON-safe Output v0.4
- Request payload is accepted but not interpreted

## Invariants
- HOI retains legitimacy
- HDS never decides
- Audit is passive (stdout + snapshot)
- Backward compatibility preserved

## Prohibitions
- No state
- No memory
- No ranking or scoring
- No implicit authority

LOCK CONFIRMED.
