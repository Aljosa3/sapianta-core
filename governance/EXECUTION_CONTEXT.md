# EXECUTION CONTEXT

## Status
DESIGN-ONLY — execution ni dovoljen

## Namen
Execution Context definira **minimalni, obvezni okvir**, v katerem se
lahko v prihodnosti izvede katerakoli akcija.

Brez popolnega Execution Contexta:
→ execution ni dovoljen.

Dokument se sklicuje na:
- LOCK_PRE_EXECUTION_ERA
- EXECUTION_ERA_ENTRY_CRITERIA
- EXECUTION_BOUNDARY

---

## 1. Temeljno pravilo

Execution Context:
- je **obvezen**
- je **nespremenljiv med izvedbo**
- je **popolnoma strukturiran**
- ne vsebuje naravnega jezika

Execution brez konteksta je **izrecno prepovedan**.

---

## 2. Obvezni elementi Execution Contexta

Vsak Execution Context MORA vsebovati:

### 2.1 Identiteta
- execution_id (unikaten)
- request_id (povezava na ChatRequest)
- plan_id (povezava na Plan)

### 2.2 Namen
- declared_intent (strukturiran, ne NLP)
- execution_scope (omejen obseg)

### 2.3 Časovni okvir
- created_at
- valid_until (če preseženo → ne izvrši)

### 2.4 Izvor
- initiated_by (user / system / delegated)
- source_layer (vedno: Planning)

---

## 3. Prepovedani elementi

Execution Context NE SME vsebovati:
- naravnega jezika
- interpretacij
- odločitev
- pogojev, ki bi zahtevali presojo

---

## 4. Validacija

Pred vsako izvedbo mora Execution Context:
- prestati popolno validacijo
- biti zavrnjen ob najmanjši nejasnosti
- biti zapisan v audit log

---

## 5. Razmerje do drugih slojev

- Chat: ustvari zahtevo
- Reasoning: razloži
- Planning: strukturira
- Execution Context: **zaklene pogoje**

Execution ne more:
- razširiti konteksta
- popraviti konteksta
- interpretirati konteksta

---

Dokument potrjen kot referenca.
Execution Context je definiran.
Execution ostaja NEAKTIVEN.
