# KERNEL EXECUTION GRAPH VALIDATION v1.0
Status: GOVERNANCE-LOCK CANDIDATE
Layer: 0 (Kernel)
Scope: STATIC + STRUCTURAL VALIDATION ONLY
Effective: v1.2.2-kernel-governance-locked +

## 1. Namen

Ta dokument definira formalno validacijo izvršitvenega grafa Kernel Layer 0, kot je definiran s TRANSITIONS.

Cilj:
- formalno dokazati, da je Layer 0 execution-complete in graph-consistent
- brez sprememb execution logike
- deterministična, statična validacija primerna za CI

## 2. Ciljni artefakti

- governance/kernel/KERNEL_EXECUTION_GRAPH_VALIDATION_v1.0.md (ta dokument)
- scripts/kernel_execution_graph_check.py (enforcement; CI-safe; stdlib only)

## 3. Kanonični model

TRANSITIONS je definiran kot:

- TRANSITIONS: Dict[Tuple[str, str], str]
- ključ: (current_state: str, event_type: str)
- vrednost: next_state: str

To definira usmerjen označen graf:

- Vozlišča (states) = množica stanj
- Robovi (edges) = množica prehodov (from_state, event_type, to_state)

## 4. Governance režim: C (Popolna deklaracija stanj)

V režimu C mora biti state space eksplicitno deklariran.

Normativna zahteva:

- modul `sapianta_hoi.runtime_stub.transitions` MORA izvoziti:

  - ALL_STATES: set[str]  (ali frozenset[str]) — kanonični seznam vseh stanj
  - TRANSITIONS: Dict[Tuple[str, str], str]

Optional (priporočeno, ne obvezno):
  - INITIAL_STATE: str (če ni prisotno, validator uporabi "INITIAL")

Razlaga:
- ALL_STATES je formalni register stanj.
- Nobeno stanje ne sme nastati implicitno zgolj kot next_state.

## 5. Validacijska pravila (MUST)

### 5.1 Closure (zaprtost)
Za vsak prehod:
  (s, e) -> t

MORA veljati:
- s ∈ ALL_STATES
- t ∈ ALL_STATES

Če katerikoli s ali t ni v ALL_STATES → FAIL.

### 5.2 Determinism (determinističnost)
Za vsak par (s, e) obstaja natanko en t.

Ker je TRANSITIONS slovar, je osnovna determinističnost implicitna, vendar validator dodatno preveri:
- ključi so natančno 2-tuple (str, str)
- vrednosti so str
- ni neveljavnih tipov (npr. None, dict, list)

### 5.3 Reachability (dosegljivost)
Naj bo I = INITIAL_STATE (ali "INITIAL" fallback).

Naj bo R množica stanj dosegljivih iz I z BFS/DFS.

MORA veljati:
- R == ALL_STATES

Če obstaja stanje v ALL_STATES, ki ni dosegljivo → FAIL.

### 5.4 Dead-end states (končna / slepa stanja)
Dead-end = stanje brez izhodnih prehodov (ne pojavi se kot current_state v nobenem ključu).

V režimu C so dead-end stanja dovoljena (terminali), vendar:
- Vsa dead-end stanja morajo biti dosegljiva (že pokrito v 5.3)
- Ne smejo obstajati “naključni terminali”, ki niso v ALL_STATES (pokrito v 5.1)

Validator dead-end stanja vedno izpiše v poročilu (stdout), ne glede na PASS/FAIL.

### 5.5 Non-divergence / Cycles (necikličnost)
Privzeta politika: cikli NISO dovoljeni, razen če so eksplicitno dovoljeni.

Ker je Layer 0 determinističen, cikli pomenijo potencialno neskončne zanke v stanju.

Privzeto MUST:
- noben self-loop (s -> s) ni dovoljen
- noben multi-node cikel ni dovoljen

Optional (če se kasneje uvede):
- ALLOWED_CYCLES: set[tuple[str, ...]] ali druga governance deklaracija
  (ni del v1.0)

Če validator zazna cikel → FAIL.

### 5.6 Orphan events (dogodki brez definicije)
Orphan event je dogodek, ki obstaja v “event space”, vendar nima prehoda iz določenih stanj.

Ker v Layer 0 ni obveznega globalnega EVENT registry, v1.0 definira minimalno:
- EVENT_SET = množica vseh event_type, ki se pojavijo v TRANSITIONS ključih.
- za vsak event ∈ EVENT_SET:
  - mora obstajati vsaj en prehod (to je trivialno res, ker je v setu)
- validator dodatno izpiše poročilo:
  - katere evente imamo
  - v katerih stanjih so uporabljeni

Strožji “event coverage” (da mora vsak event biti definiran v vseh stanjih) NI del v1.0,
ker bi to zahtevalo dodatno governance odločitev.

## 6. Izhodi in CI režim

Enforcement skripta:
- PASS: exit code 0
- FAIL: exit code 1 (ali specifični code; glej 6.1)

### 6.1 Klasifikacija napak (stdout + exit code 1)
Validator izpiše:
- seznam kršitev po kategoriji
- deterministično urejeno (sortirano)

## 7. Ne-cilji (out of scope)
- runtime simulacija
- izvajanje guardov
- spremembe execution logike
- redesign arhitekture
- zunanji dependency-ji

## 8. Referenca implementacije
- scripts/kernel_execution_graph_check.py

