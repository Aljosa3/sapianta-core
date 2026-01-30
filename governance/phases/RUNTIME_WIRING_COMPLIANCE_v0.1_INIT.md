# RUNTIME WIRING & COMPLIANCE v0.1 — INIT

## Status
INIT  
LOCK-ready (v0.1)  
No execution • No autonomy • No decision authority

---

## Purpose

Runtime Wiring & Compliance v0.1 formalno definira in zaklene
**edino dovoljeno zaporedje prehoda** skozi sistem SAPIANTA.

Dokument:
- dokazuje, da je `wiring.py` **edini sistemski entry point**,
- zagotavlja, da **nič ne more obiti** HOI → HDS Boundary → HDS Schema → HDS Guard,
- vzpostavlja **auditno sled** brez uvajanja runtime logike.

---

## Canonical Wiring Path

Edina dovoljena pot:

Human
↓
SAPIANTA_CHAT (thin: delegator + renderer)
↓
wiring.py
↓
HOI Orchestrator v0.2
↓
HDS Boundary v0.1
↓
HDS Schema / Contract v0.1
↓
HDS Execution Guard v0.1
↓
[ Guarded, Non-Executable Output ]


Vsak izhod zunaj te poti je **neveljaven**.

---

## Wiring Constraints (MANDATORY)

`wiring.py` MORA zagotavljati:

1. **Single Entry Invariant**
   - noben drug modul ne sme neposredno prejemati vhodov iz Chat,
   - vsi tokovi gredo izključno skozi `wiring.py`.

2. **Fixed Order Invariant**
   - vrstni red modulov je nespremenljiv:
     HOI → Boundary → Schema → Guard.

3. **No Bypass Invariant**
   - noben modul ne sme:
     - preskočiti Boundary,
     - preskočiti Schema,
     - preskočiti Guard.

4. **No Side-Effects Invariant**
   - `wiring.py` ne izvaja dejanj,
   - ne shranjuje stanja,
   - ne sproža procesov.

---

## Compliance Rules

Sistem je skladen (COMPLIANT), če:

- vsi izhodi z `hds_ready: true` preidejo:
  - Boundary normalizacijo,
  - Schema tipizacijo,
  - Guard validacijo.

Sistem je **NESKLADEN**, če zaznamo:
- neposreden klic HOI ali HDS izven `wiring.py`,
- preskok kateregakoli sloja,
- runtime logiko v `wiring.py`.

---

## Compliance Outcomes (Abstract)

```json
{
  "compliance_status": "COMPLIANT | NON_COMPLIANT",
  "scope": "RUNTIME_WIRING_COMPLIANCE_v0.1",
  "notes": "informational only"
}
