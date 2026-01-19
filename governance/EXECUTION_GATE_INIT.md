# EXECUTION_GATE_INIT

## Status
INIT — RUNTIME SAFETY GATE

## Namen
Execution Gate je obvezna runtime varovalka,
ki zagotavlja, da se noben execution adapter
ne more zagnati brez eksplicitne Decision instance.

Gate uveljavlja normativni invariant sistema
na tehnični ravni.

---

## Vloga v arhitekturi
Execution Gate se nahaja med:
DECISION → EXECUTION

Noben execution adapter se ne sme klicati neposredno.
Vsi klici morajo iti skozi Execution Gate.

---

## Vhodi
- Decision objekt (obvezen)
- Context (obvezen)
- Execution adapter (konkretna implementacija)

---

## Obnašanje
Execution Gate:
- preveri obstoj Decision instance
- preveri tip Decision (ni dict, ni signal)
- preveri skladnost z contextom
- zavrne execution, če pogoji niso izpolnjeni

---

## Prepovedi
Execution Gate:
- ne ustvarja odločitev
- ne razlaga odločitev
- ne spreminja Decision objekta
- ne izvaja dejanj sam

---

## Invariant
**No execution without explicit decision.**

Vsak execution adapter mora biti
klican izključno preko Execution Gate.

---

## Opomba
Execution Gate je obvezna komponenta
v vseh produkcijskih in demo tokovih,
razen če je eksplicitno izključen
v testnem okolju.
