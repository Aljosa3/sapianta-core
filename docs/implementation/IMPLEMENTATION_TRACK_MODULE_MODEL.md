# IMPLEMENTATION TRACK — GOVERNANCE-FIRST EXECUTION
## IMPLEMENTATION_TRACK_MODULE_MODEL

### Status
**ACTIVE — MODULE MODEL DEFINITION**

---

## 1. NAMEN DOKUMENTA

Ta dokument opredeljuje **model modulov** v implementacijskem toku sistema SAPIANTA.

Namen dokumenta je:
> **določiti, kaj modul je in kaj modul ni**, brez uvajanja kode, tehnologij ali arhitekturnih rešitev.

Dokument:
- ne predpisuje implementacije
- ne določa API-jev
- ne opisuje runtime-a

Določa **konceptualni okvir**, ki preprečuje, da bi moduli postali nosilci
normativnih ali regulatornih odločitev.

---

## 2. DEFINICIJA MODULA

V kontekstu SAPIANTA je **modul**:

> **izolirana funkcionalna enota, ki izvaja točno eno tehnično vlogo
in nima lastne normativne avtoritete.**

Modul:
- ne sprejema odločitev
- ne interpretira pravil
- ne razširja produktnega obsega
- ne generira regulatornih trditev

---

## 3. TEMELJNA NAČELA MODULNE ZASNOVE

Vsak modul mora izpolnjevati naslednja načela:

### 3.1 Enonamenskost

Modul:
- izvaja eno jasno določeno nalogo
- nima stranskih učinkov izven svojega obsega

Če modul opravlja več vlog:
> **je napačno definiran.**

---

### 3.2 Brez normativne avtonomije

Modul:
- ne vsebuje pravil
- ne vsebuje politik
- ne vsebuje odločitev

Vse normativne presoje:
> **obstajajo zunaj modulov.**

---

### 3.3 Zamenljivost

Modul mora biti:
- tehnično zamenljiv
- logično nadomestljiv
- reverzibilen

Če odstranitev modula:
- spremeni obnašanje sistema na normativni ravni

potem modul:
> **krši ta model.**

---

### 3.4 Nevidnost navzven

Moduli:
- niso del javnega vmesnika
- niso produktna lastnost
- niso regulatorna entiteta

Modul obstaja:
> **izključno kot implementacijska podpora.**

---

## 4. DOVOLJENE VRSTE MODULOV

Naslednje vrste modulov so konceptualno dovoljene:

### 4.1 Izvedbeni moduli

- izvajajo tehnične operacije
- nimajo kontekstualnega razumevanja
- nimajo avtoritete

---

### 4.2 Pretvorbeni moduli

- pretvarjajo vhod v izhod
- ne vrednotijo vsebine
- ne ocenjujejo tveganj

---

### 4.3 Opazovalni moduli

- zbirajo signale
- beležijo dogodke
- ne interpretirajo pomena

---

## 5. IZRECNO PREPOVEDANE LASTNOSTI MODULOV

Modul **ne sme**:

- odločati o dovoljenosti dejanj
- ocenjevati skladnosti
- sklepati o tveganjih
- nadomeščati človeka
- ustvarjati implicitnih obljub

Če se zdi, da modul to počne:
> **gre za arhitekturni drift.**

---

## 6. RAZMERJE MODULOV DO DRUGIH SLOJEV

### 6.1 Razmerje do governance

Moduli:
- ne berejo kanona
- ne uveljavljajo pravil
- ne presojajo skladnosti

Governance:
> **ni implementirana v modulih.**

---

### 6.2 Razmerje do produkta

Moduli:
- ne definirajo funkcionalnosti
- ne razširjajo obsega
- ne ustvarjajo produktnih obljub

Produkt:
> **ostaja dokumentiran, ne kodiran.**

---

### 6.3 Razmerje do regulatornega toka

Moduli:
- ne proizvajajo dokazov
- ne generirajo regulatornih signalov
- ne komunicirajo z regulatorji

CERT-TRACK:
> **ostaja analitičen, ne tehničen.**

---

## 7. POSLEDICE ZA IMPLEMENTACIJO

Ta model pomeni, da:

- implementacija bo bolj modularna
- več odgovornosti ostane zunaj kode
- tehnična kompleksnost ne pomeni normativne kompleksnosti

To je **namenska omejitev**, ne pomanjkljivost.

---

### IMPLEMENTATION_TRACK_MODULE_MODEL — ZAKLJUČENO

Ta dokument določa,
kaj modul je — in predvsem, kaj **ne sme biti**.

Moduli izvajajo.  
Odločitve ostajajo drugje.
