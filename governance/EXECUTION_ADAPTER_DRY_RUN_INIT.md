# EXECUTION_ADAPTER_DRY_RUN_INIT

Status: INIT  
Scope: Execution simulation only  
Lock: NO

---

## 1. NAMEN

Ta dokument uvaja **Execution Adapter v načinu dry-run**.

Namen adapterja je:
- simulirati potencialno izvršitev
- prikazati, kaj bi se zgodilo
- preprečiti dejansko izvajanje

---

## 2. MEJE ADAPTERJA

Dry-run adapter:

- ne izvaja dejanj
- ne spreminja sistema
- ne dostopa do zunanjih virov
- ne odloča
- ne presoja pravilnosti

---

## 3. ODNOS DO SISTEMA

Execution adapter:

- prejme izhod iz Decision sloja (ali demo substitut)
- prejme sistemski context
- vrne simuliran execution plan

Če je `execution_allowed = true`, se adapter **mora ustaviti**.

---

## 4. VARNOSTNA INVARIANTA

> Execution brez eksplicitne odobritve ni dovoljen.

Dry-run adapter to invarianto **strogo uveljavlja**.

---

## 5. ZAKLJUČEK

Ta adapter omogoča razvoj in testiranje
izvršitvenih tokov brez tveganja.

---

Konec dokumenta.
