# JURISDICTION_LAYER_INIT

Status: INIT  
Odvisnost:
- DECISION_AUTHORITY_REGISTRY_INIT = LOCKED
- AUDIT_LAYER_INIT = LOCKED
- EXPLAIN_LAYER_INIT = LOCKED
- INTENT_LAYER_INIT = LOCKED
- CANON_GUARD_DECISION_CHAIN = ACTIVE

Razred: Governance / Jurisdiction  
Narava: Normativna (ne-logična, ne-odločitvena)

---

## 1. NAMEN

Vzpostaviti **JURISDICTION LAYER** kot edini dovoljen sloj za
uveljavljanje **pravnih, regulativnih in organizacijskih okvirov**,
znotraj katerih sistem sploh sme delovati.

Jurisdiction Layer:
- ne evaluira
- ne odloča
- ne izvršuje

Njegova vloga je **omejevalna**, ne aktivna.

---

## 2. TEMELJNO NAČELO

> Kar ni dovoljeno v jurisdikciji,
> se v sistemu **ne sme zgoditi**,
> ne glede na intent, evaluacijo ali authority.

Jurisdikcija ima prednost pred:
- moduli
- evaluacijo
- razlago
- izvršitvijo

---

## 3. KAJ JE JURISDIKCIJA

Jurisdikcija je formalni okvir, ki določa:

- kje sistem deluje
- pod katerimi pravili
- s katerimi omejitvami

Jurisdikcija:
- ni implementirana v modulih
- ni “če-potem” logika v kodi
- ni interpretativna

Je **deklarativni normativni sloj**.

---

## 4. OSNOVNA JURISDIKCIJA: EU (BASELINE)

Privzeta jurisdikcija sistema je:

- **EU – baseline**

To pomeni:
- spoštovanje veljavnih EU regulativ
- zmožnost uveljavljanja lokalnih razširitev
- prepoved delovanja, kjer skladnost ni zagotovljena

Druge jurisdikcije se lahko dodajo **le kot ločeni profili**.

---

## 5. JURISDIKCIJSKI PROFIL

Vsak jurisdikcijski profil mora vsebovati:

- identifikator jurisdikcije
- veljavna pravila in omejitve
- dovoljene tipe odločitev
- zahteve za authority
- zahteve za audit in explain
- omejitve executiona

Brez profila → jurisdikcija ne obstaja.

---

## 6. UPORABA JURISDIKCIJE

Jurisdiction Layer se uporablja:

- **pred Decision Gate**
- **pred Execution**
- kot **filter dovoljenosti**

Če jurisdikcija zavrne dejanje:
➡️ Decision Gate ne sme nadaljevati.

---

## 7. ODNOS DO MODULOV

Moduli:
- ne poznajo jurisdikcije
- ne vsebujejo pravil
- ne preverjajo zakonitosti

Če modul predpostavlja jurisdikcijo:
➡️ krši arhitekturo.

---

## 8. ODNOS DO AUTHORITY

Decision Authority:
- mora delovati znotraj jurisdikcije
- ne more preglasiti jurisdikcije
- ne more odločati izven dovoljenega okvira

Jurisdikcija je **nad** authority.

---

## 9. INVARIANTA

> Če se odločitev ali izvršitev zgodi
> v nasprotju z jurisdikcijo,
> sistem ni več skladen.

Ta invariant ima absolutno prednost.

---

## 10. ZAKLEP FAZE

Faza `JURISDICTION_LAYER_INIT` se lahko označi kot **LOCKED**, ko velja:

- jurisdikcija je ločen sloj
- moduli so jurisdikcijsko slepi
- jurisdikcija blokira nedovoljene poti
- ni obvodov ali izjem

---

Konec dokumenta.
