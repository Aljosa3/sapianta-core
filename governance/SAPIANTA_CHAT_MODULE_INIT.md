# SAPIANTA_CHAT_MODULE_INIT

Status: INIT  
Odvisnost:
- INTENT_LAYER_INIT = LOCKED
- MODULE_CONTRACT_INIT = LOCKED
- RISK_ASSESSMENT_REVIEW = LOCKED
- CANON_GUARD_DECISION_CHAIN = ACTIVE

Razred: Module / Interaction  
Narava: Vhodna (ne-odločitvena)

---

## 1. NAMEN

Vzpostaviti **SAPIANTA Chat Modul** kot edini dovoljen
interakcijski vmesnik med uporabnikom in sistemom.

Chat Modul:
- zbira uporabniške vnose
- strukturira INTENT
- sproži sistemski tok

Ne interpretira in ne odloča.

---

## 2. DOVOLJENO OBNAŠANJE

Chat Modul sme:

- sprejeti surovi uporabniški vnos
- ustvariti deklarativni INTENT
- predati INTENT v sistemski tok
- prikazati Explain izhod (če obstaja)

---

## 3. PREPOVEDANO OBNAŠANJE

Chat Modul izrecno NE SME:

- presojati pomena uporabnikovega namena
- odločati ali potrjevati dejanja
- izvajati ukazov
- preverjati jurisdikcije
- nadomeščati Decision Authority
- pisati v Audit

---

## 4. ODNOS DO INTENT LAYERJA

Chat Modul:
- je primarni vir uporabniškega INTENTA
- ne interpretira namena
- ne obogati namena z logiko

Vsak INTENT mora biti sledljiv nazaj do uporabniškega vnosa.

---

## 5. ODNOS DO OSTALIH SLOJEV

- Evaluation: Chat ne evaluira
- Decision Gate: Chat nima vpliva
- Authority: Chat ni authority
- Execution: Chat nima dostopa

Chat je **vhod**, ne del jedra.

---

## 6. INVARIANTA

> Če Chat Modul povzroči odločitev ali izvršitev,
> ni več interakcijski modul, temveč prikrita oblast.

---

## 7. ZAKLEP FAZE

Faza `SAPIANTA_CHAT_MODULE_INIT` se lahko označi kot **LOCKED**, ko velja:

- Chat generira samo INTENT
- Chat ne vsebuje odločilne logike
- Chat je zamenljiv brez vpliva na sistem

---

Konec dokumenta.
