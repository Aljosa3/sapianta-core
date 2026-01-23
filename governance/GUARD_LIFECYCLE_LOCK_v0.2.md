# GUARD_LIFECYCLE — LOCK v0.2

## Status
**LOCKED**

Ta dokument formalno zaklene implementacijo **GuardLifecycle v0.2** in določa
nepreklicna arhitekturna in normativna pravila za nadaljnji razvoj sistema.

---

## Scope

Ta lock velja za:

- GuardLifecycle kot **edini dovoljeni execution gate**
- Minimal Execution Path (MEP)
- Normativno ločitev med:
  - guard odločitvami
  - execution
  - explain / audit plastmi

---

## Locked Invariants (v0.2)

### I1 — Single Execution Gate

- Vsak execution (LLM ali drug runtime) **MORA** vstopiti prek:
  - `GuardLifecycleOrchestrator`
- Neposreden klic:
  - `Orchestrator.run(ctx)`
  je **prepovedan** in predstavlja **ProtocolViolation**.

---

### I2 — Origin Marker Authority

- `ExecutionContext._origin`:
  - obstaja
  - je privzeto `None`
  - **nastavi ga IZKLJUČNO GuardLifecycleOrchestrator**
- MEP, guards, SP-ji in execution moduli:
  - **NE SMEJO** nastavljati ali spreminjati `_origin`

Execution brez nastavljenega `_origin` je **neveljaven**.

---

### I3 — Phase Ownership

- Prehod: INIT → EXECUTION je **izključna pristojnost GuardLifecycle**.
- Runtime guards **NE SMEJO** mutirati `ctx.phase` in smejo le preverjati, da je faza `EXECUTION`.


---

### I4 — Status Authority

- `Status.ALLOW`: lahko nastavi **izključno runtime guard**
- Orchestrator **NE SME** nastaviti `ALLOW` 
- Lahko nastavi samo:
  - `HALT`
  - `FINAL`
  - `HARD_FAIL`

---

### I5 — Explain Layer Isolation

- `ctx.explain` vedno obstaja
- je **post-decision artefakt**
- **NIMA normativnega vpliva**
- Spremembe explain podatkov **NE SMEJO** vplivati na `status`, `phase` ali `result`

---

### I6 — SP Discipline

- SP-1 … SP-8:
- **NE SMEJO** klicati `finalize()`
- **NE SMEJO** spreminjati `phase`
- Normativni zaključek (`FINAL`, `DENY`, `HALT`, `HARD_FAIL`) je dovoljen samo v Orchestratorju ali v GuardLifecycle (v primeru kršitve protokola)

---

## Implementation Reference

Lock v0.2 je implementiran in preverjen v naslednjih komponentah:

- `runtime/guard_lifecycle/`
- `runtime/mep/context.py`
- `runtime/mep/guards.py`
- `runtime/mep/orchestrator.py`
- `runtime/mep/runner.py`

Testna validacija:

- `tests/test_guard_lifecycle.py`
- `tests/test_guard_invariant_*`

---

## Lock Semantics

- Ta lock:
- **NE preprečuje** nadaljnjega razvoja
- **PREPREČUJE** retroaktivne spremembe pomena v0.2
- Vsaka sprememba teh invariantov zahteva novo verzijo (v0.3+) ekspliciten **UNLOCK** ali **SUPERSEDE** dokument

---

## Version

- GuardLifecycle: **v0.2**
- Lock date: **2026-01-23**
- Commit reference: `e22606e`
- Git tag: `v0.2`

---

**This lock is FINAL.**
