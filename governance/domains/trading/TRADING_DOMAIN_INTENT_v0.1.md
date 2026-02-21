# TRADING DOMAIN INTENT v0.1

## Purpose
Define a deterministic, governance-first trading decision pipeline:

SIGNAL → DECISION → INTENT → (later) EXECUTION

The domain provides a minimal event vocabulary + validation discipline for trading decisions.
It does not change or expand the core public surface.

## Non-goals (v0.1)
- No live trading
- No broker coupling (IBKR not integrated yet)
- No portfolio management
- No order management system
- No ML training / model lifecycle
- No runtime market data ingestion mandate

## Domain boundary
- The core remains the constitutional substrate (sealed).
- TRADING is expressed as governance artifacts + validation + tests.
- No reverse imports across sealed layer boundaries.
- Determinism and repeatability remain invariant.

## Versioning
- This intent is versioned as v0.1.
- Forward-compatible: future versions may add events and fields without breaking existing names.
- Event names declared here are stable identifiers.