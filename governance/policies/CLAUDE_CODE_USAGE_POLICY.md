# CLAUDE CODE USAGE POLICY — v0.1

## Status
ACTIVE  
Governance-enforced  
Applies to all code-generation agents (incl. Claude Code)

---

## Purpose

Ta dokument določa **stroga pravila uporabe Claude Code**
(z in brez integracije v IDE) znotraj sistema **SAPIANTA**.

Namen policy-ja je:
- preprečiti **arhitekturni zdrs**,
- ohraniti **fazno disciplino**,
- zagotoviti, da noben code agent ne pridobi
  implicitne avtoritete ali odločilne vloge.

Claude Code je **izvajalec**, ne arhitekt.

---

## Allowed Usage (WHAT CLAUDE MAY DO)

Claude Code SME izključno:

### 1. Generirati kodo po LOCK dokumentih
- izključno na podlagi:
  - LOCK-anih INIT/CONTRACT/SCHEMA dokumentov,
- brez interpretacije pomena ali namena.

Primer dovoljenega poziva:
> “Generiraj Python strukturo, ki točno sledi HDS_SCHEMA_v0.1.”

---

### 2. Generirati statične artefakte
- sheme,
- test vectors (neizvršilne),
- markdown dokumente po dani predlogi.

---

### 3. Izvajati preverjanje skladnosti (read-only)
- preveri, ali koda ali izhod krši pogodbo,
- poroča o kršitvah,
- **ne popravlja samodejno**.

---

## Forbidden Usage (WHAT CLAUDE MUST NEVER DO)

Claude Code STROGO NE SME:

### ❌ Predlagati izboljšav arhitekture
- noben “suggestion”,
- noben “optimization”,
- noben “refactor proposal”.

---

### ❌ Zapolnjevati konceptualnih vrzeli
- ne odgovarja na vprašanja tipa:
  - “kaj še manjka?”,
  - “kako bi to izboljšal?”,
  - “kaj bi bilo bolje?”.

---

### ❌ Prehajati faze
- ne implementira prihodnjih faz,
- ne uvaja nove logike brez LOCK dokumenta.

---

### ❌ Sprejemati odločitev ali priporočil
- noben ranking,
- noben “best choice”,
- nobena normativna izjava.

---

## Mandatory Prompt Rules

Vsak poziv Claude Code-u MORA:

1. Natančno navesti:
   - referenčni LOCK dokument,
   - verzijo (npr. v0.1).

2. Eksplicitno vsebovati prepoved:
   > “Do not suggest improvements or alternatives.”

3. Prepovedati interpretacijo:
   > “Do not infer intent beyond the provided document.”

Pozivi brez teh pravil so **neveljavni**.

---

## Authority Boundary

Claude Code:
- nima avtoritete,
- nima pravice do “zakaj”,
- nima pravice do odločitev.

Vsa arhitekturna odgovornost ostaja:
- **izključno pri človeku**,
- potrjena prek governance LOCK mehanizma.

---

## Enforcement

Vsak izhod Claude Code-a, ki:
- krši to politiko,
- uvaja novo semantiko,
- predlaga spremembe,

se šteje za **NESKLADEN** in se **zavrže brez izjeme**.

---

## Version Boundary

Ta policy velja:
- do naslednje verzije (v0.2),
- za vse obstoječe in prihodnje code agente.

Spremembe policy-ja so dovoljene **izključno prek novega LOCK dokumenta**.

---

END OF DOCUMENT
