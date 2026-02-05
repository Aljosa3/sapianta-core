PATH: governance/audit/HOI_DECISION_PREVIEW_AUDIT_INDEX_v0.39_LOCK.md

# HOI_DECISION_PREVIEW_AUDIT_INDEX_v0.39_LOCK

Status: LOCK-READY  
Scope: Decision Preview lifecycle  
Coverage: v0.34 → v0.39  
Mode: READ-ONLY  
Paraphrase: DISALLOWED  
Interpretation: DISALLOWED  

---

## 1. NAMEN DOKUMENTA

Ta dokument predstavlja **enoten audit index** za celoten *Decision Preview* tok.

Namen dokumenta je:

- potrditi **neprekinjeno normativno verigo**
- zagotoviti **sledljivost LOCK dokumentov**
- omogočiti **hitri sanity-check skladnosti**
- služiti kot vstopna točka za audit, CI in review

Dokument **NE**:

- uvaja novih pravil
- spreminja obstoječih LOCK dokumentov
- nadomešča katerikoli normativni vir

---

## 2. PREGLED VERIGE (CANONICAL CHAIN)

Decision Preview lifecycle je definiran z naslednjimi **LOCK dokumenti**:

| Verzija | Dokument | Namen |
|-------:|----------|-------|
| v0.34 | HOI_DECISION_PREVIEW_PRESENTATION_SCHEMA | Struktura in string-level pravila |
| v0.35 | HOI_DECISION_PREVIEW_VALIDATOR_ENFORCEMENT | Obvezen validator |
| v0.36 | HOI_DECISION_PREVIEW_RUNTIME_INTEGRATION | Runtime tok |
| v0.37 | HOI_DECISION_PREVIEW_FAILURE_AUDIT_SEMANTICS | FAIL propagacija |
| v0.38 | HOI_DECISION_PREVIEW_AUDIT_EVENT_SCHEMA | Audit dogodki |
| v0.39 | HOI_DECISION_PREVIEW_VALIDATOR_REFERENCE | Nezavezujoča referenca |

---

## 3. ODVISNOSTI IN TOK

Normativni tok **MORA** slediti tej verigi:

```
v0.34 → v0.35 → v0.36 → v0.37 → v0.38
↘
v0.39 (reference only)
```

Pravila:

- v0.39 **NE** vpliva na runtime
- v0.38 je končna normativna točka za audit
- brez v0.34 ni veljavnega izpisa
- brez v0.35 ni veljavnega prikaza

---

## 4. SANITY-CHECK MATRICA

### 4.1. STRUKTURNA SKLADNOST

| Kontrola | Vir | Status |
|---------|-----|--------|
| Fiksno število sekcij | v0.34 | REQUIRED |
| Zaporedje sekcij | v0.34 | REQUIRED |
| Brez dodatnih blokov | v0.34 | REQUIRED |

---

### 4.2. VALIDACIJSKA SKLADNOST

| Kontrola | Vir | Status |
|---------|-----|--------|
| Obvezen validator | v0.35 | REQUIRED |
| PASS / FAIL binarnost | v0.35 | REQUIRED |
| Brez retry / fallback | v0.35 | REQUIRED |

---

### 4.3. RUNTIME SKLADNOST

| Kontrola | Vir | Status |
|---------|-----|--------|
| Validator pred prikazom | v0.36 | REQUIRED |
| Enoten tok CLI/API/GUI | v0.36 | REQUIRED |
| NO-OUTPUT ob FAIL | v0.36 | REQUIRED |

---

### 4.4. FAILURE SEMANTIKA

| Kontrola | Vir | Status |
|---------|-----|--------|
| FAIL ≠ runtime error | v0.37 | REQUIRED |
| FAIL brez razlage | v0.37 | REQUIRED |
| FAIL brez izpisa | v0.37 | REQUIRED |

---

### 4.5. AUDIT SKLADNOST

| Kontrola | Vir | Status |
|---------|-----|--------|
| Read-only audit zapis | v0.38 | REQUIRED |
| PASS / FAIL event | v0.38 | REQUIRED |
| Brez vsebine previewja | v0.38 | REQUIRED |

---

### 4.6. REFERENČNA SKLADNOST

| Kontrola | Vir | Status |
|---------|-----|--------|
| Reference ni runtime binding | v0.39 | REQUIRED |
| Reference ne vpliva na audit | v0.39 | REQUIRED |

---

## 5. HITRI LOCK SANITY-CHECK

Decision Preview sistem je **LOCK-VALID**, če:

- vsi dokumenti v0.34–v0.38 obstajajo
- noben LOCK dokument ni bil spremenjen
- runtime sledi v0.36
- audit sledi v0.38
- v0.39 se uporablja izključno kot referenca

Če katerikoli pogoj ni izpolnjen → **CHAIN INVALID**.

---

## 6. UPORABA V PRAKSI

Ta dokument se uporablja:

- kot **audit entry point**
- kot **CI checklist**
- kot **review povzetek**
- kot dokaz skladnosti pri zunanjem pregledu

---

## 7. KONČNA DOLOČBA

Ta audit index:

- ne uvaja novih obveznosti
- ne spreminja obnašanja sistema
- obstaja izključno za sledljivost in preglednost

V primeru konflikta velja:
**primarni LOCK dokument > audit index**

---
