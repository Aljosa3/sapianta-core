# SP-15 — ACCESS CONTROL & AUTHORITY PROTOCOL (ACAP)

**Status:** INIT  
**Vloga:** governance protokol za določanje pristojnosti, dostopa in avtoritete akterjev v sistemu SAPIANTA

---

## 1️⃣ NAMEN FAZE

SP-15 določa **zavezujoč okvir**, ki opredeljuje:
- kdo ima pravico do katerih dejanj
- kdo lahko sproža, spreminja ali potrjuje odločitve
- kako se ločijo pristojnosti med akterji
- kako se preprečijo implicitne ali eskalirane pravice

Cilj faze je:
- preprečiti nepooblaščene posege
- zagotoviti jasno hierarhijo avtoritete
- omogočiti varno sodelovanje več akterjev
- ohraniti nadzor nad kritičnimi funkcijami sistema

SP-15 **ne določa tehnične implementacije**, temveč **normativni model avtoritete**.

---

## 2️⃣ DEFINICIJA AKTERJEV

Sistem SAPIANTA prepoznava naslednje tipe akterjev:

### 🔹 ČLOVEK (Human Actor)
- lastnik sistema
- operater
- vzdrževalec
- pooblaščeni auditor

### 🔹 SISTEM (System Actor)
- runtime
- guard sloji
- orchestrator
- policy engine

### 🔹 AI (AI Actor)
- generativni modeli
- analizni moduli
- pomožni agenti

### 🔹 ZUNANJI ORGAN (External Authority)
- regulator
- certifikacijski organ
- pogodbeni nadzornik

Vsak akter ima **omejeno in definirano avtoriteto**.

---

## 3️⃣ NAČELO NAJMANJŠIH PRAVIC

> Vsak akter ima **najmanjši možni nabor pravic**, ki še omogoča njegovo vlogo.

- pravice niso dedne
- pravice niso implicitne
- pravice so časovno in vsebinsko omejene

---

## 4️⃣ AVTORITETNE RAVNI

### 🔹 RAVEN 0 — OBSERVE
- ogled explain artefaktov
- brez vpliva na sistem

### 🔹 RAVEN 1 — OPERATE
- sprožanje dovoljenih interakcij
- brez sprememb pravil ali konfiguracij

### 🔹 RAVEN 2 — CONFIGURE
- upravljanje konfiguracij
- brez sprememb normativnih pravil

### 🔹 RAVEN 3 — GOVERN
- spreminjanje governance dokumentov (INIT / ACTIVE)
- predlaganje sprememb (SP-13)

### 🔹 RAVEN 4 — AUTHORIZE
- odobritev sprememb
- aktivacija verzij (SP-14)
- sprožitev LOCK faz

### 🔹 RAVEN 5 — OVERSIGHT
- audit dostop
- nadzor skladnosti
- brez posega v delovanje

Nobena raven **ne vključuje** višje ravni implicitno.

---

## 5️⃣ DOVOLJENA DEJANJA PO AKTERJIH

| Akter | Najvišja dovoljena raven |
|------|--------------------------|
| Human (Owner) | RAVEN 4 |
| Human (Operator) | RAVEN 1 |
| AI Actor | RAVEN 1 |
| System Actor | RAVEN 2 |
| External Authority | RAVEN 5 |

Vsako odstopanje zahteva **izrecno odobritev**.

---

## 6️⃣ PREPREČEVANJE ESKALACIJE

Sistem **mora preprečiti**:
- samodejno eskalacijo pravic
- krožno potrjevanje (self-approval)
- prenos avtoritete brez sledi
- združevanje nezdružljivih vlog

Avtoriteta je **neprenosljiva brez postopka**.

---

## 7️⃣ DOSTOP DO PODATKOV IN ARTEFAKTOV

Dostop do:
- explain artefaktov → RAVEN 0+
- audit evidence → RAVEN 5
- execution trace → SYSTEM ONLY (izjemoma agregirano)

Nepravilni dostop pomeni **kršitev SP-15**.

---

## 8️⃣ RAZMERJE DO DRUGIH FAZ

SP-15:
- temelji na SP-9 do SP-14
- deluje skupaj s SP-13 (Change Management)
- uporablja SP-14 (Versioning)
- ne spreminja Canona ali Core Laws

SP-15 je **avtoritetni okvir**, ne implementacija.

---

## 9️⃣ KRŠITVE IN POSLEDICE

Vsaka kršitev:
- se obravnava kot incident (SP-12)
- se dokumentira
- lahko sproži začasno omejitev pravic

Ponovljene kršitve:
> zahtevajo revizijo avtoritete.

---

## 🔟 STATUS FAZE

Ta dokument ima status **INIT**.

Zaklep (LOCK) se lahko izvede po praktični uporabi z več akterji in brez eskalacij.

---
