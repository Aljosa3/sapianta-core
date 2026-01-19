# AUDIT_TRACE_IMPLEMENTATION_INIT — Runtime Hook & Append-Only Audit Log

## Status
INIT  
(Declarative implementation plan. No active runtime changes.)

---

## Purpose

AUDIT_TRACE_IMPLEMENTATION_INIT določa,
**kako se audit sled tehnično priključi (hooka) v runtime**,
brez posega v odločanje, execution ali razlago.

Ta dokument:
- ne uvaja dejanske implementacije
- ne spreminja obstoječega toka
- definira *kje* in *kako* se audit beleži

---

## Core Principle

> **Audit je pasiven opazovalec runtime-a.  
> Nikoli ne vpliva na potek sistema.**

Če audit odpove:
- sistem nadaljuje
- audit zabeleži napako kot dogodek
- ni rollbacka

---

## Hook Points (Read-Only)

Audit hook-i se lahko priključijo izključno na:

- Chat input acceptance
- Intent creation
- Risk signal emission
- Decision issuance
- ExecutionGate evaluation
- Execution adapter invocation (tudi dry-run)

Audit hook:
- prejme kopijo podatkov
- nima povratnega kanala
- nima pravice blokirati

---

## Canonical Runtime Placement

Audit implementacija je logično umeščena:

sapianta/
 ├─ runtime/
 │   ├─ controller.py
 │   └─ hooks/
 │       └─ audit_hook.py   (read-only)


Audit hook je:
- opcijski
- zamenljiv
- izoliran

---

## Audit Record Structure (Minimal)

Vsak zapis MORA vsebovati:

- `trace_id`
- `timestamp`
- `event_type`
- `origin`
- `payload_ref`
- `hash`

In NE SME vsebovati:
- osebnih podatkov
- polne vsebine payloada
- razlag ali sklepanj

---

## Append-Only Semantics

Audit zapis je:
- samo dodajalen (append-only)
- nespremenljiv po zapisu
- verižljiv (hash-chain ready)

Operacije, ki so prepovedane:
❌ update
❌ delete
❌ overwrite

---

## Failure Handling

Če audit zapis ne uspe:

- zabeleži se `AUDIT_FAILURE`
- runtime se NE ustavi
- odločitev ostane veljavna

Audit nikoli ni single point of failure.

---

## Separation Guarantees

Audit implementacija:
- ne kliče DecisionEngine
- ne kliče ExecutionGate
- ne kliče Explain layer
- ne dostopa do internih stanj modulov

Audit vidi **dogodke**, ne **namena**.

---

## Security & Compliance Notes

- Audit zapis je forenzičen, ne uporabniški
- Dostop je read-only
- Export je ločen proces (ni del runtime-a)

---

## Non-Goals

AUDIT_TRACE_IMPLEMENTATION_INIT:
- ne definira storage tehnologije
- ne definira retention obdobij
- ne definira export formatov

To so ločeni dokumenti.

---

## Verdict

AUDIT_TRACE_IMPLEMENTATION_INIT določa,
kako audit sled tehnično obstaja v sistemu,
brez vpliva na njegovo avtonomijo.

S tem je audit pripravljen za varno implementacijo.

---

## Next Steps (Suggested)

- AUDIT_TRACE_IMPLEMENTATION (code)
- AUDIT_RETENTION_POLICY_INIT
- AUDIT_EXPORT_INTERFACE_INIT

END OF AUDIT_TRACE_IMPLEMENTATION_INIT
