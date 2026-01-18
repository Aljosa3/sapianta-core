# UC-3.1 — OBSERVATION STATES
## AI Monitor / Auditor

**Use-case:** UC-3  
**Status:** DEFINITIVE  
**Layer:** Observational / Monitoring Semantics  
**Governance dependency:** Canon, CORE_LAWS, SP-9  
**Depends on:** UC-3_INIT

---

## 1. NAMEN DOKUMENTA

Ta dokument definira **opazovana stanja**, v katerih se lahko znajde
monitoring ali audit zaznava v use-caseu **UC-3: AI Monitor / Auditor**.

Dokument:
- NE uvaja novih pravil
- NE sproža dejanj
- NE opisuje implementacije

Dokument izključno opisuje:
> **opazovana sistemska stanja, ki jih AI lahko zazna in zabeleži**

---

## 2. NAČELO

V UC-3 AI:
- ne interpretira posledic
- ne predlaga ukrepov
- ne sproža izvajanja

Vsako zaznano stanje je:
- pasivno
- opisno
- ločeno od odločanja

---

## 3. DEFINICIJA OPAZOVANIH STANJ

### 3.1 NORMAL_STATE

**Opis:**  
Zaznano stanje je skladno s pričakovanim delovanjem sistema.

**Lastnosti:**
- brez odstopanj
- brez tveganj
- brez potrebe po opozorilu

**Opazovalni kriterij:**  
Ni zaznanih anomalij ali kršitev.

---

### 3.2 DEVIATION_DETECTED

**Opis:**  
Zaznano je odstopanje od pričakovanega ali referenčnega stanja.

**Lastnosti:**
- odstopanje je zaznano, ne interpretirano
- ne pomeni nujno kršitve
- zahteva pozornost, ne ukrepanja

**Opazovalni kriterij:**  
Zaznana je razlika glede na referenco.

---

### 3.3 POLICY_RISK_INDICATED

**Opis:**  
Zaznano stanje lahko pomeni potencialno normativno tveganje.

**Lastnosti:**
- tveganje ni potrjeno
- brez zaključkov
- brez samodejnih posledic

**Opazovalni kriterij:**  
Zaznani so indikatorji možne neskladnosti.

---

### 3.4 POLICY_VIOLATION_SUSPECTED

**Opis:**  
Zaznano stanje nakazuje možno kršitev pravil ali politike.

**Lastnosti:**
- kršitev ni potrjena
- AI ne presoja odgovornosti
- stanje zahteva človeški pregled

**Opazovalni kriterij:**  
Zaznani so močni indikatorji kršitve.

---

### 3.5 AUDIT_EVENT_RECORDED

**Opis:**  
Zaznano je stanje, ki zahteva formalni audit zapis.

**Lastnosti:**
- dogodek je zabeležen
- ni del uporabniške interakcije
- služi sledljivosti

**Opazovalni kriterij:**  
Dogodek izpolnjuje kriterije za audit.

---

## 4. POMEMBNE OMEJITVE

- Opazovana stanja niso odločitve
- Opazovana stanja ne sprožajo dejanj
- Opazovana stanja ne spreminjajo poteka sistema

Vsak odziv na ta stanja je:
> **zunaj obsega UC-3**

---

## 5. POVEZAVA NA SP-9

UC-3.1:
- ne vpliva na generacijo izhodov
- ne vpliva na normativno presojo
- ne posega v odločanje

Deluje izključno kot:
> **pasivni opazovalni sloj**

---

## 6. ZAKLJUČEK

S temi stanji je UC-3:
- formalno opredeljen
- regulatorno razložljiv
- združljiv z UC-1 in UC-2
- pripravljen za operativni tok

UC-3.1 ne razširja pravic AI
in ne uvaja novih odgovornosti.
