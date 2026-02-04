# PHASE v0.20 — NEGATIVE PROOF WALKTHROUGH

Status: CANONICAL PROOF  
Version: v0.20  
Date: 2026-02-04  
Scope: Validator — Module Graph Pass  
Authority: Validator (exclusive)

---

## NAMEN

Ta dokument dokazuje, da je validator v v0.20:
- nujen
- zadosten
- neobhodljiv

Dokaz poteka izključno prek NEGATIVNIH scenarijev.
Vsak scenarij mora povzročiti HARD FAIL v točno določeni fazi.
Nobena kasnejša faza ne sme “reševati” napake.

---

## REFERENCA

Proof Module:
- Module ID: proof_multifile_v020
- Datoteke:
  - core.py
  - utils.py
  - logic.py

Validator faze (LOCKED):
1. Module Boundary Resolution
2. File Index Construction
3. Import Extraction (syntax-level only)
4. Module Boundary Enforcement
5. Dependency Graph Construction
6. Cycle Detection (DAG check)

---

## ❌ FAIL SCENARIO 1 — CIRCULAR DEPENDENCY

### Opis
- logic.py vsebuje import core.py
- Nastane cikel: core → utils → logic → core

### Sprehod po fazah

**FAZA 1 — Module Boundary Resolution**  
PASS  
Vse FILE poti pripadajo istemu modulu.

**FAZA 2 — File Index Construction**  
PASS  
Vse datoteke obstajajo in so unikatne.

**FAZA 3 — Import Extraction**  
PASS  
Vsi importi so statično razpoznani.

**FAZA 4 — Module Boundary Enforcement**  
PASS  
Vsi importi ciljajo znotraj modula.

**FAZA 5 — Dependency Graph Construction**  
PASS  
Graf je uspešno zgrajen.

**FAZA 6 — Cycle Detection (DAG check)**  
HARD FAIL  
Validator zazna cikel v grafu.

### Zaklep
- Build se ustavi.
- RawModuleWriter se ne kliče.
- Nobena datoteka se ne zapiše.
- Nobena faza pred FAZO 6 ne sme failati tega scenarija.

---

## ❌ FAIL SCENARIO 2 — OUT-OF-MODULE IMPORT

### Opis
- core.py vsebuje import iz zunanjega namespace-a
  (npr. external_lib ali other_module)

### Sprehod po fazah

**FAZA 1 — Module Boundary Resolution**  
PASS  
FILE poti so znotraj enega modula.

**FAZA 2 — File Index Construction**  
PASS  
Indeks datotek je veljaven.

**FAZA 3 — Import Extraction**  
PASS  
Import je statično zaznan.

**FAZA 4 — Module Boundary Enforcement**  
HARD FAIL  
Cilj importa ni znotraj modula.

### Zaklep
- Build se ustavi v FAZI 4.
- Graf se ne gradi.
- Cycle detection se ne izvaja.
- Runtime in writer nimata nobene vloge.

---

## ❌ FAIL SCENARIO 3 — PHANTOM FILE IMPORT

### Opis
- core.py importira missing.py
- missing.py ni FILE blok v buildu

### Sprehod po fazah

**FAZA 1 — Module Boundary Resolution**  
PASS

**FAZA 2 — File Index Construction**  
PASS  
Indeks vsebuje samo dejanske FILE bloke.

**FAZA 3 — Import Extraction**  
PASS  
Import je zaznan.

**FAZA 4 — Module Boundary Enforcement**  
HARD FAIL  
Ciljna datoteka ne obstaja v indeksu modula.

### Zaklep
- Build se ustavi.
- Ne pride do grafa.
- Ne pride do zapisovanja.

---

## NEGATIVNI DOKAZ — KLJUČNE POSLEDICE

1. Noben FAIL scenarij ne more biti “rešen” v runtime-u.
2. Noben FAIL scenarij ne more biti “ignoriran”.
3. Vsak FAIL ima eno in samo eno legitimno točko zaustavitve.
4. Validator je edina komponenta z dovolj konteksta za presojo.

---

## SEMANTIČNI ZAKLEP

Če bi katerikoli od teh scenarijev:
- PASS-al
- ali fail-al v napačni fazi

potem v0.20 ni veljavna faza.

Ta dokument dokazuje, da:
> Module Graph Pass ni opcija, temveč nujnost.

— END OF NEGATIVE PROOF —
