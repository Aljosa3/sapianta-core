PATH: governance/policies/HOI_DECISION_PREVIEW_VALIDATOR_REFERENCE_v0.39_LOCK.md

# HOI_DECISION_PREVIEW_VALIDATOR_REFERENCE_v0.39_LOCK

Status: LOCK-READY  
Layer: Decision Preview → Validator  
Mode: READ-ONLY  
Normativity: NON-NORMATIVE  
Runtime Binding: NONE  

---

## 1. NAMEN DOKUMENTA

Ta dokument določa **referenčno (nezavezujočo) validacijsko specifikacijo** za preverjanje izpisa *Decision Preview*.

Dokument:

- zagotavlja enoten referenčni model validacije
- omogoča testiranje, CI in regresijsko preverjanje
- preslika normativna pravila v0.34–v0.37 v preverljive korake
- služi kot **primer pravilne implementacije**

Dokument **NE**:

- spreminja ali dopolnjuje normativna pravila
- uvaja nove runtime zahteve
- nadomešča obvezni validator v0.35
- ustvarja zavezujoče obnašanje sistema

---

## 2. STATUS REFERENČNE IMPLEMENTACIJE

2.1. Ta validator je:
- referenčen
- test-only
- nezavezujoč

2.2. Runtime implementacije:
- **NE SMEJO** biti odvisne od te reference
- **MORAJO** slediti izključno normativnim dokumentom

2.3. Neskladje med referenco in runtime validatorjem:
- **NE** predstavlja kršitve
- dokler runtime validator sledi v0.35–v0.38

---

## 3. VHODNI IN IZHODNI MODEL

### 3.1. Vhod

- celoten *Decision Preview output*
- kot en sam neprekinjen tekstovni niz
- brez metapodatkov
- brez konteksta

### 3.2. Izhod

Ena od vrednosti:
- PASS
- FAIL

Brez dodatnih informacij.

---

## 4. PRESLIKAVA NA NORMATIVNA PRAVILA

Referenčni validator **MORA** preverjati pravila v naslednjem zaporedju:

1. Struktura sekcij (v0.34 §3, §4)
2. Prepovedane sekcije (v0.34 §7)
3. String-level allowlist (v0.34 §6)
4. String-level denylist (v0.34 §8)
5. Dinamični vstavek `<CANONICAL_INPUT_ID>` (v0.34 §6.3)
6. Prazne vrstice in ločila (v0.34 §9.7)
7. Končna binarna odločitev

Če katerikoli korak vrne FAIL → **končni rezultat = FAIL**.

---

## 5. REFERENČNI VALIDACIJSKI KORAKI

### 5.1. VALIDACIJA STRUKTURE

- preveri točno 6 sekcij
- preveri vrstni red
- preveri odsotnost dodatnih blokov

FAIL, če katerikoli pogoj ni izpolnjen.

---

### 5.2. VALIDACIJA NIZOV

- vsak niz mora biti bit-for-bit enak allowlisti
- noben niz ne sme ustrezati denylisti
- preverjanje je case-sensitive (allowlist)
- denylist se preverja case-insensitive

FAIL ob prvem odstopanju.

---

### 5.3. VALIDACIJA DINAMIČNEGA VSTAVKA

- dovoljen je samo `<CANONICAL_INPUT_ID>`
- pojavi se lahko samo enkrat
- ne sme vsebovati presledkov ali semantike

FAIL ob kršitvi.

---

### 5.4. VALIDACIJA PRAZNIH VRSTIC

- ena prazna vrstica med sekcijami
- brez praznih vrstic na začetku ali koncu
- brez simbolnih ločil

FAIL ob kršitvi.

---

## 6. TESTNI PRIMERI (NEZAVEZUJOČI)

### 6.1. VALID primer

- izpis, ki je 100 % skladen z v0.34
- rezultat: PASS

### 6.2. INVALID primeri

- manjkajoča sekcija
- dodatna beseda
- uporaba besede iz denylist
- sprememba ločila
- dodatna prazna vrstica

Rezultat v vseh primerih: FAIL

---

## 7. OMEJITVE REFERENCE

- Referenca **NE SME**:
  - vračati razlage
  - vračati delne rezultate
  - popravljati izpisa
  - izvajati retry logike

- Referenca **NE SME**:
  - vplivati na runtime tok
  - biti uporabljena za UX odločitve

---

## 8. RAZMERJE DO AUDITA

- Referenčni validator:
  - ne generira audit eventov
  - ne sodeluje v v0.38 toku
- Audit semantika ostaja izključno normativna

---

## 9. KONČNA DOLOČBA

Ta dokument:

- obstaja izključno kot pomoč za implementatorje
- nima normativne ali pravne teže
- ne spreminja LOCK statusa nobene faze

V primeru konflikta velja:
**v0.34–v0.38 > v0.39**

---
