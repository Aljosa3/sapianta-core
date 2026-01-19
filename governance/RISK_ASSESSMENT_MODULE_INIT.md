# RISK_ASSESSMENT_MODULE_INIT

Status: INIT  
Odvisnost:
- MODULE_CONTRACT_INIT = LOCKED
- MODULE_SKELETON_REVIEW = LOCKED
- CANON_GUARD_DECISION_CHAIN = ACTIVE

Razred: Module / Assessment  
Narava: Evalvacijska (ne-odločitvena)

---

## 1. NAMEN

Vzpostaviti **Risk Assessment Modul** kot prvi funkcionalni modul,
ki zaznava potencialna tveganja in skladnostne signale
brez kakršnekoli odločilne ali izvršilne moči.

---

## 2. DOVOLJENO OBNAŠANJE

Modul sme:
- brati INTENT
- brati CONTEXT
- vračati ne-zavezujoče ocene tveganja

---

## 3. PREPOVEDANO OBNAŠANJE

Modul:
- ne odloča
- ne dovoljuje
- ne zavrača
- ne preverja jurisdikcije
- ne izvaja zakonodaje
- ne piše v audit

---

## 4. VLOGA V SISTEMU

Risk Assessment Modul:
- podpira Decision Gate
- ne nadomešča Decision Authority
- ne legitimira odločitev

Njegov izhod je **signal**, ne odločitev.

---

## 5. INVARIANTA

> Če izhod tega modula neposredno povzroči odločitev,
> modul krši Module Contract.

---

## 6. ZAKLEP FAZE

Faza `RISK_ASSESSMENT_MODULE_INIT` se lahko označi kot **LOCKED**, ko velja:

- modul se naloži in izvede
- izhod je ne-zavezujoč
- ni stranskih učinkov
- ni kršitev Canona

---

Konec dokumenta.
