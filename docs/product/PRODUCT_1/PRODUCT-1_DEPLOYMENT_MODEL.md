# PRODUCT-1 — SAPIANTA REGULATED AI PLATFORM
## PRODUCT-1_DEPLOYMENT_MODEL

### Status
**ACTIVE — DEPLOYMENT MODEL DEFINITION**

---

## 1. NAMEN DOKUMENTA

Ta dokument določa **konceptualne modele dostave (deployment)** produkta PRODUCT-1.

Dokument:
- ne opisuje infrastrukture
- ne predpisuje tehničnih rešitev
- ne omejuje implementacijskih odločitev

Njegov namen je:
> **opredeliti, v kakšnih oblikah se PRODUCT-1 lahko legitimno uporablja in distribuira.**

---

## 2. NAČELA DEPLOYMENTA

Vsi deployment modeli PRODUCT-1 morajo spoštovati naslednja načela:

- nespremenljivost jedra
- nadrejenost governance sloja
- ločitev odločanja, izvedbe in nadzora
- možnost uveljavljanja jurisdikcijskih omejitev
- ohranitev sledljivosti in revizije

Deployment model **ne sme** obiti ali oslabiti teh načel.

---

## 3. PODPRTI DEPLOYMENT MODELI (KONCEPTUALNO)

PRODUCT-1 podpira naslednje **konceptualne deployment oblike**:

### 3.1 Centralizirana storitev (SaaS)

Produkt je dostavljen kot upravljana storitev, kjer:
- je jedro centralno vzdrževano
- so politike in posodobitve nadzorovane
- so uporabniki vezani na definirane vstopne točke

Ta model je primeren za okolja, kjer:
- je potrebna poenotena governance
- je centralni nadzor zaželen

---

### 3.2 Lokalna namestitev (On-Premises)

Produkt je nameščen v nadzorovanem lokalnem okolju uporabnika ali organizacije.

Ta model:
- omogoča večjo avtonomijo
- zahteva večjo odgovornost uporabnika
- ne razveljavlja dedovanih invarianc

Jedro in governance ostajata nespremenjena ne glede na lokacijo izvajanja.

---

### 3.3 Hibridni modeli

Kombinacija centraliziranih in lokalnih komponent, kjer:
- določeni deli sistema delujejo lokalno
- določeni deli ostajajo centralno nadzorovani

Hibridni modeli so dovoljeni, dokler:
- ne razbijejo sistemskih meja
- ne omogočajo obhoda governance slojev

---

### 3.4 Vmesniški dostop (API / SDK / CLI)

PRODUCT-1 je lahko dostopen preko:
- programskih vmesnikov
- razvojnih kompletov
- nadzorovanih uporabniških vmesnikov

Ti načini dostopa **niso samostojni produkti**, temveč:
> **vstopne točke v isti regulirani sistem.**

---

## 4. NEPODPRTI DEPLOYMENT MODELI

Naslednji modeli so **izrecno izključeni**:

- decentralizirane ali nekontrolirane replikacije jedra
- avtonomno razmnoževanje ali samostojna redistribucija
- “offline” uporaba brez možnosti uveljavljanja governance
- deployment, ki onemogoča audit ali sledljivost

Takšni modeli so nezdružljivi z identiteto PRODUCT-1.

---

## 5. STABILNOST DEPLOYMENTA

Deployment model:
- ne spreminja identitete produkta
- ne spreminja njegovega obsega
- ne redefinira odgovornosti

Sprememba deploymenta je **operativna odločitev**, ne produktna redefinicija.

---

### PRODUCT-1_DEPLOYMENT_MODEL — ZAKLJUČENO

Ta dokument določa dovoljene oblike dostave PRODUCT-1.

Kako je produkt nameščen, je variabilno.  
Kaj produkt je, ostaja nespremenjeno.
