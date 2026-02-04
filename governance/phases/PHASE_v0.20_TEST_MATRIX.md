# PHASE v0.20 — TEST CASE MATRIX

Status: CANONICAL TEST AUTHORITY  
Version: v0.20  
Date: 2026-02-04  
Scope: Validator — Module Graph Pass  
Authority:
- PHASE_v0.20_MULTI_FILE_MODULE_LOCK.md
- PHASE_v0.20_NEGATIVE_PROOF_WALKTHROUGH.md
- PHASE_v0.20_IMPLEMENTATION_CHECKLIST.md

---

## NAMEN

Ta dokument definira popoln in zaprt nabor testnih primerov za fazo v0.20.
Vsak testni primer ima:
- jasno definiran vhod
- pričakovano točko PASS ali HARD FAIL
- natančno fazo validatorja, kjer se mora build ustaviti

Če kateri koli test ne ustreza pričakovanemu rezultatu,
je implementacija v0.20 neveljavna.

---

## REFERENČNI MODUL

Module ID: proof_multifile_v020  
Datoteke (osnovni nabor):
- core.py
- utils.py
- logic.py

---

## ✅ PASS TEST CASES

### TC-PASS-01 — VALID MULTI-FILE MODULE

Opis:
- Trije FILE bloki
- Vsi importi so znotraj modula
- Brez ciklov

Pričakovani rezultat:
- Validator PASS
- RawModuleWriter se kliče
- Vse datoteke so zapisane

Validator faze:
- FAZA 1 → PASS
- FAZA 2 → PASS
- FAZA 3 → PASS
- FAZA 4 → PASS
- FAZA 5 → PASS
- FAZA 6 → PASS

---

### TC-PASS-02 — FILE BLOCK ORDER IRRELEVANCE

Opis:
- Enak nabor FILE blokov kot TC-PASS-01
- FILE bloki so v drugačnem vrstnem redu v LLM outputu

Pričakovani rezultat:
- Validator PASS
- Rezultat identičen TC-PASS-01

Zaklep:
- Vrstni red FILE blokov ne vpliva na validacijo

---

## ❌ FAIL TEST CASES — STRUKTURNE KRŠITVE

### TC-FAIL-01 — CIRCULAR DEPENDENCY

Opis:
- logic.py importira core.py
- Nastane cikel

Pričakovani rezultat:
- HARD FAIL

Fail faza:
- FAZA 6 — Cycle Detection

Zaklep:
- Nobena prejšnja faza ne sme failati tega testa

---

### TC-FAIL-02 — OUT-OF-MODULE IMPORT

Opis:
- core.py vsebuje import iz zunanjega namespace-a

Pričakovani rezultat:
- HARD FAIL

Fail faza:
- FAZA 4 — Module Boundary Enforcement

Zaklep:
- Graf se ne gradi
- Writer se ne kliče

---

### TC-FAIL-03 — PHANTOM FILE IMPORT

Opis:
- core.py importira datoteko, ki ni FILE blok

Pričakovani rezultat:
- HARD FAIL

Fail faza:
- FAZA 4 — Module Boundary Enforcement

---

## ❌ FAIL TEST CASES — FILE PATH VIOLATIONS

### TC-FAIL-04 — DUPLICATE FILE PATH

Opis:
- Dva FILE bloka imata isto pot

Pričakovani rezultat:
- HARD FAIL

Fail faza:
- FAZA 2 — File Index Construction

---

### TC-FAIL-05 — FILE OUTSIDE MODULE ROOT

Opis:
- En FILE blok ima pot izven skupnega modula

Pričakovani rezultat:
- HARD FAIL

Fail faza:
- FAZA 1 — Module Boundary Resolution

---

## ❌ FAIL TEST CASES — IMPORT EXTRACTION ERRORS

### TC-FAIL-06 — NON-STATIC IMPORT

Opis:
- Import ni statično razpoznaven

Pričakovani rezultat:
- HARD FAIL

Fail faza:
- FAZA 3 — Import Extraction

---

### TC-FAIL-07 — UNRESOLVABLE IMPORT TARGET

Opis:
- Importa ni mogoče preslikati v ime datoteke

Pričakovani rezultat:
- HARD FAIL

Fail faza:
- FAZA 3 — Import Extraction

---

## 🚫 NEGATIVNI TESTI — IZRECNO PREPOVEDANO

Ti testi morajo FAIL-ati brez izjeme:

- dovoljen standard library import
- implicitni __init__ import
- runtime-only import
- fallback ali “best effort” validacija
- delni zapis datotek ob FAIL-u

Pričakovani rezultat:
- HARD FAIL
- brez zapisovanja
- brez warnings

---

## ZAKLJUČNI POGOJ

Faza v0.20 je pravilno implementirana, če in samo če:
- vsi PASS testi PASS-ajo
- vsi FAIL testi FAIL-ajo v točno določeni fazi
- ni dodatnih FAIL ali PASS primerov

Vsako odstopanje zahteva:
- zavrnitev implementacije
- ali odprtje nove faze

— END OF TEST MATRIX —
