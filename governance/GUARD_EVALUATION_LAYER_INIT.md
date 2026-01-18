# GUARD_EVALUATION_LAYER_INIT

Status: INIT  
Odvisnost: GUARD_CONTEXT_SURFACE_INIT = LOCKED  
Razred: Runtime / Governance  
Narava: Evaluacijska (ne-izvršilna)

---

## 1. NAMEN

Vzpostaviti **evalvacijski sloj Guarda**, ki sme:
- izvajati presojo nad že vidnim kontekstom
- vendar **ne sme sprejemati odločitev**
- in **ne sme vplivati na runtime**

Ta faza uvede **razlikovanje med zaznavo in presojo**.

---

## 2. NAČELO

> Guard v tej fazi sme **ocenjevati**, ne sme pa **odločati**.

Vsaka evaluacija je:
- neizvršilna
- ne-zavezujoča
- brez stranskih učinkov

---

## 3. VHODI V EVALUACIJSKI SLOJ

Guard v fazi `GUARD_EVALUATION_LAYER_INIT` prejme izključno:

- kontekstno površino iz `GUARD_CONTEXT_SURFACE_INIT`
- statično referenco na aktivne policy ID-je (brez vsebine)
- statično referenco na jurisdikcijske oznake

❌ brez dostopa do policy pravil  
❌ brez dostopa do hierarhije  
❌ brez dostopa do resolucij konfliktov  

---

## 4. DOVOLJENE EVALUACIJE

Guard SME izvajati izključno naslednje tipe presoj:

### 4.1 Skladnost konteksta
- ali vhodni kontekst *potencialno* spada v nadzorovani razred
- ali obstaja potreba po nadaljnji normativni obravnavi

### 4.2 Detekcija tveganja (neodločitvena)
- zaznava prisotnosti rizičnih označevalcev
- zaznava mejnih pogojev

⚠️ zaznava ≠ ukrep  
⚠️ zaznava ≠ blokada  

---

## 5. IZRECNO PREPOVEDANE AKCIJE

V tej fazi Guard NE SME:

- dovoliti dejanja
- zavrniti dejanja
- blokirati izvajanja
- eskalirati v izvršilni sloj
- aktivirati policy
- sprožiti audit

Vsak poskus pomeni **kršitev evalvacijske izolacije**.

---

## 6. IZHOD EVALUACIJSKEGA SLOJA

Edini dovoljen izhod je:

- **Evalvacijski signal**, ki vsebuje:
  - tip zaznave (npr. none / potential / elevated)
  - identifikator konteksta
  - časovni žig

Evalvacijski signal:
- nima izvršilne moči
- nima normativne teže
- ne vpliva na runtime

---

## 7. INVARIANTA

> Če evalvacija spremeni potek izvajanja, to ni več evalvacija.

Ta ločnica je absolutna.

---

## 8. ZAKLEP FAZE

Faza `GUARD_EVALUATION_LAYER_INIT` se lahko označi kot **LOCKED**, ko velja:

- evalvacija je ločena od odločanja
- evalvacija nima stranskih učinkov
- izhod je zgolj signal, ne ukaz

Dovoljen nadaljnji prehod:
- `GUARD_DECISION_GATE_INIT` (če in samo če obstaja)

---

Konec dokumenta.
