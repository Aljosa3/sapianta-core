# IGL-GR-007 — No Time-Based Behavior

Status: DRAFT  
Scope: SRS (Implementation Guard Layer)

## Rule
SRS implementation code MUST NOT contain implicit or explicit
time-based behavior unless time is provided explicitly via an interface.

## Definition
Time-based behavior includes any logic that depends on:
- current system time
- elapsed time
- sleep or delay
- scheduling
- timers or background timing mechanisms

## Rationale
Time introduces non-determinism, implicit state, and hidden execution order.
In a governed system, all temporal behavior MUST be explicit, injectable,
and externally controlled.

## Enforcement
The following are DISALLOWED in SRS code:
- direct calls to system time APIs
- `sleep`, `delay`, or wait-based logic
- timers, schedulers, cron-like behavior
- polling loops dependent on time

The following are ALLOWED:
- receiving time as an explicit parameter
- using time values provided by an interface
- deterministic computation over provided timestamps

## Examples (Non-exhaustive)

### ALLOWED
- `process(event_time)`
- `decide(context.timestamp)`

### DISALLOWED
- `time.time()`
- `datetime.now()`
- `sleep(1)`
- retry loops with backoff based on time
