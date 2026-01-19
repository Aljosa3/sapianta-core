# DECISION_LAYER_REVIEW

## Status
LOCKED — KANONIČNA DEFINICIJA

## Povzetek
Decision layer je potrjen kot edini normativni sloj
za pretvorbo sistemskih signalov v eksplicitne odločitve.

Ta sloj:
- ne komunicira z uporabnikom
- ne izvaja dejanj
- ne razlaga odločitev

---

## Arhitekturna vloga
Decision layer deluje kot most med:
ASSESSMENT → DECISION → EXECUTION

Odločitev je dovoljenje ali prepoved,
ne pa dejanje.

---

## Potrjene omejitve
- Execution adapterji ne smejo delovati brez Decision instance
- Chat nima nobene odločitvene avtoritete
- Risk moduli ne vračajo odločitev
- Explain layer ne vpliva na odločanje

---

## Invariant
**No execution without explicit decision.**

Vsak execution adapter mora imeti referenco
na veljavno Decision instanco.

---

## Zaklep
Struktura decision sloja je zaklenjena.
Implementacija logike je dovoljena šele po
naslednji fazi odobritve.
