# IMPLEMENTATION TRACK — GOVERNANCE-FIRST EXECUTION
## IMPLEMENTATION_TRACK_RUNTIME_SKELETON

### Status
**ACTIVE — RUNTIME SKELETON DEFINITION**

---

## 1. NAMEN DOKUMENTA

Ta dokument določa **minimalni runtime skelet** sistema SAPIANTA.

Namen dokumenta je:
> **opredeliti, katere logične runtime komponente obstajajo
in kakšna je njihova vloga — brez implementacijskih podrobnosti.**

Dokument:
- ne opisuje arhitekture
- ne predpisuje tehnologij
- ne definira podatkovnih struktur
- ne uvaja izvajanja

Služi kot:
> **orientacijski okvir za implementacijo**, ne kot tehnična specifikacija.

---

## 2. NAČELO RUNTIME-A

Runtime sistema SAPIANTA:
- ne sprejema normativnih odločitev
- ne interpretira pravil
- ne ustvarja regulatornih pomenov

Runtime:
> **izvaja tokove, ki so bili določeni zunaj njega.**

---

## 3. OSNOVNE RUNTIME KOMPONENTE (KONCEPTUALNO)

### 3.1 Vhodni vmesnik (Input Boundary)

Vloga:
- sprejem vhodov
- validacija oblike (ne vsebine)
- usmerjanje v nadaljnji tok

Ne sme:
- presojati dovoljenosti
- interpretirati pomena
- zavračati na normativni osnovi

---

### 3.2 Kontekstualni nosilec (Context Carrier)

Vloga:
- prenašanje konteksta skozi tok
- ohranjanje sledljivosti
- brez interpretacije

Kontekst:
> **ni odločitev**, temveč nosilec informacij.

---

### 3.3 Izvedbeni tok (Execution Flow)

Vloga:
- zaporedno ali vzporedno izvajanje korakov
- klicanje modulov
- obvladovanje tehničnega poteka

Ne sme:
- spreminjati vloge sistema
- presojati tveganj
- odločati o izidih

---

### 3.4 Opazovalni tok (Observation Flow)

Vloga:
- zaznavanje dogodkov
- beleženje tehničnih signalov
- podpora sledljivosti

Ne sme:
- interpretirati dogodkov
- označevati kršitev
- ustvarjati normativnih sodb

---

### 3.5 Izhodni vmesnik (Output Boundary)

Vloga:
- oblikovanje izhodov
- posredovanje rezultatov
- tehnična dostava

Ne sme:
- trditi veljavnosti
- razširjati pomena
- nadomeščati razlage ali revizije

---

## 4. PREPOVEDANI RUNTIME VZORCI

Runtime **ne sme** vsebovati:

- odločitev skritih v pretokih
- pravil, zakodiranih v tokovih
- implicitnih “fallback” odločitev
- avtomatskih eskalacij brez zunanje presoje

Če se tak vzorec pojavi:
> **je to kršitev architecture boundaries.**

---

## 5. RAZMERJE DO MODULOV

Runtime:
- orkestrira module
- ne razume njihove vsebine
- ne presoja njihovega rezultata

Moduli:
> **so orodja runtime-a, ne njegovi odločevalci.**

---

## 6. SLEDLJIVOST BREZ ODLOČANJA

Runtime mora omogočati:
- rekonstrukcijo poteka
- časovno zaporedje
- identifikacijo korakov

Brez:
- interpretacije
- utemeljevanja
- normativnega pomena

---

## 7. POSLEDICE ZA IMPLEMENTACIJO

Ta skelet pomeni, da:

- runtime ostaja “tanek”
- več logike obstaja zunaj izvajanja
- implementacija je lažje preverljiva
- normativni drift je lažje zaznati

To je **namenska arhitekturna odločitev**.

---

### IMPLEMENTATION_TRACK_RUNTIME_SKELETON — ZAKLJUČENO

Ta dokument določa,
kaj runtime **je** — in česa **ne sme početi**.

Izvajanje brez odločanja.  
Tok brez sodbe.
