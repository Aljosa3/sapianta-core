# GOVERNANCE SNAPSHOT v1

**Sistem:** SAPIANTA  
**Datum:** 2026-01-17  
**Status:** REFERENČNI DOKUMENT  
**Vloga:** enoten pregled governance arhitekture, veljavnih protokolov in zaklenjenih normativnih meja

---

## 1️⃣ NAMEN DOKUMENTA

Ta dokument predstavlja **enotno referenco** za:
- trenutno veljavno governance strukturo sistema SAPIANTA
- status posameznih SP protokolov
- jasno ločnico med zaklenjenim jedrom in prilagodljivo plastjo

Dokument:
- **ne uvaja novih pravil**
- **ne nadomešča posameznih SP dokumentov**
- služi orientaciji, onboardingu in zunanji razlagi sistema

---

## 2️⃣ HIERARHIJA VELJAVNOSTI

Veljavnost pravil v sistemu SAPIANTA je hierarhična:

Canon  
→ Core Laws  
→ Phase Locks (SP-LOCK)  
→ ACTIVE / INIT SP protokoli  
→ Implementacija

Nižji nivo **ne sme** razširjati ali reinterpretirati višjega.

---

## 3️⃣ ZAKLENJENO GOVERNANCE JEDRO (LOCKED)

Naslednji protokoli so **normativno zaklenjeni** in se ne smejo spreminjati brez nove faze:

### 🔒 SP-9 — AI Output Governance Protocol
- določa obvezno strukturo vseh AI izhodov
- preprečuje explain-driven drift
- zahteva celovitost vsebin

**Status:** LOCKED

---

### 🔒 SP-10 — Explainability Boundary Protocol
- ločuje explain / audit / trace
- preprečuje razkrivanje notranjih razlogov
- uvaja minimal evidence principle

**Status:** LOCKED

---

### 🔒 SP-11 — Audit & Retention Policy
- določa obseg in trajanje hrambe podatkov
- preprečuje prekomerno logiranje
- ločuje audit od execution trace

**Status:** LOCKED

---

### 🔒 SP-12 — Incident Response Protocol
- določa zaznavo, obravnavo in zapiranje incidentov
- uvaja containment pred razlago
- zagotavlja determinističen odziv

**Status:** LOCKED

---

## 4️⃣ OPERATIVNA GOVERNANCE PLAST (INIT)

Naslednji protokoli so **aktivni, a namenoma nezaklenjeni**,
da omogočajo testiranje in prilagoditve:

### 🟡 SP-9A — Document Status Governance
- določa statuse dokumentov (DRAFT / INIT / ACTIVE / LOCKED)

**Status:** INIT

---

### 🟡 SP-13 — Change Management Protocol
- ureja predlaganje, odobritev in izvedbo sprememb

**Status:** INIT

---

### 🟡 SP-14 — Configuration & Policy Versioning
- določa verzioniranje in aktivacijo politik

**Status:** INIT

---

### 🟡 SP-15 — Access Control & Authority Protocol
- določa avtoritetne ravni in dostopne pravice

**Status:** INIT

---

### 🟡 SP-16 — Delegation & Trust Protocol
- ureja delegacijo avtoritete in preklic zaupanja

**Status:** INIT

---

## 5️⃣ KLJUČNA NAČELA SISTEMA

SAPIANTA temelji na naslednjih nespremenljivih načelih:

- Explain ≠ Audit ≠ Trace
- Governance > Implementacija
- Brez implicitnih pravic
- Brez retroaktivnih sprememb
- Containment ima prednost pred razlago
- Odgovornost ostaja pri delegatorju

---

## 6️⃣ OPERATIVNE POSLEDICE

- AI ne more samovoljno razlagati odločitev
- Audit ne more eskalirati v nadzor nad jedrom
- Incidenti se obravnavajo brez improvizacije
- Spremembe so sledljive in nadzorovane
- Delegacija je vedno omejena in preklicljiva

---

## 7️⃣ UPORABA DOKUMENTA

Ta snapshot se uporablja za:
- onboarding novih sodelavcev
- razlago sistema regulatorjem
- notranjo orientacijo pri razvoju
- referenco pred zaklepanjem novih faz

---

## 8️⃣ STATUS SNAPSHOTA

Ta dokument je **referenčen** in se lahko posodablja
z novimi verzijami (v2, v3, …) brez vpliva na zaklenjene faze.

---
