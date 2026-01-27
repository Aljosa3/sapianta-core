# AUDIT_HARNESS v0.1 — LOCK

Status: LOCKED  
Datum: 2026-01-26  
Veljavnost: kanonična  
Spremembe: prepovedane brez nove faze

---

## 1. Scope

Ta dokument zaklepa modul **Audit Harness** kot
pasivni, dokazni sloj za zajem dialoga.

Audit Harness je namenjen izključno:
- zajemu standardnega izhoda (stdout)
- ustvarjanju dokaznih zapisov
- forenzični sledljivosti dialoga

Audit Harness NI namenjen:
- interpretaciji vsebine
- zaznavanju kršitev
- nadzoru dialoga
- poseganju v HOI, HDS ali LLM

---

## 2. Hard Constraints (NON-NEGOTIABLE)

Naslednje omejitve so absolutne:

- NO signal detection
- NO signal inference
- NO interpretation
- NO adaptation
- NO memory in runtime
- NO state mutation
- NO control authority
- NO decision-making logic

Vsaka kršitev pomeni **neveljavno implementacijo**.

---

## 3. Relationship to Locked Modules

Audit Harness:
- je zunanji ovoj
- ne spreminja zaklenjenih modulov:
  - HDS Chat Shell v0.1
  - HOI CLI Adapter v0.1
- nima pravice do:
  - filtriranja vsebine
  - preoblikovanja izhodov
  - vplivanja na potek dialoga

---

## 4. Allowed Operations

Dovoljene so izključno naslednje operacije:

- zajem stdout
- zapis v trajni log
- terminalni izpis identičen izvirnemu

Vse operacije so:
- pasivne
- deterministične
- write-only

---

## 5. Evidence Semantics

- zapis je dokazni artefakt
- vsebina se ne interpretira
- vrstni red izpisa se ohrani
- ni retroaktivnih sprememb

Audit Harness ne sklepa, ne ocenjuje in ne razsoja.

---

## 6. Forbidden Behaviors

Prepovedano je:

- aktivno spremljanje pravilnosti
- zaznavanje kršitev LOCK-ov
- avtomatsko označevanje tveganj
- vnos metapodatkov, ki vplivajo na pomen dialoga
- kakršnokoli posredno odločanje

---

## 7. Version Lock

- Ta dokument zaklepa verzijo **v0.1**
- Razširitve zahtevajo:
  - novo INIT fazo
  - nov LOCK dokument
- Neposredne spremembe niso dovoljene

---

LOCK CONFIRMED.
