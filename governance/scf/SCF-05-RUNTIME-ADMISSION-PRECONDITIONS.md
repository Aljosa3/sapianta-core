# SCF-05 — RUNTIME ADMISSION PRECONDITIONS

## Status
LOCKED — v0.4 CANONICAL  
Spremembe niso dovoljene brez formalne revizije SCF.

---

## ID
SCF-05-RAP

## Verzija
v1.0

## Faza
v0.4 — Execution Boundary & Runtime Governance (Phase Closure)

## Datum
2026-01-25

## Avtor
SAPIANTA — Canonical Governance Layer

---

## 1. NAMEN DOKUMENTA

Ta dokument definira **minimalne in obvezne predpogoje**, ki
**MORAJO obstajati**, preden je kakršnakoli oblika
izvajanja (runtime execution) sploh lahko dovoljena
v prihodnjih fazah (v0.5+).

Dokument:
- NE uvaja runtime okolja
- NE uvaja izvajanja modulov
- NE opisuje tehnične implementacije

Njegov namen je **normativno zapreti fazo v0.4**
in preprečiti prezgodnji ali implicitni prehod v izvajanje.

---

## 2. POLOŽAJ V SISTEMU

SCF-05 deluje kot:

> **zadnja normativna zapora pred runtime-om**

in je zavezujoč za:
- vse prihodnje faze
- vse runtime arhitekture
- vse oblike izvajanja ali interakcije

Brez izpolnitve vseh pogojev v tem dokumentu:
> **runtime execution ni dovoljen.**

---

## 3. RAZMERJE DO OBSTOJEČIH SCF DOKUMENTOV

Ta dokument je neposredno vezan na:

- **SCF-03 — MODULE SYNERGY CONSTRAINT**
- **SCF-04 — GUARD LIFECYCLE: EXECUTION BOUNDARY & DECISION AUTHORITY**

SCF-05:
- ne širi pooblastil Guard Lifecycle
- ne reinterpretira sinergije
- ne uvaja novih pravic modulom

Deluje izključno kot **precondition set**.

---

## 4. OBVEZNI RUNTIME PREDPOGOJI

### SCF-05-RAP-01 — Identiteta zahteve

Vsaka prihodnja zahteva za izvajanje MORA imeti:
- enoličen identifikator
- jasno določen izvor
- nedvoumno deklariran namen

Anonimne ali implicitne zahteve so prepovedane.

---

### SCF-05-RAP-02 — Kontekst zahteve

Vsaka zahteva MORA biti umeščena v:
- formalno definiran kontekst
- sledljiv izvorni okvir
- časovno določljiv trenutek

Zahteva brez konteksta je **neveljavna**.

---

### SCF-05-RAP-03 — Guard odločitev

Vsaka zahteva za runtime execution MORA imeti:
- eksplicitno odločitev Guard Lifecycle
- odločitev tipa **ALLOW**
- sledljivo utemeljitev

Brez Guard odločitve:
> **izvajanje ni dovoljeno.**

---

### SCF-05-RAP-04 — Skladnost s SCF-03 (sinergija)

Če zahteva vključuje več kot en modul:
- MORA biti presojena skladnost s **SCF-03**
- MORA biti dokazljivo, da:
  - ni deljenja stanja
  - ni koordinacije
  - ni kolektivnega odločanja

Vsaka kršitev → **DENY**.

---

### SCF-05-RAP-05 — Audit sled

Pred kakršnimkoli izvajanjem MORA obstajati:
- zapis zahteve
- zapis Guard odločitve
- povezava med obema

Izvajanje brez audit sledi je **nedovoljeno**.

---

### SCF-05-RAP-06 — Prepoved implicitnega izvajanja

Izvajanje:
- ne sme biti sproženo samodejno
- ne sme biti posledica stranskih učinkov
- ne sme biti rezultat “privzetega vedenja”

Vsak runtime prehod MORA biti:
> **ekspliciten in preverljiv.**

---

## 5. IZRECNO PREPOVEDANO (v0.4)

V fazi v0.4 je izrecno prepovedano:

- implementirati runtime sloj
- izvajati module
- orkestrirati sinergijo
- testirati execution poti
- uvajati optimizacije

Vsak tak poskus predstavlja:
> **kršitev fazne discipline.**

---

## 6. FAZNI PREHOD

Izpolnitev pogojev tega dokumenta:
- NE pomeni, da je runtime dovoljen
- pomeni zgolj, da je **normativna osnova popolna**

Prehod v v0.5 zahteva:
- ločeno fazno avtorizacijo
- nov Transition Report
- eksplicitno odločitev o implementaciji

---

## 7. ZAKLEP FAZE v0.4

S tem dokumentom je faza **v0.4 normativno zaključena**.

- Execution Boundary je definirana
- Guard Lifecycle je vzpostavljen kot avtoriteta
- Runtime prehodi so blokirani
- Pogoji za prihodnost so jasni in sledljivi

---

## KONEC DOKUMENTA
