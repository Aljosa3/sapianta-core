# PHASE 42 — Capability Policy Engine (PURPOSE)

## Status
PURPOSE — CANONICAL INTENT DEFINITION

## Namen faze

F42 definira **Capability Policy Engine**, osrednji normativni sloj,
ki odloča ali se deklarirana zmožnost (capability) modula
lahko uporabi v določenem kontekstu.

F42 je **edini dovoljeni sloj**, kjer se lahko
deklarirana capability začasno pretvori v dovoljenje (permission).

---

## Ključna razmejitev

- Capability ≠ Permission
- Capability je deklarativna
- Permission je kontekstna in pogojna

F42 **nikoli ne izvaja dejanj** in **nikoli ne spreminja Core odločitve**.

---

## Pozicija v sistemu

F42 se nahaja med deklaracijo modula in runtime odločitvijo:

Module  
→ F40 Identity  
→ F41 Capability Declaration  
→ **F42 Capability Policy Engine**  
→ RuntimeController  
→ Execution Gate  

---

## Vhodni podatki

F42 obravnava izključno naslednje informacije:

- Identity modula
- Deklarirane capability-je
- Zahtevano capability
- Execution Intent (namen uporabe)
- Invocation Context (CLI, API, SaaS, Agent)

F42 **nima dostopa** do Core notranje logike.

---

## Izhod F42

F42 lahko vrne izključno eno od naslednjih odločitev:

- ALLOW
- DENY
- CONDITIONAL

F42 nikoli ne vrača odločitve za execution.

---

## Hierarhija pravil

F42 spoštuje strogo hierarhijo policy pravil:

1. System Canon Policies
2. Community Policies (npr. regulativni okviri)
3. Organizational Policies
4. Local / Contextual Policies

Nižji nivo **ne more razveljaviti višjega**.

---

## Varnostno pravilo

Če F42:
- ne obstaja
- odpove
- nima ustreznega pravila

je **privzeta odločitev vedno DENY**.

---

## Kaj F42 ne počne

F42:
- ne izvaja dejanj
- ne upravlja execution
- ne vsebuje runtime logike
- ne implementira ROI pravil
- ne vsebuje policy jezika (DSL)

Te funkcije so predmet naslednjih faz.

---

## Odnos do naslednjih faz

- F43: Capability Enablement
- F44: Execution Binding

F42 vzpostavi **normativni temelj**, na katerem lahko
naslednje faze varno gradijo.

---

## Zaklep namena

Ta dokument definira **namen in meje F42**.
Vsaka implementacija mora biti z njim skladna.

Spremembe so dovoljene izključno prek nove faze.
