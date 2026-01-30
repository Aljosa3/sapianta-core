# HDS SCHEMA / CONTRACT v0.1 — INIT

## Status
INIT  
LOCK-ready (v0.1)  
No execution • No autonomy • No decision authority

---

## Purpose

HDS Schema / Contract v0.1 definira **edino dovoljeno podatkovno obliko**
za informacije, označene kot *HDS-ready*.

Namen dokumenta je:
- formalno tipizirati izhod HOI/HDS Boundary,
- omejiti vsebino, ki jo HDS *lahko vidi*,
- izrecno prepovedati vse izvršilne ali normativne semantike.

Ta dokument je **pogodba**, ne implementacija.

---

## Position in System Architecture

Human
↓
SAPIANTA_CHAT (thin interface)
↓
HOI Orchestrator v0.2 (reference-only)
↓
HDS Boundary v0.1 (passive normalization)
↓
HDS Schema / Contract v0.1
↓
[ Typed, Passive, Non-Executable Data ]


HDS Schema:
- ne izvaja logike,
- ne spreminja toka,
- ne uvaja avtoritete.

---

## Scope of the Contract

Pogodba velja za:
- vse izhode z oznako `hds_ready: true`,
- vse prihodnje HDS implementacije,
- vse audite skladnosti HDS.

Pogodba **ne velja** za:
- runtime orkestracijo,
- odločanje,
- optimizacijo,
- izvrševanje.

---

## Allowed Data Categories

HDS Schema v0.1 DOVOLJUJE izključno:

### 1. Context
- opis stanja ali problema,
- brez interpretacije ali sklepanja.

### 2. Options
- seznam možnih poti ali vidikov,
- brez rangiranja,
- brez priporočil.

### 3. Constraints
- eksplicitne omejitve,
- zakonske, tehnične ali sistemske,
- brez prioritet.

### 4. Notes
- pojasnila ali dodatne informacije,
- informativne narave.

---

## Explicitly Forbidden Content

HDS Schema v0.1 STROGO PREPOVEDUJE:

- priporočila (“najboljša izbira”, “priporočamo”),
- ocene (“boljše/slabše”),
- uteži, točke ali score,
- verjetnosti uspeha,
- navodila za akcijo,
- implicitne odločitve.

---

## Schema Invariants

- Schema defines structure, not meaning
- Schema does not imply authority
- Schema has no execution semantics
- Schema is stable within v0.1
- wiring.py remains the sole system entry path

---

## Reference Schema (Abstract)

Primer abstraktne, neizvršilne sheme:

```json
{
  "mode": "HDS_SCHEMA_REFERENCE",
  "scope": "HDS_SCHEMA_v0.1",
  "hds_ready": true,
  "data": {
    "context": "...",
    "options": ["...", "..."],
    "constraints": ["...", "..."],
    "notes": "..."
  }
}
