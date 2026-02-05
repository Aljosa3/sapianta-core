PATH: governance/policies/HOI_DECISION_PREVIEW_RUNTIME_INTEGRATION_v0.36_LOCK.md

# HOI_DECISION_PREVIEW_RUNTIME_INTEGRATION_v0.36_LOCK

Status: LOCK-READY
Layer: HOI → Decision Preview
Mode: READ-ONLY
Paraphrase: DISALLOWED
Interpretation: DISALLOWED

---

## 1. NAMEN DOKUMENTA

Ta dokument normativno določa **runtime integracijo validatorja**, definiranega v:

- HOI_DECISION_PREVIEW_VALIDATOR_ENFORCEMENT_v0.35_LOCK

Dokument:

- razširi HOI Runtime Contract (v0.30)
- določi obvezno mesto validatorja v runtime toku
- onemogoči alternativne ali obhodne tokove
- uveljavi enotno obnašanje za CLI, API in GUI

Dokument ne:

- opisuje implementacije
- uvaja nove semantične omejitve
- razlaga razlogov za validacijo
- opisuje UX ali obnašanje uporabnika

---

## 2. OBVEZNOST RUNTIME INTEGRACIJE

2.1. HOI **MORA** integrirati validator kot obvezno runtime fazo.

2.2. Integracija **MORA** biti:
- deterministična
- sinhrona
- enaka za vse vmesnike

2.3. Runtime tok brez validatorja je **NEVELJAVEN**.

---

## 3. RUNTIME ZAPOREDJE (OBVEZNO)

3.1. HOI runtime tok **MORA** slediti točnemu zaporedju:

1. Vhod zahteve (HOI entry)
2. Ugotavljanje upravičenosti previewja (v0.33)
3. Generacija Decision Preview (read-only)
4. **Validator execution (v0.35)**
5. Odločitev o prikazu
6. Prikaz izpisa (če VALID)

3.2. Noben korak **NE SME** biti:
- izpuščen
- zamenjan
- ponovljen z namenom obhoda

---

## 4. MESTO VALIDATORJA

4.1. Validator **MORA** biti izveden:
- po popolni generaciji izpisa
- pred kakršnimkoli prikazom ali posredovanjem

4.2. Validator **NE SME** biti:
- premaknjen pred generacijo
- premaknjen po prikazu
- izveden delno

4.3. Rezultat validatorja je **zavezujoč**.

---

## 5. RUNTIME OBNAŠANJE OB PASS

5.1. Ob rezultatu **PASS**:

- runtime tok se nadaljuje
- izpis se prikaže uporabniku
- izpis ostane nespremenjen

5.2. HOI **NE SME**:
- dodati runtime oznak
- dodati validacijskih indikatorjev
- spremeniti format ali vsebino

---

## 6. RUNTIME OBNAŠANJE OB FAIL

6.1. Ob rezultatu **FAIL**:

- runtime tok se **TAKOJ prekine**
- izpis se **NE prikaže**

6.2. Ob FAIL stanju:

- ni nadomestnega toka
- ni ponovne generacije
- ni obvestila uporabniku
- ni razlage napake

6.3. FAIL v runtime pomeni **NO-OUTPUT**.

---

## 7. ENOTNOST MED VMESNIKI

7.1. CLI, API in GUI **MORAJO** uporabljati:
- isti runtime tok
- isti validator
- iste posledice PASS / FAIL

7.2. Različni runtime tokovi za različne vmesnike so **PREPOVEDANI**.

---

## 8. PREPOVED RUNTIME BYPASSA

8.1. HOI **NE SME**:

- preskočiti validatorja glede na kontekst
- spremeniti zaporedje zaradi zmogljivosti
- uporabiti asinhrone poti za prikaz
- prikazati delni izpis

8.2. Vsak runtime bypass pomeni:
- kršitev v0.36
- neveljavno delovanje sistema

---

## 9. RAZMERJE RUNTIME NAPAK ↔ VALIDACIJA

9.1. Runtime napaka **NI** validacijski FAIL.

9.2. Validacijski FAIL **NI** runtime napaka.

9.3. Runtime napake:
- se obravnavajo izven področja Decision Preview
- ne smejo sprožiti prikaza previewja

---

## 10. KONČNA DOLOČBA

10.1. Decision Preview, ki ni:
- generiran skladno z v0.33
- validiran skladno z v0.34
- uveljavljen skladno z v0.35
- integriran skladno z v0.36

**NE OBSTAJA** v runtime kontekstu.

10.2. Vsak prikaz brez popolne skladnosti pomeni:
- kršitev v0.36
- neveljavno delovanje HOI

---
