# MPL_DEFINITION.md
Status: FINAL · PROOF LOCK
Vezano na: F47_LOCK
Namen: Formalna definicija Minimal Proof Loop (MPL)

---

## 1. NAMEN MPL

Minimal Proof Loop (MPL) je dokazni mehanizem, s katerim Sapianta
tehnično ratificira izvršljivost in neobidljivost Canona,
kot je določen v F47_RUNTIME_ENFORCEMENT.md.

MPL:
- ne uvaja novih normativnih pravil
- ne spreminja Canona
- ne razširja sistema

MPL obstaja izključno kot dokaz.

---

## 2. OBSEG MPL

MPL pokriva točno en zaprt tok:

INPUT
→ Canon preverjanje (SP-1)
→ LLM dovoljenje (SP-2)
→ LLM odgovor
→ Canon preverjanje (SP-3)
→ OUTPUT ali HALT

Izrecno izven obsega MPL:
- agenti
- moduli
- orodja
- verižni klici
- UX logika

---

## 3. DOKAZNA ARTEFAKTA MPL

MPL je sestavljen iz treh obveznih artefaktov:

### A. Testni scenariji
Datoteka:
docs/mpl/MPL_TEST_SCENARIOS.md

Vsebuje:
- deterministične testne primere
- pozitivne in negativne dokaze
- prepoved bypass mehanizmov

---

### B. Izvršilna psevdo-koda
Datoteka:
docs/mpl/MPL_PSEUDOCODE.md

Vsebuje:
- natančen algoritmični tok
- fiksne stop-točke (SP-1, SP-2, SP-3)
- eksplicitne HALT in HARD_FAIL pogoje

---

### C. Normativna osnova
Datoteka:
docs/phases/F47_RUNTIME_ENFORCEMENT.md

Določa:
- obveznost zaustavitve
- prepoved interpretacije
- izvršilno hierarhijo Canona

---

## 4. KRITERIJ USPEHA MPL

MPL je uspešen, če in samo če:
- vsi testni scenariji PASS
- ni konfiguracijskih izjem
- ni bypass flagov
- ni implicitnih ALLOW poti

Če en sam pogoj ni izpolnjen:
MPL FAIL

---

## 5. ODNOS DO NADALJNJIH FAZ

MPL:
- ne nadomešča F48–F50
- ne odpira normativnih vprašanj
- zaklene prehod iz normativne gradnje v tehnično verifikacijo

F48–F50 se lahko začnejo šele po uspešnem MPL.

---

## 6. STATUS ZAKLEPA

Ta dokument:
- je zaklenjen po uspešnem MPL
- se ne dopolnjuje
- se ne interpretira
- služi kot trajna referenca dokaznega stanja

---

## 7. KONČNA IZJAVA

Canon brez dokazljivega enforcementa je deklaracija.
MPL je dokaz, da Canon deluje kot sistem.

