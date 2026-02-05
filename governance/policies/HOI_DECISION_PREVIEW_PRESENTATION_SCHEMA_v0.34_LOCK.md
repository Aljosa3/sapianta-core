PATH: governance/policies/HOI_DECISION_PREVIEW_PRESENTATION_SCHEMA_v0.34_LOCK.md

# HOI_DECISION_PREVIEW_PRESENTATION_SCHEMA_v0.34_LOCK

Status: LOCK-READY  
Layer: HOI → Decision Preview  
Mode: READ-ONLY  
Paraphrase: DISALLOWED  
Interpretation: DISALLOWED  

---

## 1. NAMEN DOKUMENTA

Ta dokument normativno določa **točno strukturo izpisa** *Decision Preview*, ki ga HOI lahko prikaže uporabniku.

Dokument:
- definira dovoljene in obvezne tekstovne sekcije
- določa zaporedje sekcij
- določa dovoljene in prepovedane stringe
- preprečuje implicitno odločanje že na ravni jezika

Dokument ne:
- razlaga sistema
- uvaja logike
- opisuje UX
- opisuje namen odločitve

---

## 2. SPLOŠNA PRAVILA IZPISA

2.1. Izpis je determinističen  
2.2. Izpis je string-level fiksiran  

2.3. Izpis ne sme biti:
- parafraziran
- lokaliziran
- skrajšan
- razširjen
- poudarjen

2.4. HOI ne sme:
- dodati besed
- izpustiti besed
- zamenjati vrstnega reda
- dodati prehodnih stavkov

---

## 3. OBVEZNE SEKCIJE (MANDATORY SECTIONS)

Vsak *Decision Preview* **MORA** vsebovati vse spodaj navedene sekcije.  
Manjkajoča sekcija pomeni **INVALID PREVIEW OUTPUT**.

---

### 3.1. SECTION: PREVIEW_HEADER

Namen: Identifikacija izpisa  
Status: OBVEZNO  

Dovoljena vsebina (exact string):
DECISION PREVIEW


Prepovedano:
- dodajanje podnaslovov
- dodajanje ikon
- dodajanje oznak verzije
- dodajanje konteksta

---

### 3.2. SECTION: PREVIEW_SCOPE

Namen: Opredelitev obsega prikaza  
Status: OBVEZNO  

Dovoljena vsebina (exact string):
This output represents a non-executing, non-recommending preview of possible decision paths.


Prepovedano:
- sinonimi
- pojasnila
- dodatni stavki
- oklepaji

---

### 3.3. SECTION: PREVIEW_INPUT_REFERENCE

Namen: Sklic na vhodne podatke  
Status: OBVEZNO  

Struktura (fiksna):
Input reference:
- Source: <CANONICAL_INPUT_ID>


Pravila:
- `<CANONICAL_INPUT_ID>` je tehnični identifikator
- brez opisov
- brez datuma
- brez razlage izvora

---

### 3.4. SECTION: PREVIEW_DECISION_SPACE

Namen: Prikaz razpoložljivega odločitvenega prostora  
Status: OBVEZNO  

Struktura (fiksna):
Decision space:
- Path A
- Path B
- Path C


Pravila:
- oznake poti so nevtralne
- brez ordinalnih vrednosti
- brez opisov poti
- brez implikacij

---

### 3.5. SECTION: PREVIEW_CONSTRAINTS

Namen: Prikaz omejitev sistema  
Status: OBVEZNO  

Dovoljena vsebina (exact string):
Constraints:
- No recommendation is provided.
- No prioritization is applied.
- No outcome is predicted.


Prepovedano:
- dodatne alineje
- razlage omejitev
- poudarki (bold, caps)

---

### 3.6. SECTION: PREVIEW_DISCLAIMER

Namen: Pravna in semantična razmejitev  
Status: OBVEZNO  
Paraphrase: ABSOLUTNO PREPOVEDANO  

Exact string (neparafrazljiv):
This preview does not constitute advice, guidance, or a suggestion. The responsibility for any decision remains entirely with the user.


---

## 4. ZAPOREDJE SEKCIJ (ORDER RULES)

Zaporedje mora biti **točno** naslednje:
1. PREVIEW_HEADER
2. PREVIEW_SCOPE
3. PREVIEW_INPUT_REFERENCE
4. PREVIEW_DECISION_SPACE
5. PREVIEW_CONSTRAINTS
6. PREVIEW_DISCLAIMER

Kršitev zaporedja pomeni:
- neveljaven izpis
- avtomatsko zavrnitev prikaza

---

## 5. PREHODNI STAVKI

Status: STROGO PREPOVEDANI  

HOI ne sme dodati:
- uvodov
- zaključkov
- povezovalnih stavkov
- pojasnil med sekcijami

Med sekcijami je dovoljena **samo prazna vrstica**.

---

## 6. DOVOLJENE FORMULACIJE (STRING-LEVEL ALLOWLIST)

