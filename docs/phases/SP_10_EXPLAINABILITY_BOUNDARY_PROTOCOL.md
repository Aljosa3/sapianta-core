# SP-10 — EXPLAINABILITY BOUNDARY PROTOCOL (EBP)

**Status:** INIT  
**Vloga:** governance protokol za določanje mej med explainability, audit evidence in execution trace v sistemu SAPIANTA

---

## 1️⃣ NAMEN FAZE

SP-10 določa **zavezujoče meje**, kaj sistem SAPIANTA:
- sme razlagati (explain)
- mora dokazovati (audit)
- mora slediti (trace)
- in česa **ne sme nikoli razkrivati**

Cilj faze je preprečiti:
- explain-driven drift
- retroaktivno razstavljanje odločitev
- zamenjavo razlogov z razlagami
- prekomerno ali nevarno transparentnost

SP-10 ne povečuje transparentnosti.
SP-10 jo **omeje in strukturira**.

---

## 2️⃣ TEMELJNO NAČELO

> **Razlaga ni razlog.  
> Audit ni razlaga.  
> Trace ni audit.**

Vsak od teh slojev ima **ločeno vlogo, občinstvo in dovoljeni obseg**.

---

## 3️⃣ DEFINICIJE SLOJEV

### 🔹 EXPLAIN (Explainability Layer)
- namenjena uporabniku ali operaterju
- odgovarja na vprašanje: *“Kaj se je zgodilo?”*
- ne razkriva:
  - notranjih pravil
  - uteži
  - policy hierarhije
  - alternativnih zavrnjenih poti

Explain je **interpretativen povzetek**, ne dokaz.

---

### 🔹 AUDIT (Audit Evidence Layer)
- namenjen nadzornemu organu ali notranjemu auditu
- odgovarja na vprašanje: *“Ali je sistem deloval skladno s pravili?”*
- vsebuje:
  - reference na veljavne politike
  - časovne oznake
  - identifikatorje odločitev

Audit **ne razlaga**, temveč **dokazuje skladnost**.

---

### 🔹 TRACE (Execution Trace Layer)
- namenjen izključno sistemu
- odgovarja na vprašanje: *“Kaj je bilo izvedeno?”*
- vsebuje:
  - tehnične zapise
  - interne identifikatorje
  - zaporedje izvrševanja

Trace **ni razkritljiv uporabniku ali auditorju**, razen v agregirani obliki.

---

## 4️⃣ ABSOLUTNE MEJE (HARD BOUNDARIES)

Sistem SAPIANTA **NE SME**:

- razlagati notranjih razlogov odločitev
- razkrivati alternativnih zavrnjenih poti
- pretvarjati trace v explain
- pretvarjati explain v dokaz
- omogočiti rekonstrukcije odločitve nazaj do policy jedra

Kršitev teh mej pomeni **sistemsko napako**.

---

## 5️⃣ NAČELO MINIMALNEGA DOKAZA

> Sistem mora zagotoviti **najmanjši možni obseg dokazov**, ki še vedno omogoča preverjanje skladnosti.

To pomeni:
- audit evidence je **omejena**
- čas hrambe je **politika**, ne privzeto stanje
- trace se ne hrani brez izrecne potrebe

---

## 6️⃣ RAZMERJE DO EU AI ACT

SP-10 omogoča skladnost z zahtevami EU AI Act, ker:
- ločuje explainability od auditability
- omogoča dokazovanje brez razkrivanja jedra
- podpira selektivno hrambo podatkov
- preprečuje prekomerno razlago kot varnostno tveganje

---

## 7️⃣ RAZMERJE DO DRUGIH FAZ

- SP-10 temelji na:
  - SP-9 (AI Output Governance)
  - SP-9A (Document Status Governance)
- SP-10 ne spreminja:
  - Canona
  - Core Laws
  - runtime mehanizmov
- SP-10 uvaja **governance mejo**, ne tehnične implementacije

---

## 8️⃣ STATUS FAZE

Ta dokument ima status **INIT**.

Zaklep (LOCK) se lahko izvede v kasnejši fazi po implementacijskem preverjanju.

---
