# EXECUTION BOUNDARY DOCUMENT

## Status
DESIGN-ONLY — brez executiona

## Namen dokumenta
Ta dokument definira **stroge meje dovoljenega delovanja** za prihodnjo Execution Ero
v sistemu SAPIANTA.

Dokument določa:
- kaj execution NAČELNO SME delati
- kaj execution IZRECNO NE SME delati
- katera področja so rezervirana za prihodnje faze

Dokument se sklicuje na:
- LOCK_PRE_EXECUTION_ERA
- EXECUTION_ERA_ENTRY_CRITERIA

---

## 1. Temeljno pravilo

Execution:
- je **podrejeni sloj**
- nikoli ne deluje samostojno
- nikoli ne interpretira namena
- nikoli ne odloča o pravilnosti

Execution **izvaja izključno eksplicitno dovoljene akcije**
na podlagi **strukturiranih, potrjenih objektov**.

---

## 2. DOVOLJENO (NAČELNO)

Execution sme (v prihodnjih fazah):

- izvajati **deterministične, jasno opisane akcije**
- delovati zgolj na podlagi:
  - potrjenega plana
  - potrjenega execution konteksta
- zapisovati **audit log** pred in po akciji
- vračati strukturiran **Execution Result**
- delovati v omejenem, vnaprej določenem obsegu

Primeri (neimplementirani):
- zapis v lokalno datoteko
- klic izoliranega notranjega modula
- branje vnaprej dovoljenega vira

---

## 3. POGOJNO DOVOLJENO (FUTURE SCOPE)

Dovoljeno **šele v prihodnjih fazah**, ob dodatnih pogojih:

- komunikacija z zunanjimi sistemi
- spreminjanje sistemskega stanja
- avtomatizacija ponavljajočih se opravil
- delovanje brez human-in-the-loop

Vsak od teh primerov zahteva:
- lasten governance dokument
- lasten lock
- eksplicitno fazno potrditev

---

## 4. IZRECNO PREPOVEDANO

Execution NIKOLI ne sme:

- interpretirati naravnega jezika
- generirati ali spreminjati plan
- obiti Chat / Reasoning / Planning sloj
- spreminjati obstoječe faze (17–19)
- spreminjati governance dokumente
- delovati brez audit zapisa
- eskalirati privilegije
- samodejno širiti lastnih zmožnosti

---

## 5. Varnostna drža (Security Posture)

Execution je:
- fail-closed (nejasno → ne izvrši)
- minimalen (najmanjši možni obseg)
- reverzibilen (kjer je mogoče)
- sledljiv (vsaka akcija je zabeležena)

---

## 6. Razmerje do drugih slojev

- Chat: NI odgovoren za execution
- Reasoning: NI odgovoren za execution
- Planning: NI odgovoren za execution
- Governance: IMA absolutno avtoriteto

Execution je **tehnični izvajalec**, ne odločevalec.

---

## 7. Spremembe dokumenta

Ta dokument se lahko spremeni samo:
- z novo FAZO
- z novim governance lockom
- z novim tagom

Spremembe za nazaj niso dovoljene.

---

Dokument potrjen kot referenca.
Execution Boundary je definiran.
Execution ostaja NEAKTIVEN.