Ta razdelek določa **izključno dovoljene nize (strings)**, ki jih HOI sme uporabiti pri izpisu *Decision Preview*.  
Vsak izpis izven te allowliste pomeni **KRŠITEV v0.34**.

### 6.1. SPLOŠNA PRAVILA

- Dovoljeni so **samo** nizi, navedeni v tem razdelku.
- Nizi so **case-sensitive**.
- Presledki, ločila in vrstni red znakov so **normativni**.
- Združevanje nizov je dovoljeno **samo** v okviru vnaprej določene strukture sekcij.
- Dodajanje ali odstranjevanje znakov je **prepovedano**.

---

### 6.2. ALLOWLIST — FIKSNI NIZI

#### 6.2.1. Naslov izpisa
DECISION PREVIEW


#### 6.2.2. Opis obsega previewja
This output represents a non-executing, non-recommending preview of possible decision paths.


#### 6.2.3. Oznaka sklica na vhod
Input reference:
- Source: <CANONICAL_INPUT_ID>

#### 6.2.4. Oznaka odločitvenega prostora
Decision space:


#### 6.2.5. Oznake poti
- Path A
- Path B
- Path C


#### 6.2.6. Oznaka omejitev
Constraints:


#### 6.2.7. Omejitveni stavki
- No recommendation is provided.
- No prioritization is applied.
- No outcome is predicted.


#### 6.2.8. Disclaimer
This preview does not constitute advice, guidance, or a suggestion. The responsibility for any decision remains entirely with the user.


---

### 6.3. DINAMIČNI VSTAVKI (OMEJENI)

Dovoljen dinamični element:
<CANONICAL_INPUT_ID>


Pravila:
- alfanumeričen identifikator
- brez presledkov
- brez opisnih ali semantičnih namigov

---

### 6.4. ABSOLUTNE PREPOVEDI

- Sinonimi dovoljenih nizov so prepovedani.
- Skrajšave so prepovedane.
- Razlage dovoljenih nizov so prepovedane.
- Kombiniranje dovoljenih nizov v nove stavke je prepovedano.

---

### 6.5. VALIDACIJSKO PRAVILO

Vsak niz v izpisu, ki:
- ni identičen enemu izmed zgoraj navedenih nizov
- ali krši pravila tega dokumenta

pomeni **INVALID DECISION PREVIEW OUTPUT**.

---

## 7. PREPOVEDANE SEKCIJE

Ta razdelek normativno določa **vse sekcije, ki jih HOI NE SME prikazati** v okviru *Decision Preview*.

Prisotnost katerekoli prepovedane sekcije pomeni:
- **INVALID DECISION PREVIEW OUTPUT**
- **avtomatsko zavrnitev prikaza**
- **kršitev v0.34**

---

### 7.1. SPLOŠNO PRAVILO

- Dovoljene so **izključno** sekcije, navedene v razdelku **3. OBVEZNE SEKCIJE**.
- Vsaka sekcija, ki ni eksplicitno dovoljena, je **prepovedana**, ne glede na ime, vsebino ali namen.
- Prepoved velja za:
  - naslove
  - podnaslove
  - opombe
  - zaključke
  - razdelke brez vsebine

---

### 7.2. IZRECNO PREPOVEDANE SEKCIJE (DENYLIST)

HOI ne sme generirati sekcij z naslednjimi imeni ali semantično ekvivalentnimi oznakami:

- Explanation
- Interpretation
- Recommendation
- Suggested action
- Advice
- Guidance
- Notes
- Summary
- Conclusion
- Context
- Background
- Rationale
- Reasoning
- Analysis
- Evaluation
- Impact
- Implications
- Risks
- Benefits
- Pros
- Cons
- Comparison
- Next steps
- What you should do
- Options
- Alternatives
- Outcome
- Prediction
- Forecast
- Confidence
- Likelihood
- Priority
- Importance

---

### 7.3. SEMANTIČNA PREPOVED

Prepoved velja tudi, če:
- je ime sekcije zapisano z drugo velikostjo črk
- je ime sekcije zapisano v množini ali ednini
- je ime sekcije parafrazirano
- je ime sekcije prevedeno v drug jezik
- je sekcija brez naslova, a vsebinsko ustreza prepovedani sekciji

---

### 7.4. STRUKTURNA PREPOVED

HOI ne sme:
- združevati obveznih sekcij v eno sekcijo
- razbijati obveznih sekcij na podsekcije
- vstavljati praznih ali skritih sekcij
- uporabljati vizualnih ločil kot nadomestilo za sekcije

---

### 7.5. VALIDACIJSKO PRAVILO

Če *Decision Preview* vsebuje:
- sekcijo, ki ni navedena v razdelku 3
- ali sekcijo, ki ustreza katerikoli prepovedi iz razdelka 8

se izpis označi kot:
INVALID DECISION PREVIEW OUTPUT


in se **ne prikaže uporabniku**.

---