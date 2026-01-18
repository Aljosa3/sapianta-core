# UC-3.2 — DECISION FLOW
## AI Monitor / Auditor

**Use-case:** UC-3  
**Status:** DEFINITIVE  
**Layer:** Operational / Monitoring Flow  
**Governance dependency:** Canon, CORE_LAWS, SP-9  
**Depends on:** UC-3_INIT, UC-3.1 (Observation States)

---

## 1. NAMEN DOKUMENTA

Ta dokument opisuje **operativni tok monitoringa in audita**
v use-caseu **UC-3: AI Monitor / Auditor**.

Dokument:
- NE uvaja novih pravil
- NE sproža dejanj
- NE opisuje implementacijskih detajlov

Dokument izključno opisuje:
> **kako sistem zazna, razvrsti in zabeleži opazovana stanja**

---

## 2. NAČELO TOKA

V UC-3 tok poteka **pasivno in enosmerno**:
- brez vpliva na druge tokove
- brez posega v odločanje
- brez eskalacije pravic

AI nikoli ne preide iz opazovanja v izvajanje.

---

## 3. VISOKO-NIVOJSKI TOK

System Events
↓
Observation Capture
↓
State Classification
↓
Audit Recording
↓
Human Review (out of band)


---

## 4. FAZE TOKA

### 4.1 SYSTEM EVENTS

**Opis:**  
Dogodki ali stanja, ki nastajajo v sistemu (izven AI).

**Lastnosti:**
- izvirajo iz delovanja sistema
- niso generirani s strani AI
- lahko so normalni ali anomalni

---

### 4.2 OBSERVATION CAPTURE

**Opis:**  
AI zazna dogodek ali stanje.

**Lastnosti:**
- pasivno zaznavanje
- brez interpretacije posledic
- brez odločanja

---

### 4.3 STATE CLASSIFICATION

**Opis:**  
Zaznano stanje se razvrsti v eno izmed opazovanih stanj
(glej UC-3.1).

**Možna stanja:**
- NORMAL_STATE  
- DEVIATION_DETECTED  
- POLICY_RISK_INDICATED  
- POLICY_VIOLATION_SUSPECTED  
- AUDIT_EVENT_RECORDED  

**Lastnosti:**
- točno eno stanje
- brez kombinacij
- brez avtomatskih odzivov

---

### 4.4 AUDIT RECORDING

**Opis:**  
Sistem ustvari sledljiv zapis zaznave.

**Lastnosti:**
- zapis je neodvisen od uporabniške interakcije
- namenjen nadzoru in reviziji
- ne vpliva na nadaljnje tokove

---

### 4.5 HUMAN REVIEW (OUT OF BAND)

**Opis:**  
Človeški pregled zaznanih stanj.

**Lastnosti:**
- izven AI sistema
- brez avtomatizacije
- ni del UC-3

---

## 5. KLJUČNE LOČITVE

Tok v UC-3 eksplicitno ločuje:

- opazovanje ↔ odločanje  
- zaznavo ↔ ukrepanje  
- audit ↔ izvajanje  

S tem se prepreči:
- prikrita avtonomija
- eskalacija pravic
- nenamerno delovanje AI

---

## 6. ZAKLJUČEK

S tem decision flowom je UC-3:
- operativno razložen
- pasiven in neinvaziven
- regulatorno sledljiv
- združljiv z UC-1 in UC-2

UC-3.2 ne spreminja nobenega obstoječega pravila
in ne uvaja novih pravic AI.
