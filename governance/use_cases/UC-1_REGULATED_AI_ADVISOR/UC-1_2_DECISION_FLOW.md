# UC-1.2 — DECISION FLOW
## Regulated AI Advisor

**Use-case:** UC-1  
**Status:** DEFINITIVE  
**Layer:** Operational / Runtime Flow  
**Governance dependency:** Canon, CORE_LAWS, SP-9  
**Depends on:** UC-1.1 (Output States)

---

## 1. NAMEN DOKUMENTA

Ta dokument opisuje **operativni tok odločanja** v use-caseu
**UC-1: Regulated AI Advisor**.

Dokument:
- NE uvaja novih pravil
- NE razlaga normativnih odločitev
- NE opisuje implementacijskih detajlov

Dokument izključno opisuje:
> **kako sistem pride od uporabniškega vprašanja do enega izmed izhodnih stanj**

---

## 2. NAČELO TOKA

Odločanje v UC-1 poteka v **strogo zaporednih fazah**.
Vsaka faza ima jasno vlogo in ne posega v druge faze.

AI-model:
- sodeluje samo v fazi generacije
- nima vpogleda v normativno presojo
- ne ve, kateri izhod bo uporabljen

---

## 3. VISOKO-NIVOJSKI TOK

