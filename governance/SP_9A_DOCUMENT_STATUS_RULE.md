# SP-9A — STATUS INITIALIZATION RULE

**Status:** INIT  
**Vloga:** governance pravilo za inicializacijo, razlago in uporabo statusov dokumentov v sistemu SAPIANTA

---

## 1️⃣ NAMEN FAZE

SP-9A določa **enotno in obvezno pravilo**, kako se v sistemu SAPIANTA:
- inicializira status dokumentov
- razlaga njihov normativni pomen
- izvaja prehod med statusi

Cilj faze je preprečiti:
- implicitne “active by default” statuse
- normativno zmedo med INIT / ACTIVE / LOCKED
- nejasno veljavnost dokumentov skozi čas

SP-9A **ne ureja vsebine dokumentov**, temveč izključno **njihov statusni pomen**.

---

## 2️⃣ KLJUČNO PRAVILO (JEDRO)

> **Vsak dokument brez izrecno zapisanega statusa se šteje za DRAFT in nima nobene normativne teže.**

To je zavezujoče pravilo.

---

## 3️⃣ DOVOLJENI STATUSI

Edini dovoljeni statusi dokumentov v sistemu SAPIANTA so:

- `DRAFT` – delovno, nestabilno
- `INIT` – inicializirano, struktura potrjena
- `ACTIVE` – veljavno in uporabljeno
- `LOCKED` – normativno zaklenjeno
- `DEPRECATED` – ohranjeno za sledljivost, neaktivno

Vsak dokument mora imeti **točno en** status.

---

## 4️⃣ POMEN POSAMEZNIH STATUSOV

### 🔹 DRAFT
- dokument je v nastajanju
- spremembe so proste
- nima normativne ali operativne teže

### 🔹 INIT
- struktura dokumenta je potrjena
- vsebina še ni normativno zaklenjena
- dovoljena so popravila brez nove faze

### 🔹 ACTIVE
- dokument je veljaven in v uporabi
- spremembe zahtevajo novo fazo ali razširitveni dokument

### 🔹 LOCKED
- dokument je normativno zaklenjen
- spremembe niso dovoljene
- dovoljena je le nadgradnja z novo fazo

### 🔹 DEPRECATED
- dokument ostaja v repozitoriju
- nima več operativne ali normativne vloge
- služi zgodovinski sledljivosti

---

## 5️⃣ OBVEZNA OBLIKA STATUSA

Vsak dokument **mora** na vrhu vsebovati vrstico v obliki:

```markdown
**Status:** INIT
