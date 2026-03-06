# PROMOTION_GATE_SPEC_v0.3

STATUS
ACTIVE

TYPE
GOVERNANCE_SPEC

LAYER
L3_DOMAIN_GOVERNANCE

VERSION
0.3

---

# 1 PURPOSE

Promotion Gate definira postopek,
po katerem eksperimentalni modeli
postanejo produkcijski modeli.

Gate zagotavlja:

- stabilnost sistema
- kontrolirano evolucijo
- minimalni blast radius sprememb.

---

# 2 CORE PRINCIPLE

Eksperimentalni modeli ne smejo
neposredno v produkcijski execution.

Vsaka sprememba mora prestati
Promotion Gate.

Flow

Experiment
    ↓
Evaluation
    ↓
Promotion Gate
    ↓
Production Deployment

---

# 3 CHANGE CLASSIFICATION

Promotion Gate klasificira spremembe
glede na njihov blast radius.

Classes

COSMETIC
PARAMETRIC
STRUCTURAL

---

# 4 COSMETIC CHANGE

Opis

Sprememba brez vpliva
na decision logic.

Primeri

logging
documentation
vizualizacija

Approval

automatic.

---

# 5 PARAMETRIC CHANGE

Opis

Sprememba parametrov
znotraj obstoječega modela.

Primeri

RSI threshold
position sizing
risk penalty factor

Zahteve

experiment replay
performance comparison
robustness evaluation

Approval

domain governance.

---

# 6 STRUCTURAL CHANGE

Opis

Sprememba strukture
odločitvenega sistema.

Primeri

nov domain
sprememba orchestration
sprememba decision artifact

Zahteve

full system replay
governance review
MetaAuthority approval.

---

# 7 BLAST RADIUS MODEL

Blast radius določa
obseg vpliva spremembe.

Levels

FILE_SCOPE
MODULE_SCOPE
DOMAIN_SCOPE
SYSTEM_SCOPE

Spremembe z večjim
blast radius zahtevajo
strožjo odobritev.

---

# 8 PROMOTION CRITERIA

Promotion Gate preveri:

experiment reproducibility
statistical improvement
risk neutrality
governance compliance.

Če kriteriji niso izpolnjeni:

promotion denied.

---

# 9 REPLAY REQUIREMENT

Promotion zahteva
deterministični replay.

Minimalni replay level

RAL2.

Kritični sistemi lahko zahtevajo

RAL3.

---

# 10 GOVERNANCE APPROVAL

Approval levels

COSMETIC → automatic
PARAMETRIC → domain governance
STRUCTURAL → MetaAuthority.

---

# 11 FAIL SAFE

Če Promotion Gate zazna:

- replay failure
- governance violation
- povečanje sistemskega tveganja

se deployment zavrne.

---

# 12 META INVARIANTS

Promotion Gate ne sme:

- bypassati governance
- spreminjati execution layer
- spreminjati world state.

Promotion Gate nadzira
evolucijo sistema.

---

END OF DOCUMENT