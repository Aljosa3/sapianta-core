# MODULE_ADMISSION — LOCK v0.3

## Status
**LOCKED**

Ta dokument formalno zaklene pravila za **admission (sprejem) modulov**
v runtime sistem SAPIANTA, verzija **v0.3**.

Brez izpolnitve teh pravil modul **NE SME** biti:
- naložen
- registriran
- izvršen
- referenciran iz Orchestratorja ali GuardLifecycle

---

## Scope

Ta lock velja za:

- vse execution module
- vse analysis / explain / audit module
- Module Builder
- Interaction Registry
- vse prihodnje runtime razširitve

---

## Locked Invariants (v0.3)

### M1 — Mandatory Module Manifest

Vsak modul **MORA** vsebovati datoteko: .module_builder_manifest 
v **korenu mape modula**.

Modul brez manifesta:
- **NE OBSTAJA**
- se **ne sme naložiti**
- se **ne sme registrirati**
- se **ne sme izvršiti**

---

### M2 — Manifest as Normative Contract

`.module_builder_manifest` je:

- normativni dokument
- ne konfiguracija
- ne priporočilo

Kar **ni eksplicitno dovoljeno**, je **prepovedano**.

---

### M3 — Explicit Permission Model

Manifest **MORA** eksplicitno določiti:

- ali modul:
  - bere `ExecutionContext`
  - piše `ctx.result`
  - piše `ctx.explain`
  - mutira `status`
  - mutira `phase`
  - kliče `finalize()`

Če dovoljenje **ni navedeno**, se šteje kot **FALSE**.

---

### M4 — Forbidden Capabilities

Ne glede na manifest, modul **NIKOLI NE SME**:

- klicati `Orchestrator`
- nastavljati ali spreminjati `_origin`
- mutirati `phase`
- neposredno klicati `finalize()`
- obiti GuardLifecycle

Vsaka taka kršitev je **ProtocolViolation**.

---

### M5 — Admission Before Execution

- Modul **MORA** biti preverjen (admitted)
- **PREDEN** se pojavi v:
  - execution flow
  - registry
  - orchestrator logiki

Execution neadmitted modula je **neveljaven**.

---

### M6 — Versioned Admission

- Admission pravilnik je verzioniran
- Spremembe zahtevajo:
  - novo verzijo (v0.4+)
  - ekspliciten UNLOCK ali SUPERSEDE dokument

---

## Implementation Reference

Ta lock je implementiran ali predviden v:

- `modules/*/.module_builder_manifest`
- `runtime/interaction_registry.py`
- Module Builder (naslednja faza)

---

## Test Expectations

Sistem **MORA** zavrniti:

- modul brez manifesta
- modul z neveljavnim manifestom
- modul, ki krši prepovedane zmožnosti

---

## Lock Semantics

- Ta lock:
  - **NE omejuje** števila modulov
  - **OMEJUJE** njihovo moč
- Preprečuje:
  - implicitne privilegije
  - runtime eskalacije
  - “skrite” module

---

## Version

- Admission Lock: **v0.3**
- Lock date: **2026-01-23**
- Supersedes: GuardLifecycle LOCK v0.2
- Status: **ACTIVE**

---

**This lock is FINAL.**

