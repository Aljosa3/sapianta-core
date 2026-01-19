# DECISION_LAYER_INIT

## Status
INIT — DEFINICIJA SLOJA (BREZ LOGIKE)

## Namen
Decision layer je **edini sloj v sistemu SAPIANTA**, ki je pooblaščen
pretvoriti sistemske signale v **eksplicitno odločitev**.

Ta sloj:
- ne razlaga
- ne komunicira z uporabnikom
- ne izvaja dejanj

Odločitev je **normativna**, ne operativna.

---

## Vhodi (Inputs)
Decision layer lahko prejme izključno:
- validirane signale (npr. risk_assessment)
- kontekst sistema (jurisdiction, phase)
- referenco na veljavno avtoriteto odločanja

Decision layer **ne bere surovega uporabniškega vnosa**.

---

## Izhodi (Outputs)
Decision layer vrača **Decision object**, ki mora vsebovati:
- odločitev (ALLOW | DENY | HOLD)
- avtoriteto odločanja
- normativno podlago
- informacijo o zavezujočnosti

Izhod **ni izvršitev**.

---

## Prepovedi (Hard Constraints)
Decision layer:
- NE SME izvajati nobene kode
- NE SME klicati execution adapterjev
- NE SME ustvarjati razlage za uporabnika
- NE SME spreminjati vhodnih signalov

---

## Odnos do drugih slojev
- Chat: nima nobene avtoritete nad odločanjem
- Risk: dobavlja signale, ne odločitev
- Jurisdiction: omejuje dovoljene odločitve
- Execution: lahko sledi samo eksplicitni odločitvi

---

## Invariant
**No execution without explicit decision.**

Vsak execution adapter mora imeti
referenco na veljavno Decision instanco.

---

## Opombe
Decision layer je normativni most med:
ASSESSMENT → DECISION → EXECUTION

Logika odločanja bo uvedena šele po
formalnem review in lock faze.
