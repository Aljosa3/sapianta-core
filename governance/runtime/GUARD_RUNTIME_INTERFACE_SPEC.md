# GUARD ↔ RUNTIME INTERFACE SPEC
## Design-Only — v0.5

## Status
DESIGN-ONLY  
Ta dokument ne uvaja kode, izvajanja ali tehničnih mehanizmov.

---

## 1. NAMEN DOKUMENTA

Ta dokument določa **konceptualni vmesnik** med:
- **Guard Lifecycle** (odločitvena avtoriteta) in
- **Runtime slojem** (nadzorovan prehodni sloj).

Cilj je:
- jasno razmejiti odgovornosti,
- določiti dovoljene signale in tokove,
- preprečiti implicitne ali dvoumne prehode v izvajanje.

Dokument:
- NE opisuje implementacije,
- NE definira API-jev,
- NE dovoljuje executiona.

---

## 2. TEMELJNA NAČELA

1. **Enosmerna avtoriteta**  
   Guard odloča. Runtime ne odloča.

2. **Brez stranskih učinkov**  
   Guard ne ustvarja stanja v runtime-u; runtime ne spreminja Guard stanja.

3. **Eksplicitnost**  
   Vsak prehod je izrecen, sledljiv in preverljiv.

4. **SCF skladnost**  
   Vsi signali in tokovi so skladni s SCF-03, SCF-04 in SCF-05.

---

## 3. VLOGE IN ODGOVORNOSTI

### 3.1 Guard Lifecycle
- Presoja skladnost zahtev s SCF.
- Uporablja Interaction Registry kot omejitveni okvir.
- Izdaja **odločitev**: ALLOW / DENY / HOLD.
- Ne izvaja dejanj in ne orkestrira modulov.

### 3.2 Runtime
- Sprejema **odločitev Guard-a** kot vhod.
- Ne interpretira pravil in ne spreminja odločitev.
- Ne prečka Execution Boundary brez eksplicitne avtorizacije (SCF-04).

---

## 4. DOVOLJENI SIGNALI (CONCEPTUAL)

Guard lahko runtime-u posreduje izključno naslednje **konceptualne signale**:

### 4.1 DECISION: ALLOW
- Pomeni, da je zahteva **normativno dopustna**.
- V v0.5:
  - NE sproži izvajanja,
  - NE prečka Admission Gate.

### 4.2 DECISION: DENY
- Pomeni kršitev SCF pravil.
- Runtime:
  - ustavi tok,
  - ne izvaja stranskih učinkov.

### 4.3 DECISION: HOLD
- Pomeni nepopolno ali nedoločljivo zahtevo.
- Runtime:
  - začasno ustavi tok,
  - ne izvaja dejanj.

Runtime ne sme generirati novih odločitev.

---

## 5. DOVOLJENI TOKOVI (DESIGN-LEVEL)

Edini dovoljen konceptualni tok:
Intent
→ Guard Evaluation
→ Decision (ALLOW / DENY / HOLD)
→ Runtime Admission Gate
→ (STOP v v0.5)


V v0.5 se tok **vedno zaključi pred izvajanjem**.

---

## 6. PREPOVEDANI TOKOVI

Izrecno prepovedano je:

- runtime, ki zahteva ponovno presojo Guard-a,
- runtime, ki interpretira ali razširja odločitev,
- Guard, ki sproža ali nadzira izvajanje,
- kakršenkoli implicitni prehod čez Execution Boundary.

Vsaka zaznava pomeni:
> **kršitev fazne discipline.**

---

## 7. SLEDLJIVOST IN AUDIT

Vsaka interakcija Guard ↔ Runtime mora biti:
- povezana z identiteto zahteve,
- povezana z Guard odločitvijo,
- zabeležena za retrospektivo.

Runtime brez audit sledi:
> ni dovoljen.

---

## 8. RAZMERJE DO INTERACTION REGISTRYJA

- Guard uporablja Interaction Registry pri presoji.
- Runtime Registryja:
  - ne bere,
  - ne spreminja,
  - ne interpretira.

Registry nikoli ni del runtime tokov.

---

## 9. IZRECNE PREPOVEDI (v0.5)

V fazi v0.5 je prepovedano:
- implementirati Guard ↔ Runtime vmesnik kot kodo,
- testirati signale ali tokove,
- dodajati runtime logiko v Guard,
- obratna avtoriteta (runtime → Guard).

---

## 10. ZAKLJUČNA VLOGA DOKUMENTA

Ta dokument:
- zapira zasnovo Guard ↔ Runtime odnosa,
- odstrani vse dvoumnosti o odgovornostih,
- je obvezen del **zaključka faze v0.5**.

Implementacija je dovoljena šele po:
- v0.5 COMPLETE,
- formalnem prehodu v v0.6.

---

## KONEC DOKUMENTA

