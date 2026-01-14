# F34.D — ARCHITECTURE FLOW (Sapianta OS)

Status: Draft (document-first)
Scope: End-to-end request flow
Audience: Core / Governance / Runtime contributors

---

## 1. Namen dokumenta

Ta dokument opisuje **celoten tok obdelave zahteve** v Sapianta OS – od vstopne točke (CLI / API / SaaS / LLM proxy) do zaklenjenega Execution Gate.

Cilji:

* popolna jasnost tokov
* stroga ločitev odgovornosti
* podlaga za nadaljnje faze (F35+)

---

## 2. Ključna načela

* Vsi vhodi so **enakovredni konektorji**
* Vse odločitve so **centralizirane**
* Noben sloj ne spreminja odločitev sloja pod sabo
* Execution je **fizično ločen** od odločanja

---

## 3. Visokonivojski tok (konceptualno)

```
[ Input Connector ]
        |
        v
[ Governance Interface ]
        |
        v
[ Sapianta Core ]
        |
        v
[ ROI Interface ]
        |
        v
[ Runtime Controller ]
        |
        v
[ Execution Gate ]
```

---

## 4. Podroben tok (operativni)

```
CLI / API / SaaS / LLM
        |
        v
+-----------------------+
| GovernanceRequest     |
| - request_type        |
| - raw_input           |
+-----------------------+
        |
        v
+-----------------------+
| Governance Interface  |
| - validacija sheme    |
| - transformacija     |
+-----------------------+
        |
        v
+-----------------------+
| CoreRequest           |
+-----------------------+
        |
        v
+-----------------------+
| Sapianta Core         |
| - deterministična     |
|   semantična ocena    |
+-----------------------+
        |
        v
+-----------------------+
| ChatResponse          |
| (ACCEPTED / REJECTED) |
+-----------------------+
        |
        v
+-----------------------+
| ROI Interface         |
| - community overlays  |
| - org overlays        |
+-----------------------+
        |
        v
+-----------------------+
| Runtime Controller    |
| - združi Core + ROI   |
| - HALT / PROCEED      |
+-----------------------+
        |
        v
+-----------------------+
| Execution Gate        |
| - NO_OP (F34)         |
+-----------------------+
```

---

## 5. Odločitvena pravila (resnica sistema)

### 5.1 Core

* vedno vrne odločitev
* nikoli ne izvaja akcij

### 5.2 ROI

* nikoli ne spremeni Core odločitve
* lahko samo **omeji nadaljevanje**

### 5.3 Runtime

* edini sloj, ki določi tok (HALT / PROCEED)

### 5.4 Execution

* ne obstaja brez Runtime PROCEED
* trenutno NO-OP

---

## 6. Negativni tokovi (primeri)

### Primer A: Prazen vnos

* Core: REJECTED
* Runtime: HALT (CORE_REJECTED)
* Execution: NO_OP

### Primer B: Veljaven vnos + ROI blok

* Core: ACCEPTED
* ROI: BLOCK
* Runtime: HALT (ROI_BLOCKED)
* Execution: NO_OP

---

## 7. Kaj ta dokument NI

* ne opisuje implementacije
* ne opisuje UI
* ne opisuje poslovne logike

---

## 8. Nadaljnji koraki

Po potrditvi tega dokumenta:

* F35 — Execution Adapter Interface
* F36 — Runtime Trace (observability)
* F37 — API Adapter

---

END
