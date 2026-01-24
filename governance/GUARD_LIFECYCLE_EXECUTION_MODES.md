# GUARD LIFECYCLE — EXECUTION MODES
Version: 1.0
Status: DRAFT (pre-lock)
Authority: GuardLifecycle Protocol
Scope: Runtime execution semantics

---

## 1. Namen dokumenta

Ta dokument definira **execution modes** kot
edino dovoljeno razlikovanje med vrstami izvajanja
znotraj GuardLifecycle.

Execution mode:
- NI izvršilna pot
- NI varnostna izjema
- NI bližnjica

Execution mode je **parametrična izbira izida**, ne vstopa.

---

## 2. Kanonična definicija execution mode

Execution mode je obvezni parameter,
ki določa:

- dovoljene side-effecte
- vrsto rezultata
- ciljni delegat izvedbe

Execution mode **NE vpliva** na:
- guard zaporedje
- normativne zahteve
- SCF presojo
- audit obveznosti

---

## 3. Seznam kanoničnih execution modes

### 3.1 EXECUTION

**Namen**
- dejanska izvedba sistema z dovoljenimi side-effecti

**Lastnosti**
- dovoljen runtime execution
- dovoljena sprememba stanja
- zahteva:
  - Status.ALLOW
  - Phase.EXECUTION
  - uspešen prehod vseh guard faz

**Delegacija**
- MEP orchestrator

**Prepovedi**
- brez GuardLifecycle → neveljavno
- brez audit traila → neveljavno

---

### 3.2 DRY_RUN

**Namen**
- normativna ocena možnosti izvedbe
- simulacija brez side-effectov

**Lastnosti**
- brez dejanskega execution
- brez spremembe sistemskega stanja
- guard zaporedje je **identično** EXECUTION

**Delegacija**
- DryRunEngine

**Rezultat**
- ELIGIBLE / INELIGIBLE / REFUSED / ERROR

**Prepovedi**
- obid guardov
- implicitna dovoljenja

---

### 3.3 CHAT

**Namen**
- interakcija brez izvršilne moči
- svetovalni ali razlagalni izhod

**Lastnosti**
- brez execution side-effectov
- brez normativne avtoritete
- guard zaporedje je **identično**

**Delegacija**
- Chat handler

**Omejitve**
- izhod je vedno:
  - advisory
  - non-binding
  - brez vpliva na Status ali Phase

---

## 4. Enotnost guard zaporedja (GL-2, GL-4)

Za vse execution modes velja:

- isti GuardLifecycle
- isti runtime guards
- isti SP passes
- isti execution gate
- isti audit hook

Razlika je dovoljena **samo v delegaciji izvedbe**.

---

## 5. Prepovedi (ključni lock)

Prepovedano je:

- imeti ločene entry-pointe za posamezne execution modes
- zmanjšati guard zaporedje za CHAT ali DRY_RUN
- implicitno dovoliti izvršitev zaradi mode-a
- interpretirati execution mode kot “nižjo varnost”

Vsaka taka implementacija je kršitev GL-2 in GL-4.

---

## 6. Execution mode kot arhitekturni parameter

Execution mode:
- je obvezen
- je ekspliciten
- je del ExecutionContext
- ne sme imeti privzete vrednosti

Manjkajoč execution mode → **ProtocolViolation**

---

## 7. Audit obveznosti (GL-5)

Ne glede na execution mode:

- audit trail je obvezen
- rezultat mora biti determinističen
- zavrnitev mora biti vidna

Ni “tihega” izhoda.

---

## 8. Status dokumenta

Ta dokument:
- zaključi GuardLifecycle arhitekturno definicijo
- deluje kot:
  - SCF dodatek
  - testna osnova
  - implementacijski lock
- mora biti zaklenjen pred:
  - runtime integracijo
  - odstranitvijo bypass poti
