PATH: governance/policies/HOI_DECISION_PREVIEW_VALIDATOR_ENFORCEMENT_v0.35_LOCK.md

# HOI_DECISION_PREVIEW_VALIDATOR_ENFORCEMENT_v0.35_LOCK

Status: LOCK-READY
Layer: HOI → Decision Preview
Mode: READ-ONLY
Paraphrase: DISALLOWED
Interpretation: DISALLOWED

---

## 1. NAMEN DOKUMENTA

Ta dokument normativno določa **obvezno uveljavitev (enforcement)** pravil, definiranih v:

- HOI_DECISION_PREVIEW_PRESENTATION_SCHEMA_v0.34_LOCK

Dokument:

- uvaja obvezni validator kot **zadnjo izvršilno mejo pred prikazom**
- določa posledice PASS in FAIL stanj
- onemogoča prikaz neveljavnega Decision Preview
- preprečuje diskrecijo HOI pri prikazu izpisa

Dokument ne:

- razlaga validacijskih pravil
- opisuje semantiko odločitev
- uvaja nove vsebinske omejitve
- opisuje UX ali obnašanje uporabnika

---

## 2. OBVEZNOST VALIDATORJA

2.1. Vsak Decision Preview **MORA** biti validiran.

2.2. Validacija **MORA** biti izvedena:
- pred vsakim prikazom izpisa
- ne glede na vstopno točko (CLI, API, GUI)
- ne glede na izvor zahteve

2.3. Decision Preview brez uspešne validacije je **NEVELJAVEN**.

---

## 3. POZICIJA VALIDATORJA V TOKU HOI

3.1. Validator je umeščen:

- po generaciji Decision Preview
- pred katerokoli obliko prikaza ali posredovanja

3.2. HOI **NE SME**:
- prikazati izpisa pred validacijo
- delno prikazati izpisa pred validacijo
- preoblikovati izpisa po validaciji

3.3. Validator predstavlja **zadnjo točko odločitve o prikazu**.

---

## 4. IZID VALIDACIJE — PASS

4.1. Če validator vrne **PASS**:

- Decision Preview je označen kot **VALID**
- izpis se lahko prikaže uporabniku
- izpis se prikaže **nespremenjen**

4.2. HOI ne sme:
- dodati dodatnih besed
- dodati oznak o uspešni validaciji
- spremeniti vrstnega reda ali oblike izpisa

---

## 5. IZID VALIDACIJE — FAIL

5.1. Če validator vrne **FAIL**:

- Decision Preview je označen kot **INVALID**
- izpis se **NE SME prikazati**

5.2. Ob FAIL stanju:

- ni fallback izpisa
- ni nadomestnega besedila
- ni obvestila uporabniku o razlogu
- ni povzetka napake

5.3. Rezultat FAIL pomeni **NO-OUTPUT**.

---

## 6. PREPOVED BYPASSA

6.1. HOI **NE SME**:

- obiti validator
- ponoviti generacijo z namenom izogiba validaciji
- spremeniti izpis po FAIL rezultatu
- prikazati del izpisa, ki je prestal delno validacijo

6.2. Vsak poskus bypassa pomeni:

- kršitev v0.35
- neveljavno delovanje HOI

---

## 7. RAZMERJE HOI ↔ VALIDATOR

7.1. Validator ima **absolutno prednost** pred HOI glede odločitve o prikazu.

7.2. HOI:

- ne interpretira validacijskega rezultata
- ne spreminja posledic PASS ali FAIL
- ne prevzema odgovornosti za vsebino izpisa

7.3. HOI deluje kot **posrednik**, ne kot odločevalec.

---

## 8. AUDIT SIGNAL (MINIMALNI)

8.1. Ob vsakem FAIL stanju se ustvari **minimalni audit signal**.

8.2. Audit signal:

- ne vsebuje vsebine Decision Preview
- ne vsebuje razloga za FAIL
- ne vsebuje interpretacije

8.3. Audit signal označuje izključno:
- da je bil izpis zavrnjen zaradi neuspešne validacije

---

## 9. STATUS IZPISA

9.1. Decision Preview ima lahko le dva statusa:

- VALID
- INVALID

9.2. Status INVALID je **terminalen**.

9.3. INVALID izpis:
- se ne prikaže
- se ne transformira
- se ne posreduje naprej

---

## 10. KONČNA DOLOČBA

10.1. Decision Preview, ki ni v celoti skladen z v0.34 in uveljavljen skozi v0.35, **ne obstaja za uporabnika**.

10.2. Prikaz brez uspešne validacije pomeni:
- kršitev v0.35
- neveljavno delovanje sistema

---
