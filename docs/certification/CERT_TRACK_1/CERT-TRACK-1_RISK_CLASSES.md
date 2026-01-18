# CERT-TRACK-1 — REGULATORY CERTIFICATION TRACK
## CERT-TRACK-1_RISK_CLASSES

### Status
**ACTIVE — CONCEPTUAL RISK CLASSIFICATION**

---

## 1. NAMEN DOKUMENTA

Ta dokument določa **konceptualno razvrstitev tveganj** za PRODUCT-1
glede na **vlogo sistema v procesu**.

Dokument:
- ne uporablja pravnih kategorij
- ne navaja zakonodaje
- ne določa obveznosti
- ne ocenjuje skladnosti

Njegov namen je izključno:
> **strukturirati razumevanje tveganj kot funkcije sistemske vloge.**

---

## 2. NAČELO RAZVRŠČANJA TVEGANJ

Tveganje v kontekstu PRODUCT-1:
- ne izhaja iz tehnologije same
- ne izhaja iz zmogljivosti modela
- ne izhaja iz implementacijskih podrobnosti

Tveganje izhaja iz:
> **načina, kako sistem sodeluje pri odločitvah in vpliva na nadaljnje korake.**

Zato je razvrščanje izvedeno **po vlogah**, ne po funkcijah.

---

## 3. RAZREDI TVEGANJ PO VLOGAH SISTEMA

### 3.1 Razred R0 — Informativna / Svetovalna vloga

**Opis vloge:**
- sistem podaja informacije
- sistem ne pogojuje odločitev
- sistem ne omejuje nadaljnjih dejanj

**Značilnosti tveganja:**
- nizko kontekstualno tveganje
- tveganje izhaja predvsem iz napačnega razumevanja
- posledice so posredne

**Regulatorni interes (konceptualno):**
- jasnost vloge
- preprečevanje implicitne avtoritete

---

### 3.2 Razred R1 — Podporna vloga pri odločanju

**Opis vloge:**
- sistem strukturira možnosti
- sistem vpliva na potek odločanja
- končna odločitev ostaja človeška

**Značilnosti tveganja:**
- srednje kontekstualno tveganje
- tveganje pristranskosti ali prekomernega zaupanja
- posledice so odvisne od konteksta uporabe

**Regulatorni interes (konceptualno):**
- razmejitev odgovornosti
- transparentnost vpliva sistema

---

### 3.3 Razred R2 — Omejevalna ali pogojna vloga

**Opis vloge:**
- sistem omejuje dovoljene izhode
- sistem zahteva eksplicitno soglasje
- sistem blokira nedovoljene poti

**Značilnosti tveganja:**
- povišano sistemsko tveganje
- tveganje napačnih omejitev
- tveganje operativnih posledic

**Regulatorni interes (konceptualno):**
- utemeljitev omejitev
- možnost pregleda in revizije

---

### 3.4 Razred R3 — Nadzorna / revizijska vloga

**Opis vloge:**
- sistem nadzira procese
- sistem zaznava odklone
- sistem ne izvaja odločitev

**Značilnosti tveganja:**
- tveganje napačne zaznave
- tveganje lažnih pozitivnih ali negativnih zaznav
- vpliv na zaupanje v proces

**Regulatorni interes (konceptualno):**
- zanesljivost nadzora
- sledljivost zaznav

---

## 4. DINAMIČNOST RAZREDOV

Razred tveganja:
- ni statična lastnost produkta
- ni vezan na modul ali funkcijo

Razred je:
> **lastnost konkretne uporabe PRODUCT-1 v določenem kontekstu.**

Isti produkt lahko hkrati deluje v več razredih tveganja.

---

## 5. RAZMERJE DO PRODUKTNE IDENTITETE

Razvrstitev tveganj:
- ne spreminja identitete produkta
- ne vpliva na obseg PRODUCT-1
- ne uvaja produktnih omejitev

Služi kot:
> **analitično orodje za regulatorni tok**, ne kot produktna definicija.

---

## 6. UPORABA V NADALJNJIH FAZAH

Ta razvrstitev predstavlja osnovo za:
- regulatorni dialog
- jurisdikcijsko presojo
- identifikacijo relevantnih zahtev

Brez:
- avtomatskih sklepov
- pravnih kvalifikacij
- obljub skladnosti

---

### CERT-TRACK-1_RISK_CLASSES — ZAKLJUČENO

Ta dokument določa, kako razumeti tveganje
kot funkcijo **vloge sistema**, ne njegove tehnologije.
