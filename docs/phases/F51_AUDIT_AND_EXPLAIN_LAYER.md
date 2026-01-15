# F51_AUDIT_AND_EXPLAIN_LAYER.md
Status: ACTIVE · POST-MPL
Vezano na: F47_LOCK, MPL_LOCK, F48_50_LOCK
Namen: Določitev auditnega in razlagalnega sloja sistema Sapianta

---

## 1. NAMEN FAZE F51

Faza F51 določa, kako sistem Sapianta:
- beleži odločitve
- razlaga zavrnitve in zaustavitve
- omogoča audit brez razkritja notranje logike

F51:
- ne uvaja novih normativnih pravil
- ne vpliva na runtime enforcement
- ne spreminja odločitev sistema

F51 je izključno razlagalni in opazovalni sloj.

---

## 2. LOČITEV MED ODLOČANJEM IN RAZLAGO

Odločanje:
- se zgodi v runtime (F47)
- je deterministično
- je neobidljivo

Razlaga:
- sledi odločitvi
- nima povratnega vpliva
- ne more spremeniti izida

Razlaga nikoli ne sodeluje pri odločanju.

---

## 3. VRSTE SISTEMSKIH IZIDOV

Sistem Sapianta razlikuje naslednje izide:

### 3.1 ALLOW
- zahteva je dovoljena
- proces se zaključi normalno
- izhod je posredovan

### 3.2 DENY
- zahteva je zavrnjena
- proces se ustavi
- ni nadaljevanja

### 3.3 HALT
- proces se zaustavi zaradi kršitve
- ni izvršitve
- izhod ni posredovan

### 3.4 HARD_FAIL
- zaznana je sistemska anomalija
- proces se prekine
- zahteva nadaljnjo tehnično obravnavo

Audit sloj mora razlikovati vse štiri izide.

---

## 4. VSEBINA RAZLAGE

Razlaga lahko vsebuje:
- tip izida (ALLOW / DENY / HALT / HARD_FAIL)
- fazo odločitve (SP-1, SP-2, SP-3, system)
- splošni razlog zavrnitve
- časovni žig

Razlaga ne sme vsebovati:
- notranjih pravil Canona
- konkretnih normativnih členov
- logike odločanja
- zaporedja preverjanj

---

## 5. NASLOVNIKI RAZLAGE

Razlaga je prilagojena naslovniku:

### 5.1 Uporabnik
- prejme minimalno razlago
- razlaga je informativna
- ne omogoča ugibanja sistema

### 5.2 Organizacija / lastnik sistema
- prejme razširjeno razlago
- vključuje fazo in tip izida
- ne razkriva Canona

### 5.3 Audit / regulator
- prejme formalno razlago
- vključuje dokaz skladnosti
- ne razkriva izvršilne logike

---

## 6. AUDIT ZAPISI

Sistem mora omogočiti beleženje:
- časa odločitve
- tipa izida
- prizadete komponente (chat / modul / LLM)
- identifikatorja zahteve

Audit zapisi:
- so ločeni od runtime logike
- niso del odločanja
- se ne uporabljajo za optimizacijo

---

## 7. PREPOVEDI AUDIT SLOJA

Audit / Explain sloj ne sme:
- vplivati na potek runtime
- sprožiti ponovne obdelave
- ustvarjati alternativnih izidov
- omogočati rekonstrukcije Canona

Vsak tak poskus:
→ je neveljaven

---

## 8. ODNOS DO DRUGIH FAZ

F51:
- sledi F48–F50
- ne predhaja nobeni normativni fazi
- je kompatibilen z vsemi execution sloji

Audit sloj:
- opazuje
- razlaga
- ne odloča

---

## 9. KONČNA IZJAVA

Sistem, ki odloča, mora znati pojasniti.
Sistem, ki pojasnjuje, ne sme odločati.

Audit in razlaga sta pravica človeka,
ne orodje sistema.
