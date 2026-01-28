
This policy is **normative** and **enforceable**.

---

## 2. ELIGIBILITY

A User Module is eligible for admission **only if all conditions below are met**.

### 2.1 Structural Eligibility (MANDATORY)

The module MUST:
- be external to SAPIANTA core
- be passive
- be non-executing
- be non-orchestrating
- be non-inferential
- use API v0.1 exclusively

The module MUST NOT:
- access runtime internals
- access HOI or HDS internals
- register hooks
- mutate state
- emit actions or decisions

---

## 3. REQUIRED ARTIFACTS

Every User Module submission MUST include **all** of the following artifacts:

### 3.1 Mandatory Files

| File | Requirement |
|----|----|
| `module.manifest.json` | REQUIRED |
| `contract.md` | REQUIRED |
| `README.md` | REQUIRED |
| API client (any language) | REQUIRED |

Missing any artifact → **AUTOMATIC REJECTION**

---

## 4. MANIFEST VALIDATION

The `module.manifest.json` MUST declare:

- `type = user_module`
- `mode = read_only` (or stricter)
- `api_version = v0.1`
- `llm = false`
- `runtime = false`
- `orchestration = false`
- `inference = false`

Any deviation → **REJECTION**

---

## 5. CONTRACT VALIDATION

The `contract.md` MUST explicitly state:

- external module status
- passive behavior
- read-only or contract-bound access
- prohibition of execution and decision logic

Absence or ambiguity → **REJECTION**

---

## 6. STATIC COMPLIANCE CHECKLIST

Admission is evaluated using the following checklist:

| Check | Result |
|----|----|
| External to core | ☐ |
| API v0.1 only | ☐ |
| No runtime access | ☐ |
| No execution logic | ☐ |
| No decision logic | ☐ |
| No LLM usage | ☐ |
| No inference | ☐ |
| Manifest valid | ☐ |
| Contract explicit | ☐ |

All checks MUST pass.

---

## 7. GROUNDS FOR REJECTION

A User Module MUST be rejected if it:

- violates any locked specification
- attempts to extend API surface
- introduces execution or orchestration
- embeds inference or decision authority
- circumvents semantic mapping
- backports logic into core

---

## 8. POST-ADMISSION RULES

Once admitted, a User Module:

- remains external
- remains passive
- may evolve internally
- MUST NOT expand privileges
- MUST reapply for admission if scope changes

---

## 9. FUTURE EXTENSIONS (NON-BINDING)

The following MAY be introduced in future policies:
- CLI admission rules
- Chat module admission rules
- Adapter admission rules

Such extensions require **separate governance approval**.

---

## 10. POLICY AUTHORITY

This policy is authoritative for User Module admission
until superseded by a formally locked successor.

POLICY VERSION: v0.1  
POLICY STATUS: ACTIVE (DRAFT)
