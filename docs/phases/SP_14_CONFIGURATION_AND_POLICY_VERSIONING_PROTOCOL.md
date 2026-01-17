# SP-14 — CONFIGURATION & POLICY VERSIONING PROTOCOL (CPVP)

**Status:** INIT  
**Vloga:** governance protokol za verzioniranje, aktivacijo in sledljivost konfiguracij ter politik v sistemu SAPIANTA

---

## 1️⃣ NAMEN FAZE

SP-14 določa **zavezujoča pravila**, kako se v sistemu SAPIANTA:
- verzionirajo konfiguracije in politike
- aktivirajo in deaktivirajo posamezne verzije
- zagotavlja sledljivost sprememb skozi čas
- preprečuje tihe ali implicitne spremembe vedenja

Cilj faze je:
- ločiti kodo od politike
- zagotoviti deterministično delovanje
- omogočiti nadzorovano evolucijo pravil
- preprečiti konfiguracijski drift

SP-14 **ne določa tehnične implementacije**, temveč **normativni okvir verzioniranja**.

---

## 2️⃣ OPREDELITEV KONFIGURACIJE IN POLITIKE

### 🔹 Konfiguracija
- parametri delovanja sistema
- pragovi, omejitve, vklopi/izklopi
- okoljske nastavitve

### 🔹 Politika
- normativna pravila odločanja
- omejitve, prepovedi, obveznosti
- governance pravila (npr. SP-9 do SP-13)

Konfiguracija **ne sme** nadomestiti politike.  
Politika **ne sme** biti implementirana kot skrita konfiguracija.

---

## 3️⃣ VERZIONIRANJE

Vsaka konfiguracija in politika mora imeti:
- enolični identifikator
- verzijsko oznako
- datum aktivacije
- status (DRAFT / INIT / ACTIVE / DEPRECATED)

Verzije so **nepovratne**:
> aktivne verzije se ne prepisujejo.

---

## 4️⃣ AKTIVACIJA IN DEAKTIVACIJA

Aktivacija verzije pomeni:
- izrecno izbiro verzije
- dokumentirano odločitev
- časovni žig

Deaktivacija:
- ne izbriše zgodovine
- označi verzijo kot neaktivno
- ohrani sledljivost

Implicitna aktivacija je **prepovedana**.

---

## 5️⃣ VEZAVA NA ODLOČITVE

Vsaka odločitev v sistemu mora biti:
- vezana na konkretno verzijo konfiguracije
- vezana na konkretno verzijo politike

Če verzije ni mogoče identificirati:
> odločitev se šteje za **neveljavno**.

---

## 6️⃣ ROLLBACK IN KOMPATIBILNOST

Rollback je dovoljen:
- samo na predhodno znano verzijo
- brez spremembe zgodovine
- z dokumentirano utemeljitvijo

Nova verzija mora:
- deklarirati kompatibilnost
- ali izrecno označiti prelom (BREAKING)

---

## 7️⃣ RAZMERJE DO CHANGE MANAGEMENTA

SP-14 deluje skupaj s SP-13:
- verzioniranje ≠ odobritev
- aktivacija verzije je sprememba
- vsaka aktivacija sledi postopku SP-13

Brez SP-13 odobritve:
> verzija ne sme postati ACTIVE.

---

## 8️⃣ AUDIT IN SLEDLJIVOST

Verzioniranje mora omogočiti:
- rekonstrukcijo stanja v času odločitve
- dokazovanje skladnosti
- preverjanje retroaktivnih vplivov

Audit **ne zahteva** vpogleda v implementacijo,
temveč v **verzijsko mapiranje**.

---

## 9️⃣ RAZMERJE DO DRUGIH FAZ

SP-14:
- temelji na SP-9 do SP-13
- ne spreminja Canona ali Core Laws
- ne uvaja runtime logike
- deluje izključno kot governance protokol

---

## 🔟 STATUS FAZE

Ta dokument ima status **INIT**.

Zaklep (LOCK) se lahko izvede po prvi uspešni verzijski migraciji brez regresij.

---
