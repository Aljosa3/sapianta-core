# DEMO_FLOW_2 — Decision-Governed Execution (Dry-Run)

## Status
REFERENCE DEMO — ARCHITECTURAL PROOF

## Namen
DEMO_FLOW_2 dokazuje, da sistem SAPIANTA
izvaja tok **izključno preko eksplicitne odločitve**
in da noben execution ne more nastopiti brez
normativnega Decision layerja.

Ta demo ni namenjen funkcionalnosti,
temveč **dokazu arhitekture**.

---

## Opis toka

DEMO_FLOW_2 razširi DEMO_FLOW_1 z uvedbo
Decision layerja med Assessment in Execution.

Tok poteka po naslednjem zaporedju:

1. **Chat**
   - sprejme uporabniški vnos
   - ustvari deklarativni INTENT
   - nima nobene odločitvene avtoritete

2. **Risk Assessment**
   - analizira intent v danem kontekstu
   - vrne signal (risk_level, confidence)
   - ne sprejema odločitev

3. **Decision Layer**
   - prejme sistemske signale
   - izvede eksplicitno odločitev (ALLOW | DENY | HOLD)
   - je edino mesto normativnega odločanja

4. **Execution Adapter (Dry-Run)**
   - prejme izključno Decision objekt
   - ne bere signalov ali intentov
   - ne izvaja dejanj
   - vrne simuliran execution plan

5. **Explain**
   - prikaže stanje in izid
   - nima vpliva na tok sistema

---

## Ključne lastnosti

- Decision je **strukturiran objekt**, ne slovar
- Execution adapter sledi samo Decision instanci
- HOLD je veljavna in stabilna odločitev
- Execution se ne izvede, tudi če je tehnično mogoč
- Vsi sloji so jasno ločeni

---

## Invariant

**No execution without explicit decision.**

Execution adapter mora imeti referenco
na veljavno Decision instanco.
V odsotnosti odločitve je execution prepovedan.

---

## Zaključek

DEMO_FLOW_2 potrjuje, da je arhitektura SAPIANTA
operativno pravilna, varna in skladna z
normativnimi zahtevami (npr. EU-style governance).

Ta demo služi kot referenčna točka
za nadaljnji razvoj:
- decision rules
- execution gate
- human-in-the-loop approval
