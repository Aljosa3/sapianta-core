PATH: governance/policies/HOI_DECISION_PREVIEW_AUDIT_EVENT_SCHEMA_v0.38_LOCK.md

# HOI_DECISION_PREVIEW_AUDIT_EVENT_SCHEMA_v0.38_LOCK

Status: LOCK-READY  
Layer: HOI → Decision Preview  
Mode: READ-ONLY  
Paraphrase: DISALLOWED  
Interpretation: DISALLOWED  

---

## 1. NAMEN DOKUMENTA

Ta dokument normativno določa **kanonično strukturo audit dogodkov**, povezanih z *Decision Preview*.

Dokument:
- definira dovoljene tipe audit dogodkov
- določa obvezna in prepovedana polja
- zagotavlja sledljivost FAIL/PASS brez UX izpostavitve
- omogoča forenzično revizijo brez semantičnega uhajanja

Dokument ne:
- uvaja runtime obnašanja
- sproža ponovne poskuse
- opisuje logiko validatorja
- vpliva na prikaz uporabniku

---

## 2. SPLOŠNA NAČELA AUDITA

2.1. Audit je **pasiven** (no side-effects).  
2.2. Audit je **read-only**.  
2.3. Audit je **determinističen**.  
2.4. Audit **nikoli** ne vpliva na runtime tok.

Audit ≠ retry  
Audit ≠ fallback  
Audit ≠ obvestilo  

---

## 3. DOVOLJENI AUDIT DOGODKI (EVENT TYPE ALLOWLIST)

HOI **SME** generirati izključno naslednje audit dogodke:

- PREVIEW_VALIDATION_PASS
- PREVIEW_VALIDATION_FAIL
- PREVIEW_RUNTIME_ERROR (brez preview prikaza)

Vsak drug event type je **PREPOVEDAN**.

---

## 4. STRUKTURA AUDIT DOGODKA (KANONIČNA)

Vsak audit dogodek **MORA** vsebovati točno naslednja polja:

- event_type
- event_timestamp
- preview_id
- canonical_input_id
- preview_hash
- validator_version
- schema_versions
- interface_origin

---

## 5. OBVEZNA POLJA (FIELD REQUIREMENTS)

### 5.1. event_type
- vrednost iz razdelka 3
- string (case-sensitive)

### 5.2. event_timestamp
- ISO-8601 UTC
- brez lokalnega časa

### 5.3. preview_id
- enoličen identifikator preview generacije
- brez semantike

### 5.4. canonical_input_id
- identičen `<CANONICAL_INPUT_ID>` iz previewja

### 5.5. preview_hash
- kriptografski hash celotnega izpisa
- hash se izračuna **pred** validacijo

### 5.6. validator_version
- npr. `v0.35`

### 5.7. schema_versions
MORA vsebovati:
- presentation_schema: v0.34
- validator_schema: v0.35
- runtime_integration: v0.36
- failure_semantics: v0.37

### 5.8. interface_origin
- CLI | API | GUI

---

## 6. PREPOVEDANA POLJA (ABSOLUTNA DENYLIST)

Audit dogodek **NE SME** vsebovati:

- razlogov FAIL
- opisov napak
- priporočil
- interpretacij
- UX besedila
- naravnega jezika (razen event_type)

Primeri prepovedanih polj:
- message
- explanation
- reason
- suggestion
- user_text
- display_hint

---

## 7. AUDIT OBNAŠANJE OB PASS

- zapiše se dogodek `PREVIEW_VALIDATION_PASS`
- preview se lahko prikaže uporabniku
- audit zapis **ne vpliva** na prikaz

---

## 8. AUDIT OBNAŠANJE OB FAIL

- zapiše se dogodek `PREVIEW_VALIDATION_FAIL`
- preview se **NE prikaže**
- audit zapis ostane interni

---

## 9. RAZMERJE AUDIT ↔ RUNTIME

- Audit se izvede **po** validaciji
- Audit se izvede **pred ali po** odločitvi o prikazu
- Audit nikoli ne spremeni izida

---

## 10. VALIDACIJSKO PRAVILO

Audit dogodek je **VALID**, če in samo če:
- vsebuje vsa obvezna polja iz razdelka 4
- ne vsebuje nobenega prepovedanega polja
- uporablja dovoljen event_type

V nasprotnem primeru:
- audit dogodek se **NE SME zapisati**
- runtime tok se **NE SME spremeniti**

---

## 11. KONČNA DOLOČBA

Decision Preview brez audit dogodka, skladnega z v0.38:
- je forenzično nepopoln
- ne krši UX pravil
- **NI** skladen z industrijskim audit standardom HOI

---
