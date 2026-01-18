# IMPLEMENTATION TRACK — GOVERNANCE-FIRST EXECUTION
## IMPLEMENTATION_TRACK_ARCHITECTURE_BOUNDARIES

### Status
**ACTIVE — ARCHITECTURE BOUNDARIES DEFINITION**

---

## 1. NAMEN DOKUMENTA

Ta dokument določa **arhitekturne meje (architecture boundaries)**,
znotraj katerih je implementacija sistema SAPIANTA dovoljena.

Namen dokumenta je:
> **preprečiti, da bi tehnična implementacija implicitno spreminjala
normativne, produktne ali regulatorne odločitve.**

Dokument:
- ne opisuje arhitekture
- ne predpisuje tehnologij
- ne uvaja implementacijskih rešitev

Določa izključno **meje poseganja**.

---

## 2. TEMELJNO NAČELO

Implementacijska arhitektura mora:
> **odražati že sprejete odločitve, ne pa jih nadomeščati ali reinterpretirati.**

Če arhitekturna odločitev:
- zahteva novo normativno presojo
- spreminja vlogo sistema
- vpliva na regulatorne stike

potem **ni dovoljena** v tem implementacijskem toku.

---

## 3. TRDNO ZAPRTE ARHITEKTURNE DOMENE

Naslednje domene so **izrecno zaprte** za implementacijske posege:

### 3.1 Governance domena

Implementacija:
- ne sme kodirati pravil kot “business logic”
- ne sme izvajati normativnih odločitev brez sledljivosti
- ne sme obhajati kanona

Governance ostaja:
> **nad-arhitekturna plast**, ne implementacijski modul.

---

### 3.2 Produktna identiteta

Implementacija:
- ne sme redefinirati obsega PRODUCT-1
- ne sme ustvarjati novih produktnih lastnosti
- ne sme uvajati implicitnih funkcij

Vsaka sprememba produktne identitete:
> **zahteva nov produktni dokument**, ne kodo.

---

### 3.3 Regulatorne trditve

Implementacija:
- ne sme implicitno trditi skladnosti
- ne sme generirati “compliance signalov”
- ne sme nadomestiti regulatorne presoje

Tehnični mehanizmi:
> **niso dokaz skladnosti.**

---

## 4. POGOJNO DOVOLJENE ARHITEKTURNE DOMENE

Naslednje domene so dovoljene **le v omejenem obsegu**:

### 4.1 Runtime struktura

Dovoljeno je:
- definirati tehnične tokove
- vzpostaviti osnovne komponente
- ločiti sloje izvajanja

Pod pogojem, da:
- runtime ne sprejema normativnih odločitev
- runtime ne interpretira pravil

---

### 4.2 Modulna organizacija

Dovoljeno je:
- konceptualno ločiti module
- vzpostaviti tehnične meje

Ni dovoljeno:
- da modul postane nosilec pravil
- da modul samostojno spreminja obnašanje sistema

---

### 4.3 Nadzor in opazovanje

Dovoljeno je:
- tehnično zaznavanje dogodkov
- zbiranje signalov

Ni dovoljeno:
- interpretirati dogodke kot kršitve
- generirati normativne sodbe

---

## 5. PREPOZNAVANJE ARHITEKTURNEGA DRIFT-A

Naslednji znaki pomenijo **arhitekturni drift**:

- “To je samo tehnična odločitev”
- “Za zdaj bomo to hardcode-ali”
- “Kasneje bomo dokumentirali”
- “To nima vpliva na governance”

Vsak tak primer:
> **zahteva zaustavitev in povratek v dokumentacijski tok.**

---

## 6. ODGOVORNOST IMPLEMENTACIJE

Implementacija je odgovorna za:
- tehnično korektnost
- sledljivost
- reverzibilnost

Ni pa odgovorna za:
- normativne odločitve
- regulatorno presojo
- produktno strategijo

---

### IMPLEMENTATION_TRACK_ARCHITECTURE_BOUNDARIES — ZAKLJUČENO

Ta dokument določa,
česa implementacija **ne sme** storiti.

Njegova vloga je zaščitna,
ne omejevalna.
