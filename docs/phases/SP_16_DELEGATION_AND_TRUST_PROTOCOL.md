# SP-16 — DELEGATION & TRUST PROTOCOL (DTP)

**Status:** INIT  
**Vloga:** governance protokol za delegiranje avtoritete, vzpostavljanje zaupanja in nadzor delegiranih dejanj v sistemu SAPIANTA

---

## 1️⃣ NAMEN FAZE

SP-16 določa **zavezujoča pravila**, kako se v sistemu SAPIANTA:
- delegira avtoriteta med akterji
- omejuje obseg delegiranih pravic
- vzpostavlja in razveljavlja zaupanje
- preprečuje trajna ali implicitna pooblastila

Cilj faze je:
- omogočiti varno razširjanje delovanja sistema
- preprečiti nenadzorovano eskalacijo pravic
- zagotoviti sledljivost delegiranih dejanj
- ohraniti centralno odgovornost

SP-16 **ne uvaja tehnične implementacije**, temveč **normativni okvir delegiranja**.

---

## 2️⃣ DEFINICIJA DELEGACIJE

Delegacija pomeni:
> časovno, vsebinsko in namensko omejen prenos pravice za izvajanje dejanja.

Delegacija **ni**:
- prenos lastništva
- trajna podelitev pravic
- implicitna razširitev avtoritete

Vsaka delegacija je:
- izrecna
- sledljiva
- preklicljiva

---

## 3️⃣ TIPI DELEGACIJE

### 🔹 OPERATIVNA DELEGACIJA
- izvajanje rutinskih dejanj
- brez spreminjanja pravil ali konfiguracij

### 🔹 TEHNIČNA DELEGACIJA
- upravljanje konfiguracij ali verzij
- brez normativnih sprememb

### 🔹 NORMATIVNA DELEGACIJA
- predlaganje sprememb (SP-13)
- brez samodejne odobritve

Normativna delegacija **nikoli** ne vključuje pravice do potrditve.

---

## 4️⃣ POGOJI ZA DELEGACIJO

Delegacija je dovoljena samo, če:
- delegator ima izvorno pravico
- obseg delegacije je natančno določen
- trajanje je omejeno
- namen je eksplicitno zapisan

Delegacija brez vseh pogojev je **neveljavna**.

---

## 5️⃣ MEJE DELEGACIJE

Delegirati **ni dovoljeno**:
- zaklepanja faz (LOCK)
- sprememb Canona ali Core Laws
- odobritev kritičnih sprememb (SP-13 Kategorija I)
- nadzorne (OVERSIGHT) avtoritete

Te pravice so **nedeljive**.

---

## 6️⃣ NAČELO ZAUPANJA

Zaupanje v sistemu SAPIANTA:
- je vezano na kontekst
- je reverzibilno
- ni globalno

Zaupanje se podeljuje:
- za namen
- za čas
- za obseg

Zaupanje **ni identiteta**.

---

## 7️⃣ PREKLIC IN IZTEK

Vsaka delegacija:
- ima določen iztek
- se lahko kadarkoli prekliče
- se samodejno razveljavi ob kršitvi

Preklic:
- ne zahteva utemeljitve
- ima takojšen učinek
- se zabeleži

---

## 8️⃣ SLEDLJIVOST IN ODGOVORNOST

Za vsako delegirano dejanje:
- je znan delegator
- je znan delegirani akter
- je znan obseg delegacije
- obstaja revizijska sled

Odgovornost:
> ostaja vedno na delegatorju.

---

## 9️⃣ KRŠITVE DELEGACIJE

Kršitev pomeni:
- preseganje obsega
- izvajanje po izteku
- implicitno širitev pravic

Vsaka kršitev:
- sproži incident (SP-12)
- povzroči takojšen preklic
- se dokumentira

---

## 🔟 RAZMERJE DO DRUGIH FAZ

SP-16:
- temelji na SP-12 (Incident Response)
- uporablja SP-13 (Change Management)
- spoštuje SP-14 (Versioning)
- dopolnjuje SP-15 (Access Control)

SP-16 **ne spreminja** Canona ali Core Laws.

---

## 1️⃣1️⃣ STATUS FAZE

Ta dokument ima status **INIT**.

Zaklep (LOCK) se lahko izvede po vsaj eni uspešni delegaciji brez eskalacij.

---
