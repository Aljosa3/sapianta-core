# SAPIANTA SYSTEM FRAMEWORK

## Status
**LOCKED — READ ONLY**

---

## 1. NAMEN DOKUMENTA

Ta dokument formalno in dokončno določa:
- normativni del sistema SAPIANTA
- tehnični izvedbeni del sistema SAPIANTA
- razmerje med njima

Dokument je **referenčen, zavezujoč in nespremenljiv**.

---

## 2. SAPIANTA CANONICAL FRAMEWORK (SCF)

### Definicija

**SAPIANTA Canonical Framework (SCF)** je zaklenjen normativni okvir, ki določa
dovoljeno obnašanje sistema SAPIANTA in omejuje vse implementacije.

SCF:
- ne izvaja logike
- ne vsebuje runtime kode
- ne interpretira
- ne uči
- ne sklepa

SCF obstaja izključno kot **omejevalni in referenčni okvir**.

### Sestava SCF

SCF vključuje:
- SAPIANTA Canon
- vse System Protocols (SP-0 … SP-9)
- vse Core zaklepe in invariants

Vsi elementi SCF so:
- zaklenjeni
- nespremenljivi
- medsebojno konsistentni

### Status SCF

SCF je **dokončno zaklenjen**.

SCF se:
- ne razširja
- ne spreminja
- ne razlaga
- ne interpretira

---

## 3. SAPIANTA RUNTIME SYSTEM (SRS)

### Definicija

**SAPIANTA Runtime System (SRS)** je tehnični izvedbeni sistem, ki implementira
funkcionalnost sistema SAPIANTA.

SRS:
- vsebuje runtime
- vsebuje decision / response logiko
- vsebuje chat adapterje in module
- se aktivno izvaja

SRS je **popolnoma omejen s SCF**.

### Status SRS

SRS:
- se lahko razvija
- se lahko razširja
- se lahko testira
- se lahko refaktorira

pod pogojem, da je **vsaka sprememba SCF-compliant**.

---

## 4. RAZMERJE MED SCF IN SRS

Razmerje je **enosmerno in hierarhično**.

- SCF omejuje SRS
- SRS ne more vplivati na SCF
- SCF ima absolutno prednost pred SRS

Če pride do konflikta:
- implementacija v SRS se zavrne
- SCF se ne prilagaja

Srednje poti ni.

---

## 5. ODNOS DO CHAT IN MODULOV

- Chat je del SRS
- Chat je adapter, ne odločevalec
- Chat ne interpretira SCF

Vsi moduli:
- so del SRS
- morajo biti SCF-compliant

SCF se nikoli:
- ne kliče
- ne uvaža
- ne izvaja

---

## 6. KONČNA IZJAVA

S tem dokumentom sta:
- **SCF** formalno razglašen kot zaklenjen normativni okvir
- **SRS** formalno razglašen kot tehnični izvedbeni sistem

To razmerje je **končno, zavezujoče in nespremenljivo**.

Vsa nadaljnja aktivnost v projektu SAPIANTA
se izvaja izključno znotraj tega okvira.

---

**END OF DOCUMENT**
