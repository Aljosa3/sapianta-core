# HOI_DECISION_PREVIEW_ELIGIBILITY_MATRIX_v0.33_LOCK

Status: LOCKED  
Phase: v0.33  
Layer: HOI (Human Orientation Interface)  
Scope: Decision Preview Eligibility & Rejection  
Supersedes: none  
Depends on:
- HOI Runtime Contract v0.30 (LOCKED)
- HOI Runtime Stub v0.31 (LOCKED)
- HOI ↔ Decision Preview Contract v0.32 (LOCKED)

---

## 1. NAMEN

Ta dokument določa **deterministično matriko upravičenosti** (eligibility)
za sprožitev **Decision Preview** prek HOI.

Dokument:
- ne interpretira namena
- ne vrednoti
- ne primerja
- ne optimizira

HOI v tej fazi **razvršča vhod** in **izvede ali zavrne** preview
izključno na podlagi te matrike.

---

## 2. NEPREKLICNA NAČELA

- HOI ne sklepa o pomenu
- HOI ne rekonstruira namena
- HOI ne predlaga reformulacij
- HOI ne nadaljuje toka po zavrnitvi

Vsak vhod se obravnava **izolirano**.

---

## 3. IZHODNE AKCIJE (ENUM)

HOI lahko izvede **samo eno** izmed naslednjih akcij:

- `ALLOW_PREVIEW`
- `REJECT`
- `HARD_BLOCK`

Druge akcije niso dovoljene.

---

## 4. RAZREDI VHODOV (INPUT CLASSES)

Vhodi se razvrstijo v **izključujoče** razrede.
Vsak vhod pripada **natanko enemu** razredu.

### IC-1: EXPLICIT_SINGLE_DECISION
Opis:
- ena jasno opredeljena odločitev
- brez primerjave
- brez vrednotenja
- brez vprašanja pravilnosti

Primerna oblika:
- pogojna, hipotetična
- “če X, kaj se zgodi”

---

### IC-2: COMPARATIVE_DECISIONS
Opis:
- več kot ena odločitev
- implicitna ali eksplicitna primerjava
- “X ali Y”, “primerjaj”, “katera”

---

### IC-3: RECOMMENDATION_SEEKING
Opis:
- zahteva po priporočilu
- zahteva po “najboljši” izbiri
- zahteva po presoji pravilnosti

---

### IC-4: OPTIMIZATION_REQUEST
Opis:
- zahteva po izboljšavi
- zahteva po minimizaciji/maksimizaciji
- zahteva po rangiranju

---

### IC-5: RISK_EVALUATION_NORMATIVE
Opis:
- vrednostna presoja tveganja
- “ali je varno”, “ali je pametno”
- normativni jezik

---

### IC-6: AMBIGUOUS_OR_INCOMPLETE
Opis:
- nejasno opredeljena odločitev
- manjkajoč ali nedoločljiv X
- nedoločljiva hipoteza

---

### IC-7: META_SYSTEM_REQUEST
Opis:
- vprašanja o sistemu
- vprašanja o pravilih
- vprašanja o mejah HOI

---

## 5. ELIGIBILITY MATRIX

| Input Class | Action         |
|------------|----------------|
| IC-1       | ALLOW_PREVIEW  |
| IC-2       | REJECT         |
| IC-3       | HARD_BLOCK     |
| IC-4       | HARD_BLOCK     |
| IC-5       | REJECT         |
| IC-6       | REJECT         |
| IC-7       | REJECT         |

Ta tabela je **izčrpna**.

---

## 6. OBVEZNO OBNAŠANJE HOI PO AKCIJI

### 6.1 ALLOW_PREVIEW
HOI:
- posreduje zahtevo v Decision Preview
- prikaže rezultat brez interpretacije
- priloži obvezni disclaimer (v0.32)

HOI NE SME:
- dodajati komentarjev
- predlagati nadaljevanja
- sprožiti dodatnih previewjev

---

### 6.2 REJECT
HOI:
- vrne **minimalno nevtralno zavrnitev**
- brez pojasnjevanja
- brez reformulacije

Dovoljen format (neparafrazljiv):
> “Zahteva ni primerna za Decision Preview v tej fazi.”

---

### 6.3 HARD_BLOCK
HOI:
- vrne **blokirni odziv**
- brez alternative
- brez poziva k ponovnemu poskusu

Dovoljen format (neparafrazljiv):
> “HOI ne more obravnavati te zahteve.”

---

## 7. PREPOVEDANI PREHODI

Izrecno prepovedano:

- REJECT → avtomatska reformulacija
- REJECT → predlaganje primerne oblike
- HARD_BLOCK → pojasnjevanje razloga
- katerikoli → implicitna primerjava
- katerikoli → nadaljevanje toka brez nove zahteve

---

## 8. STANJE PO OBRAVNAVI

Po vsaki obravnavi:

- ni aktivnega stanja
- ni shranjenega konteksta
- ni “čakajoče” odločitve

Sistem se vrne v **nevtralno HOI stanje**.

---

## 9. PREPOVED AGENTNOSTI

Ta matrika je **zadnja vhodna varovalka**.

Kršitve vključujejo:
- semantično interpretacijo
- pomoč pri formulaciji
- implicitno svetovanje

Vsaka kršitev je **architectural breach**.

---

## 10. LOCK DOLOČILO

Ta dokument je zaklenjen (LOCKED).

- brez razširitev
- brez reinterpretacij
- brez UX izjem

Spremembe so možne samo z novo fazo in novim LOCK dokumentom.

---

END OF DOCUMENT
