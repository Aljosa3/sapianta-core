# MODULE_SKELETON_INIT

Status: INIT  
Odvisnost:
- MODULE_CONTRACT_INIT = LOCKED
- CANON_GUARD_DECISION_CHAIN = ACTIVE

Razred: Module / Reference  
Narava: Referenčna (brez funkcionalnosti)

---

## 1. NAMEN

Vzpostaviti **referenčni modul**, ki:
- spoštuje Module Contract
- se pravilno vključi v runtime
- ne posega v decision, jurisdiction ali execution

Ta modul ni namenjen uporabi.
Je **arhitekturni test**.

---

## 2. DOVOLJENO OBNAŠANJE

Skeleton modul:
- prejme intent (read-only)
- prejme context (read-only)
- vrne evalvacijski signal

Ne izvaja nobene logike.

---

## 3. PREPOVEDANO OBNAŠANJE

Skeleton modul:
- ne odloča
- ne sproža Decision Gate
- ne preverja jurisdikcije
- ne piše v audit
- ne komunicira z uporabnikom

---

## 4. VLOGA V SISTEMU

Skeleton modul služi kot:
- referenca za vse prihodnje module
- testni primer za runtime tok
- dokaz skladnosti Module Contracta

---

## 5. ZAKLEP FAZE

Faza `MODULE_SKELETON_INIT` se lahko označi kot **LOCKED**, ko velja:

- modul se uspešno naloži
- modul se izvede brez stranskih učinkov
- modul ne krši nobene invariance

---

Konec dokumenta.
