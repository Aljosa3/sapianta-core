# SELF-BUILD CLOSURE PATCH PLAN
## (Closure #1–#5 · minimalni operativni posegi)

Status: DRAFT  
Namen: Zapreti manjkajoče tehnične vezi za samogradnjo modulov  
Obseg: Izključno obstoječe komponente  
Prepovedano: nova arhitektura, nove faze, refaktor

---

## Closure #1 — Interpretation ↔ Materialization (Format Enforcement)

**Problem**
Claude vrača JSON output, RawModuleWriter zahteva FILE: marker format.

**Cilj**
Zagotoviti determinističen, strojno berljiv output za materializacijo.

**Poseg**
Izvesti ENEGA od naslednjih dveh (ne obeh):
1. Zaostriti prompt v `PromptRenderer`, da zahteva izključno:

FILE: <path>
<content>
2. Dodati tanek adapter:
- vhod: Claude JSON output
- izhod: FILE-marker struktura

**Datoteke (orientacijsko)**
- sapianta_chat/execution/prompt_renderer.py
- runtime/raw_module_writer.py

FILE: modules/example/__init__.py
# empty

FILE: modules/example/main.py
def run():
    pass


---

## Closure #2 — Human Approval Gate (HALT)

**Problem**
Build pipeline nima STOP točke pred zapisom.

**Cilj**
Zagotoviti, da noben zapis ne steče brez izrecne človeške potrditve.

**Poseg**
V `build_flow.py` vstaviti HALT točko:
- po uspešnem Claude outputu
- pred `RawModuleWriter.write_from_raw()`

HALT (blocking approval gate) mora:
- prikazati seznam FILE-paths
- zahtevati APPROVE / REJECT
- ob REJECT takoj prekiniti tok

**Datoteke**
- sapianta_chat/cli/build_flow.py

---

## Closure #3 — Guard Wiring

**Problem**
`mechanical_guard_v0_64` obstaja, vendar ni nikoli klican.

**Cilj**
Aktivirati guard kot dejanski varnostni mehanizem.

**Poseg**
V `build_flow.py` dodati klic:
- `GUARD.check_self_build(context)`
- pred vsako materializacijo
- pred uporabo self-build artefakta za loop-back

Ob DENY:
- tok se prekine
- brez zapisa

**Datoteke**
- governance/runtime/mechanical_guard_v0_64.py
- sapianta_chat/cli/build_flow.py

---

## Closure #4 — Self-Referential Loop-Back (ENKRAT)

**Problem**
`controlled_self_build_v0_65` generira inertni artifact, ki se nikoli ne uporabi.

**Cilj**
Omogočiti enkratno povratno zanko samogradnje.

**Poseg**
Po uspešni validaciji:
- artifact iz `controlled_self_build_v0_65`
se ponudi kot naslednji `build_plan`
- brez avtomatske ponovitve
- brez rekurzije

Loop-back je:
- ekspliciten
- enkraten
- ročno potrjen

**Datoteke**
- governance/runtime/controlled_self_build_v0_65.py
- sapianta_chat/cli/build_flow.py

---

## Closure #5 — Module Builder Activation

**Problem**
`module_builder.py` je stub in ni vključen v dejanski tok.

**Cilj**
Builder postane koordinator, ne generator kode.

**Poseg**
`module_builder.prepare_build_task()`:
- prebere build_plan
- razdeli nalogo na:
- interpretacijo
- materializacijo
- validacijo
- ne generira kode

Povezava:
builder → executor → writer → validator

**Datoteke**
- runtime/module_builder.py
- sapianta_chat/cli/build_flow.py

---

## Končni učinek

Po izvedbi vseh zgornjih posegov:

- SAPIANTA ZMORE samogradnjo modulov
- Samogradnja je nadzorovana (HALT + Guard)
- Zapis je izoliran in sledljiv
- v0.50–v0.65 dobijo operativni pomen
- Ni potrebna nobena nova faza

---

## Opomba

Ta dokument:
- ni izvršljiv
- ni normativen
- služi kot tehnični checklist za implementacijo

Vsak poseg se lahko implementira in testira ločeno.

