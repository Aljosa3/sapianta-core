# SRS: MODULE BUILDER — IGL v2 COMPLIANCE CHECKLIST

Layer: SRS  
Component: Module Builder  
Bindings: IGL v2 (GR-001 – GR-009)  
Status: ACTIVE  
Normativity: NONE (structural enforcement only)

---

## GR-001 — NO IMPLICIT ASSUMPTIONS

✔ Module Builder zahteva popolnoma eksplicitni `ModuleSpec`  
✔ Nobeno polje ni opcijsko  
✔ Ni privzetih vrednosti  
✔ Ne obstaja inference ali dopolnjevanje vhodov  

Status: COMPLIANT

---

## GR-002 — NO SEMANTIC INTERPRETATION

✔ Module Builder ne interpretira pomena polj  
✔ Vrednosti se obravnavajo kot neinterpretirani nizi / strukture  
✔ Ne obstaja semantična validacija imen, verzij ali vsebine  

Status: COMPLIANT

---

## GR-003 — NO AUTHORITY ESCALATION

✔ Module Builder ne sprejema odločitev  
✔ Ne sproža dejanj zunaj lastnega obsega  
✔ Ne kliče SCF, Chat ali runtime komponent  

Status: COMPLIANT

---

## GR-004 — DETERMINISTIC BEHAVIOR

✔ Enak `ModuleSpec` → enak rezultat  
✔ Brez časovnih, okoljskih ali globalnih vplivov  
✔ Brez naključnosti  

Status: COMPLIANT

---

## GR-005 — EXPLICIT FAILURE

✔ Vse napake so terminalne  
✔ Brez fallback poti  
✔ Brez tihe korekcije  
✔ Napake so tipizirane (`SchemaError`, `IGLValidationError`, `EmissionError`)  

Status: COMPLIANT

---

## GR-006 — NO HIDDEN CONTROL FLOW

✔ Ni dekoratorjev  
✔ Ni implicitnih hookov  
✔ Ni magic metod za nadzor toka  

Status: COMPLIANT

---

## GR-007 — NO GLOBAL STATE

✔ Module Builder ne hrani stanja  
✔ Ni singletonov  
✔ Ni cache-a  

Status: COMPLIANT

---

## GR-008 — LAYER ISOLATION

✔ Importi omejeni na `srs.module_builder.*`  
✔ Ni cross-layer dostopa  
✔ Ni odvisnosti od SCF ali Chat  

Status: COMPLIANT

---

## GR-009 — EXTERNAL CALLER NEUTRALITY

✔ Module Builder ne razlikuje klicateljev  
✔ Claude Code, CLI ali CI imajo enak status  
✔ Ni privilegiranih poti  

Status: COMPLIANT

---

## OVERALL VERDICT

Module Builder je **IGL v2 COMPLIANT** na strukturni ravni.

Ta dokument je:
- obvezen del SRS
- referenca za implementacijo
- blokada proti semantičnim zdrsom
