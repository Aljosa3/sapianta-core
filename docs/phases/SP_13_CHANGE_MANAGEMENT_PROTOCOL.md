# SP-13 — CHANGE MANAGEMENT PROTOCOL (CMP)

**Status:** INIT  
**Vloga:** governance protokol za nadzor, odobritev, izvedbo in sledljivost sprememb v sistemu SAPIANTA

---

## 1️⃣ NAMEN FAZE

SP-13 določa **zavezujoč okvir** za upravljanje sprememb, ki:
- preprečuje nenadzorovane posege v sistem
- zagotavlja sledljivost in odgovornost
- ločuje eksperimentiranje od produkcijske stabilnosti
- varuje Canon, Core Laws in zaklenjene faze

SP-13 **ne definira tehnične implementacije sprememb**, temveč **pravila njihovega upravljanja**.

---

## 2️⃣ OPREDELITEV SPREMEMBE

Sprememba je vsak poseg, ki:
- spreminja obnašanje sistema
- spreminja governance pravila
- spreminja obseg razlage, audita ali hrambe
- uvaja ali odstranjuje funkcionalnost
- vpliva na uporabniško ali regulatorno zaznavo

Refaktor brez spremembe vedenja **ni** sprememba v smislu SP-13, če je dokazljivo nevtralen.

---

## 3️⃣ KATEGORIJE SPREMEMB

### 🔹 Kategorija I — Kritične
- poseg v Canon ali Core Laws
- sprememba zaklenjenih (LOCKED) faz
- sprememba varnostnih ali normativnih meja

### 🔹 Kategorija II — Pomembne
- sprememba ACTIVE faz
- sprememba governance protokolov
- sprememba audit ali retention politike

### 🔹 Kategorija III — Manjše
- sprememba INIT faz
- pojasnila brez semantičnega vpliva
- tehnični popravki brez vpliva na vedenje

---

## 4️⃣ POSTOPEK PREDLAGANJA SPREMEMBE

Vsaka sprememba mora imeti:
- jasen opis namena
- kategorizacijo (I / II / III)
- utemeljitev potrebe
- oceno vpliva
- predlagan čas uveljavitve

Neopredeljene spremembe so **neveljavne**.

---

## 5️⃣ ODOBRITEV SPREMEMB

| Kategorija | Zahteva |
|-----------|---------|
| I | Nova faza + izrecna odobritev |
| II | Razširitvena faza ali amandma |
| III | Dovoljena v okviru INIT |

Sprememba brez ustrezne odobritve:
> se šteje za **kršitev protokola**.

---

## 6️⃣ IZVEDBA SPREMEMBE

Spremembe se izvajajo:
- postopno
- sledljivo
- reverzibilno (kjer je mogoče)

Izvedba mora:
- ohraniti obstoječe odločitve
- ne uvajati retroaktivnih sprememb
- ne razbijati sledljivosti

---

## 7️⃣ DOKUMENTIRANJE

Vsaka sprememba mora biti:
- dokumentirana v ustrezni fazi
- povezana s commit-i
- časovno označena
- povezana z odgovorno osebo ali procesom

Dokumentacija je **del spremembe**, ne dodatna obveznost.

---

## 8️⃣ PREVERJANJE IN VALIDACIJA

Po izvedbi spremembe se izvede preverjanje, ki:
- potrdi skladnost s SP-9 do SP-12
- preveri nepredvidene učinke
- potrdi, da ni prišlo do razširitve razlage ali audita

Neuspešno preverjanje:
> zahteva povrnitev ali korekcijo.

---

## 9️⃣ NUJNE SPREMEMBE (EMERGENCY)

V nujnih primerih je dovoljena začasna sprememba, če:
- preprečuje neposredno škodo
- je časovno omejena
- je naknadno dokumentirana

Vsaka nujna sprememba mora biti:
- označena kot **EMERGENCY**
- predmet naknadnega pregleda

---

## 🔟 RAZMERJE DO DRUGIH FAZ

SP-13:
- temelji na SP-9, SP-10, SP-11 in SP-12
- ne spreminja Canona ali Core Laws
- ne posega v runtime implementacijo
- deluje izključno kot governance protokol

---

## 1️⃣1️⃣ STATUS FAZE

Ta dokument ima status **INIT**.

Zaklep (LOCK) se lahko izvede po vsaj eni uspešni spremembi brez regresij.

---
