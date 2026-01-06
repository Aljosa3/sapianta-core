# EXECUTION RESULT

## Status
DESIGN-ONLY — execution ni dovoljen

## Namen
Execution Result definira **edini dovoljeni izhod** execution sloja.

Execution, ki ne vrne strukturiranega Execution Resulta,
se šteje kot **neveljaven**.

Dokument se sklicuje na:
- EXECUTION_CONTEXT
- EXECUTION_BOUNDARY

---

## 1. Temeljno pravilo

Execution Result:
- je vedno strukturiran
- je determinističen
- je popoln (ni delnih, nejasnih izhodov)
- ne vsebuje razlage ali interpretacije

---

## 2. Dovoljeni izidi

Execution Result ima natanko enega od naslednjih statusov:

- SUCCESS
- FAILURE
- PARTIAL
- ABORTED

---

## 3. Obvezni elementi Execution Resulta

Vsak Execution Result MORA vsebovati:

### 3.1 Identiteta
- execution_id
- context_id

### 3.2 Status
- result_status
- completed_at

### 3.3 Sledljivost
- audit_reference
- affected_resources (če obstajajo)

---

## 4. Prepovedani elementi

Execution Result NE SME vsebovati:
- naravnega jezika
- priporočil
- nadaljnjih korakov
- samodejnih sprožilcev

Interpretacija Execution Resulta je odgovornost
**višjih slojev**, nikoli executiona samega.

---

## 5. Razmerje do sistema

- Execution Result zaključi execution
- Ne sproži novega plana
- Ne sproži novega reasoning cikla
- Ne spreminja sistema samodejno

---

Dokument potrjen kot referenca.
Execution Result je definiran.
Execution ostaja NEAKTIVEN.
