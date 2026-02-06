# ARTIFACT_ONLY_SELF_BUILD_v0.60_INIT

STATUS: INIT  
PHASE: v0.60  
SCOPE: Artifact-Only Self-Build (First Write)  
MUTABILITY: MUTABLE  
NORMATIVE STATUS: NON-NORMATIVE  

## DEPENDENCIES
- v0.50 — Self-Build Preconditions (LOCKED)
- v0.55 — Explicit Human Approval (INIT)
- v0.56 — Execution Gating (INIT)
- v0.57 — Explicit Execution Authorization (INIT)
- v0.58 — Execution Handshake (No-Op) (INIT)
- v0.59 — Execution Simulation / Reversible Execution (INIT)

## EXPLICIT NON-DEPENDENCIES
- runtime execution
- runtime binding
- persistent state mutation
- external side-effects
- automation
- enforcement mechanisms

---

## 1. NAMEN DOKUMENTA

Ta dokument definira fazo **Artifact-Only Self-Build (First Write)** kot prvo
dovoljeno obliko samogradnje, omejeno izključno na **pisanje pasivnih artefaktov**
v governance prostor, brez kakršnegakoli vpliva na runtime ali izvedbo.

Namen faze v0.60 je:
- prvič dovoliti **WRITE** v okviru samogradnje,
- strogo omejiti WRITE na **neizvršljive artefakte**,
- ohraniti popolno ločitev med zapisom, aktivacijo in uporabo.

---

## 2. DEFINICIJA “ARTIFACT-ONLY WRITE”

Artifact-only write pomeni:
- zapis **predloga**, **osnutka**, **razlike (diff)** ali **utemeljitve**,
- zapis v **governance prostor**,
- brez vključitve v runtime ali execution tok.

Takšen WRITE:
- ne spremeni vedenja sistema,
- ne spremeni aktivne kode,
- ne vpliva na odločanje ali simulacijo.

---

## 3. DOVOLJENI ARTEFAKTI

V fazi v0.60 so dovoljeni naslednji artefakti:
- predlogi sprememb obstoječih modulov,
- osnutki novih modulov,
- diffs obstoječih artefaktov,
- utemeljitve, razlogi in analize vpliva.

Vsak artefakt mora biti:
- pasiven,
- neizvršljiv,
- ločen od runtime okolja,
- auditabilen.

---

## 4. POLOŽAJ V TOKU SAMOGRADNJE

Faza v0.60 predstavlja:
- **vstopno točko samogradnje**,
- brez implicitnega nadaljevanja,
- brez avtomatske eskalacije v binding ali execution.

Samogradnja v tej fazi:
- ustvarja,
- ne uporablja,
- ne aktivira.

---

## 5. STROGO PREPOVEDANO

V fazi v0.60 je strogo prepovedano:
- zapis v runtime okolje,
- sprememba ali zamenjava aktivne kode,
- avtomatska vključitev artefaktov,
- interpretacija artefaktov kot navodil,
- uporaba WRITE kot signala za nadaljnje faze.

---

## 6. ODNOS DO INTELIGENCE

V tej fazi inteligenca:
- lahko sodeluje pri **ustvarjanju artefaktov**,
- ne sme odločati o njihovi uporabi,
- ne sme sprožiti bindinga ali aktivacije.

Artefakti:
- niso učni signal,
- niso trigger,
- niso povratna zanka.

---

## 7. ODNOS DO ČLOVEKA

Človeški nadzor v v0.60:
- je impliciten,
- ne potrjuje aktivacije,
- ne spreminja statusa artefaktov.

Noben artefakt:
- ne postane aktiven brez ločene, eksplicitne človeške odločitve.

---

## 8. FAILURE SEMANTIKA

Neuspeh zapisa artefakta:
- je lokalen,
- ne vpliva na sistem,
- ne sproži fallback ali retry mehanizmov,
- ne eskalira v druge faze.

---

## 9. AUDIT VIDIK

V audit plasti je obvezno beleženje:
- *artifact write attempted*
- *artifact write completed*

Prepovedano je:
- interpretiranje pomena zapisa,
- vrednotenje kakovosti,
- povezovanje z execution ali readiness logiko.

---

## 10. PHASE BOUNDARY CLAUSE

Faza v0.60:
- omogoča pisanje,
- ne omogoča uporabe,
- ne znižuje praga za execution,
- ne odpira poti za runtime binding.

Vsaka naslednja faza mora:
- eksplicitno nasloviti **binding**, **activation** ali **promotion**,
- biti ločeno potrjena.

---

## 11. ZAKLJUČEK FAZE

Z v0.60 je samogradnja **dejansko začeta** v svoji najvarnejši obliki.

Sistem:
- prvič ustvarja,
- brez kakršnegakoli operativnega učinka,
- pod popolnim nadzorom in sledljivostjo.

Nobena oblika aktivne spremembe sistema v tej fazi ni dovoljena.
