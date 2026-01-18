# GUARD_DECISION_GATE_INIT

Status: INIT  
Odvisnost:
- RUNTIME_GUARD_INIT = LOCKED
- GUARD_CONTEXT_SURFACE_INIT = LOCKED
- GUARD_EVALUATION_LAYER_INIT = LOCKED

Razred: Runtime / Governance  
Narava: Odločitvena točka (strogo omejena)

---

## 1. NAMEN

Vzpostaviti **edino dovoljeno odločitveno točko**, kjer se lahko:
- evalvacijski signal *pretvori* v odločitev
- vendar **ne s strani Guarda**
- in **ne brez zunanjega odločitvenega nosilca**

Ta faza obstaja izključno zato, da prepreči razlivanje odločanja drugam.

---

## 2. TEMELJNO NAČELO

> Guard nikoli ne odloča.  
> Guard lahko le **posreduje evalvacijo** v odločitveni prehod.

Vsaka odločitev:
- se zgodi **izven Guarda**
- je **eksplicitno vezana** na Decision Gate
- ima jasno določeno odgovornost

---

## 3. VHODI V DECISION GATE

Decision Gate lahko prejme izključno:

- evalvacijski signal iz `GUARD_EVALUATION_LAYER_INIT`
- identifikator konteksta
- referenco na aktivne policy ID-je
- referenco na jurisdikcijske oznake

❌ brez surovega vhoda  
❌ brez dodatne interpretacije  
❌ brez samostojne obogatitve podatkov  

---

## 4. DOVOLJENE OPERACIJE GATE-A

Decision Gate SME:

- preslikati evalvacijski signal → odločitveni razred
- izbrati ustrezen **Decision Authority** (če obstaja)
- pripraviti **odločitveni zahtevek**

Decision Gate NE SME:

- sprejeti končne odločitve
- izvajati politike
- sprožiti blokade
- dovoliti ali zavrniti dejanja

---

## 5. ODLOČITVENI NOSILEC (DECISION AUTHORITY)

Vsaka odločitev mora biti izvedena s strani:

- zunanjega odločitvenega modula
- ali eksplicitno določenega normativnega sloja
- ali človeškega odobritvenega vmesnika

Decision Authority:
- NI Guard
- NI del Decision Gate
- NI implicitna

Če Decision Authority ne obstaja → **odločitev se ne zgodi**.

---

## 6. IZHOD DECISION GATE-A

Edini dovoljen izhod je:

- **Odločitveni zahtevek**, ki vsebuje:
  - identifikator konteksta
  - povzetek evalvacije (brez razlage)
  - zahtevan tip odločitve
  - referenco na policy / jurisdikcijo

Gate sam:
- ne izvaja
- ne blokira
- ne potrjuje

---

## 7. IZRECNE PREPOVEDI

V tej fazi je absolutno prepovedano:

- implicitno odločanje
- samodejno dovoljevanje
- samodejno zavračanje
- fallback odločanje
- “best-effort” presoja

Vsaka od teh točk pomeni **kritično kršitev arhitekture**.

---

## 8. INVARIANTA

> Če se odločitev zgodi brez jasno določene Decision Authority,
> sistem ni več upravljan — temveč samovoljen.

Ta invariant je nadrejen implementaciji.

---

## 9. ZAKLEP FAZE

Faza `GUARD_DECISION_GATE_INIT` se lahko označi kot **LOCKED**, ko velja:

- Decision Gate je edina odločitvena točka
- Guard nima odločitvene moči
- brez Decision Authority ni odločitve
- odločanje je strogo ločeno od evaluacije

S tem je **Guard-veriga zaključena**.

---

Konec dokumenta.
