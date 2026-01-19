# INTENT_LAYER_INIT

Status: INIT  
Odvisnost:
- RUNTIME_GUARD_INIT = LOCKED
- CANON_GUARD_DECISION_CHAIN = ACTIVE

Razred: Interaction / Governance  
Narava: Deklarativna (ne-interpretativna)

---

## 1. NAMEN

Vzpostaviti **INTENT LAYER** kot formalni sloj za
deklaracijo namena uporabnika ali modula,
ki obstaja **pred kontekstom, evalvacijo in odločanjem**.

INTENT LAYER:
- ne sklepa
- ne interpretira
- ne presoja
- ne odloča

Njegova edina vloga je: **zapis namena**.

---

## 2. TEMELJNO NAČELO

> Intent opisuje **kaj je bilo zahtevano**,  
> ne pa **kaj pomeni**, **ali je dovoljeno** ali **kaj se bo zgodilo**.

Vsak poskus interpretacije pomeni kršitev tega sloja.

---

## 3. KAJ JE INTENT

Intent je strukturirana izjava, ki vsebuje izključno:

- **tip namena** (npr. inquire, request, execute, recommend)
- **ciljni objekt** (abstraktno, brez semantike)
- **vir** (user / module / system)
- **obseg** (informativni / zahtevan / potrditveni)
- **časovni žig**

Intent:
- ni ukaz
- ni zahteva za izvršitev
- ni pravna podlaga

---

## 4. KAJ INTENT NI

INTENT LAYER izrecno NE SME:

- razlagati uporabniškega besedila
- ugotavljati resničnega namena
- presojati zakonitosti
- odločati o nadaljnjih korakih
- popravljati ali “izboljševati” zahteve

Če je potreben pomen → to ni Intent, to je Explain.

---

## 5. DOVOLJENI VIRI INTENTA

INTENT je lahko ustvarjen izključno iz:

- uporabniškega vmesnika (npr. SAPIANTA Chat)
- modula (znotraj Module Contracta)
- sistemskega sprožilca (npr. scheduled task)

Vsak intent mora imeti jasno določen **vir**.
Brez vira → intent ni veljaven.

---

## 6. PRENOS V NASLEDNJE SLOJE

INTENT se lahko posreduje naprej samo kot:

- nespremenjena deklaracija
- brez obogatitve
- brez sklepanja

Naslednji sloji (Context, Evaluation, Decision)
**ne smejo spreminjati INTENTA**,
ampak se lahko nanj samo sklicujejo.

---

## 7. INVARIANTA

> Če sistem iz INTENTA sklepa pomen ali posledice,
> INTENT LAYER ne obstaja več.

Ta meja je absolutna.

---

## 8. ZAKLEP FAZE

Faza `INTENT_LAYER_INIT` se lahko označi kot **LOCKED**, ko velja:

- intent je zgolj deklarativen
- intent nima izvršilne moči
- intent ni interpretiran
- intent je sledljiv v audit zapisu

---

Konec dokumenta.
