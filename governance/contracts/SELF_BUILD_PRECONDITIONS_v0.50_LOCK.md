# SELF_BUILD_PRECONDITIONS_v0.50_LOCK

STATUS: LOCKED  
PHASE: v0.50  
SCOPE: Self-Build Preconditions & Normative Import  
MUTABILITY: IMMUTABLE  

DEPENDENCIES:
- v0.34 — Decision Preview Presentation Schema (LOCKED)
- v0.35 — Validator Enforcement (LOCKED)
- v0.36 — Runtime Integration Contract (LOCKED)
- v0.37 — Failure Propagation & Audit Semantics (LOCKED)
- v0.38 — Audit Event Schema (LOCKED)
- v0.39 — Audit Index & Sanity-Check (LOCKED)
- v0.40 — Decision Preview Exposure / Surface Contract (LOCKED)
- v0.41 — Surface Adapter Contract (LOCKED)
- v0.42 — Surface Adapter Compliance Harness (LOCKED)

EXPLICIT NON-DEPENDENCIES:
- vsebina normativnih dokumentov
- interpretacija naravnega jezika
- UI / surface adapterji
- audit zapisi
- compliance rezultati
- runtime heuristike
- učenje ali prilagajanje na podlagi zgodovine

---

## 1. NAMEN DOKUMENTA

Ta dokument normativno določa **Self-Build Preconditions**.

Namen faze v0.50 je:
- določiti **ali** je samogradnja modulov dovoljena,
- izključno na podlagi **normativnega stanja sistema**,
- brez branja ali interpretacije vsebine predhodnih faz.

v0.50 ne opisuje samogradnje.  
v0.50 določa **pravico do začetka samogradnje**.

---

## 2. DEFINICIJA SAMOGRADNJE (NORMATIVNO)

Samogradnja je normativna **pravica**, ne tehnična zmožnost.

Samogradnja:
- ni runtime odločanje,
- ni izvedbeni mehanizem,
- ni učni proces.

Obstoj gradbenih mehanizmov **ne implicira** dovoljenja za njihovo uporabo.

---

## 3. NORMATIVNI UVOZ FAZ (NON-SEMANTIC IMPORT)

v0.50 uvaža predhodne faze **izključno** kot:

- obstoj faze,
- identiteto faze,
- status zaklepa (LOCKED).

Izrecno je prepovedano:
- branje vsebine dokumentov,
- povzemanje pravil,
- interpretacija pomena besedila,
- sklepanje o namenu faz.

Faze so v v0.50 **strukturni artefakti**, ne semantični viri.

---

## 4. OBVEZNI PREDPOGOJI ZA SAMOGRADNJO

Samogradnja je dovoljena **le, če** so izpolnjeni vsi naslednji pogoji:

- vse faze v0.34–v0.42 obstajajo,
- vse navedene faze imajo status LOCKED,
- nobena faza ni označena kot delno veljavna ali pogojna.

Če je katerikoli pogoj neizpolnjen, je samogradnja **prepovedana**.

---

## 5. PRECONDITION MATRIX (MACHINE-CHECKABLE)

| Faza | Zahtevan status | Učinek |
|-----|------------------|--------|
| v0.34 | LOCKED | required |
| v0.35 | LOCKED | required |
| v0.36 | LOCKED | required |
| v0.37 | LOCKED | required |
| v0.38 | LOCKED | required |
| v0.39 | LOCKED | required |
| v0.40 | LOCKED | required |
| v0.41 | LOCKED | required |
| v0.42 | LOCKED | required |

Ne obstajajo izjeme ali alternativne poti.

---

## 6. NO-SELF-BUILD STANJE

NO-SELF-BUILD je veljavno normativno stanje.

V tem stanju:
- samogradnja se ne izvaja,
- ni nadomestnega ali delnega delovanja,
- ni fallback mehanizmov.

Tišina in neaktivnost sta pravilno vedenje.

---

## 7. PREPOVED SIGNALOV ZA SAMOGRADNJO

Samogradnja **ne sme** uporabljati signalov iz:

- UI ali surface adapterjev,
- audit zapisov,
- compliance rezultatov,
- validator PASS/FAIL zaporedij,
- runtime vedenja ali časovnih korelacij.

Samogradnja se ne uči iz zgodovine in ne sklepa iz opazovanja.

---

## 8. RAZMERJE MED SAMOGRADNJO IN RUNTIME

Samogradnja:
- ne spreminja runtime pravil,
- ne vpliva na runtime odločanje,
- ne prejema signalov iz runtime toka.

Runtime ne signalizira samogradnji in ne sodeluje pri precondition presoji.

---

## 9. RAZMERJE MED SAMOGRADNJO IN VALIDATORJEM

Validator ostaja binaren in determinističen.

Samogradnja:
- ne sklepa iz validatorjevih izidov,
- ne prilagaja vedenja na podlagi PASS/FAIL,
- validatorja ne uporablja kot gradbeni signal.

---

## 10. FAZNA DISCIPLINA PO v0.50

Po v0.50:
- ni dovoljeno dodajanje novih normativnih faz,
- ni dovoljeno retroaktivno spreminjanje faz v0.34–v0.42,
- vse nadaljnje razširitve so:
  - moduli,
  - koda,
  - izvedbeni artefakti.

Ustavna plast se po v0.50 ne širi več.

---

## 11. PHASE BOUNDARY CLAUSE (v0.50)

v0.50:
- ne opisuje, kako se samogradnja izvaja,
- ne opisuje, kaj se gradi,
- ne opisuje, kdaj se gradi.

v0.50 določa **izključno**, ali je samogradnja normativno dovoljena.

---

## 12. SKLADNOST, ZAKLEP IN NEPOVRATNOST

Ta dokument:
- je skladen z v0.34–v0.42,
- ne interpretira njihove vsebine,
- ne uvaja novih semantičnih pravil.

Dokument **SELF_BUILD_PRECONDITIONS_v0.50_LOCK.md** je s tem
**DOKONČNO ZAKLENJEN** in se ne sme več spreminjati.

---
