# PHASE v0.20 — MULTI-FILE MODULE SUPPORT (LOCK)

Status: LOCKED  
Version: v0.20  
Date: 2026-02-04  
Scope: Module build pipeline  
Authority: Validator (exclusive)

---

## 1. FAZA v0.20 — NAMEN

Faza v0.20 formalno zaklepa podporo za **večdatotečne module** z notranjo strukturo,
ob ohranitvi popolne governance discipline.

Sistem mora dokazati, da lahko:
- v enem determinističnem buildu sprejme več FILE blokov
- materializira več datotek znotraj enega modula
- omogoča notranje importe znotraj modula
- zavrne vse strukturno nedovoljene konfiguracije

Ta faza ne uvaja novih runtime zmožnosti.

---

## 2. KANONIČNA DEFINICIJA MODULA (LOCK)

V kontekstu v0.20 je **modul** definiran izključno kot:

> množica FILE blokov, ki delijo skupni modul root,
> in so validirani kot strukturno dopustna celota.

Modul:
- ni runtime entiteta
- ni Python paket v interpretativnem smislu
- ne obstaja izven validatorja in zapisanih datotek

---

## 3. DOVOLJENO V v0.20

Sistem MORA omogočiti:

- več FILE blokov v enem buildu
- več datotek znotraj istega modula
- statične, eksplicitne notranje importe med datotekami
- poljuben vrstni red FILE blokov v LLM outputu

---

## 4. PREPOVEDANO V v0.20 (HARD LOCK)

Sistem NE SME:

- popravljati ali reinterpretirati LLM outputa
- inferirati __init__.py ali implicitnih paketov
- dovoliti importov izven modula
- dovoliti krožnih odvisnosti
- dovoliti importov neobstoječih datotek
- izvajati runtime heuristik
- uvajati fallback ali “best effort” vedenja
- zapisovati delnih rezultatov

Vsaka kršitev povzroči HARD FAIL.

---

## 5. VALIDATOR — EDINA AVTORITETA (LOCK)

Validator je edina komponenta, ki:

- razume notranjo strukturo modula
- gradi graf odvisnosti
- presoja dopustnost builda

Runtime:
- ne interpretira importov
- ne preverja strukture
- ne pozna modula kot koncepta

RawModuleWriter:
- izvaja izključno deterministični zapis datotek
- ne izvaja validacije
- ne razvršča ali optimizira FILE blokov

---

## 6. MODULE GRAPH PASS — ZAKLENJENA SEMANTIKA

Validator v v0.20 izvaja točno naslednje faze:

1. Module Boundary Resolution  
2. File Index Construction  
3. Import Extraction (syntax-level only)  
4. Module Boundary Enforcement  
5. Dependency Graph Construction  
6. Cycle Detection (DAG check)

Nobena dodatna faza ni dovoljena brez odklepa faze.

---

## 7. DOKAZNI ARTEFAKT (PROOF REQUIREMENT)

Faza v0.20 se šteje kot uspešno zaključena, če:

- validni večdatotečni modul PASS-a
- vsak od naslednjih scenarijev HARD FAIL-a:
  - krožna odvisnost
  - import izven modula
  - import neobstoječe datoteke

Brez izjem.

---

## 8. SEMANTIČNI POVZETEK (LOCK STATEMENT)

v0.20 dokazuje, da SAPIANTA:

> zna zgraditi notranje strukturiran modul
> brez ene same interpretativne ali heuristične poteze.

Struktura je deklarirana.  
Presoja je deterministična.  
Validator je edina resnica.

---

## 9. ZAKLEP FAZE

S to datoteko je faza v0.20:
- konceptualno zaključena
- semantično zaklenjena
- pripravljena za implementacijo brez odločanja

Vsaka sprememba zahteva novo fazo.

— END OF LOCK —
