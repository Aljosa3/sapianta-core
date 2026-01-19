# DECISION_AUTHORITY_REGISTRY_INIT

Status: INIT  
Odvisnost:
- CANON_GUARD_DECISION_CHAIN = ACTIVE
- AUDIT_LAYER_INIT = LOCKED
- EXPLAIN_LAYER_INIT = LOCKED
- INTENT_LAYER_INIT = LOCKED

Razred: Governance / Authority  
Narava: Registracijska (ne-odločitvena)

---

## 1. NAMEN

Vzpostaviti **Decision Authority Registry** kot edini dovoljen mehanizem
za definicijo, identifikacijo in uporabo **nosilcev odločitev** v sistemu.

Brez registrirane Decision Authority:
- odločitev se ne sme zgoditi
- execution ni dovoljen
- sistem ostane v stanju *no-decision*

---

## 2. TEMELJNO NAČELO

> Odločitev je veljavna samo,
> če jo sprejme **registrirana in aktivna Decision Authority**.

Implicitne, privzete ali sklepane avtoritete so prepovedane.

---

## 3. KAJ JE DECISION AUTHORITY

Decision Authority je eksplicitno določen nosilec,
ki ima **pravno ali operativno legitimnost**, da:

- potrdi ali zavrne odločitev
- prevzame odgovornost
- pusti sled v auditu

Decision Authority:
- ni Guard
- ni Evaluation Layer
- ni Decision Gate
- ni modul

---

## 4. REGISTRIRANI TIPI AUTHORITY (OSNOVNI)

Registry lahko vsebuje izključno naslednje tipe:

### 4.1 Human Authority
- posameznik ali skupina
- potrjuje z zavestnim dejanjem (klik, podpis, potrditev)
- vedno auditirana

### 4.2 Legal / Policy Authority
- pravni ali normativni modul
- deluje v okviru jurisdikcije
- potrditve so deterministične

### 4.3 Certified System Authority
- sistemski modul z izrecno certifikacijo
- omejen obseg odločanja
- praviloma v sandbox ali nadzorovanem režimu

Drugi tipi niso dovoljeni brez spremembe registra.

---

## 5. REGISTRACIJSKI PODATKI

Vsaka Decision Authority mora imeti:

- enolični identifikator
- tip authority
- obseg pristojnosti
- jurisdikcijski okvir
- status (active / suspended / revoked)
- zahteve za audit

Brez popolne registracije → authority ne obstaja.

---

## 6. UPORABA REGISTRA

Decision Gate:
- lahko izbere authority **samo iz registra**
- ne sme sklepati ali nadomeščati authority
- ne sme uporabiti “najbližje” ali “privzete” možnosti

Če primerna authority ne obstaja:
➡️ odločitev se ne zgodi.

---

## 7. PREKLIC IN ŽIVLJENJSKI CIKEL

Authority:
- se lahko začasno suspendira
- se lahko trajno prekliče
- ne more delovati retroaktivno

Vsaka sprememba statusa:
- je auditirana
- ne vpliva na že sprejete odločitve

---

## 8. INVARIANTA

> Če je odločitev sprejeta brez
> registrirane Decision Authority,
> sistem ni več upravljan.

Ta invariant je nadrejen implementaciji.

---

## 9. ZAKLEP FAZE

Faza `DECISION_AUTHORITY_REGISTRY_INIT`
se lahko označi kot **LOCKED**, ko velja:

- registry obstaja
- authority so eksplicitne
- brez registra ni odločitev
- Decision Gate nima nadomestnih poti

---

Konec dokumenta.
