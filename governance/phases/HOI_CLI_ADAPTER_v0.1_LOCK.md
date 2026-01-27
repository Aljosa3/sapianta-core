# HOI_CLI_ADAPTER v0.1 — LOCK

Status: LOCKED  
Datum: 2026-01-26  
Veljavnost: kanonična  
Spremembe: prepovedane brez nove faze

---

## 1. Scope

Ta dokument zaklepa modul **HOI CLI Adapter** kot
zunanji, ročni legitimnostni nadzor nad dialogom.

Adapter je namenjen izključno:
- ročnemu upravljanju HOI stanja
- uveljavljanju legitimnostne prioritete
- takojšnji prekinitvi ali preusmeritvi dialoga

Adapter NI namenjen:
- zaznavanju signalov
- interpretaciji vsebine dialoga
- odločanju ali svetovanju
- poseganju v HDS ali LLM logiko

---

## 2. Hard Constraints (NON-NEGOTIABLE)

Naslednje omejitve so absolutne:

- NO signal detection
- NO signal inference
- NO adaptation
- NO memory
- NO autonomous logic
- NO dialog interpretation
- NO decision-making authority

Vsaka kršitev pomeni **neveljavno implementacijo**.

---

## 3. Relationship to Locked Modules

HOI CLI Adapter:
- je zunanji ovoj
- ne spreminja zaklenjenih modulov:
  - HDS Chat Shell v0.1
  - HOI Guard
- nima pravice do:
  - spremembe izhodov
  - filtriranja vsebine
  - ponovne formulacije HDS predlogov

---

## 4. Allowed Operations

Dovoljene so izključno naslednje operacije:

- nastavitev HOI stanja:
  - ORIENT
  - PAUSE
  - REDIRECT
- terminalni izpis stanja
- uveljavitev prekinitve dialoga

Vse operacije so:
- ročne
- eksplicitne
- deterministične

---

## 5. Pause Semantics

- HOI:PAUSE ima absolutno prednost
- dialog se takoj ustavi
- nadaljevanje NI možno brez eksplicitnega HOI:ORIENT
- adapter ne sme samodejno nadaljevati dialoga

---

## 6. Forbidden Behaviors

Prepovedano je:

- kakršnokoli posredno odločanje
- kakršnokoli vplivanje na HDS vsebino
- eskalacija v svetovalno ali priporočilno vlogo
- implicitno nadaljevanje dialoga po PAUSE
- avtomatsko preklapljanje HOI stanj

---

## 7. Version Lock

- Ta dokument zaklepa verzijo **v0.1**
- Razširitve zahtevajo:
  - novo INIT fazo
  - nov LOCK dokument
- Neposredne spremembe niso dovoljene

---

LOCK CONFIRMED.
