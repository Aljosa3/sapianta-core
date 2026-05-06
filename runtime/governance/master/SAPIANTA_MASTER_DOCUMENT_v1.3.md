🧠 SAPIANTA — UNIFIED MASTER DOCUMENT (v1.3)

(združeni vsi obstoječi viri + zadnji commit)

1. IDENTITETA SISTEMA

SAPIANTA je:

→ governed autonomous development system
→ determinističen
→ self-healing
→ self-improving
→ self-certifying
→ fail-safe

Ključni principi:

brez nenadzorovanih mutacij
popolna replayabilnost
fail-closed model
arhitekturna zaščita enforced

📄 Referenca:
📄 Specifikacija:

2. OSNOVNI PIPELINE (GAD)
IDEA → PLAN → CODEGEN → VALIDATE → TEST → REPAIR → CERTIFY → LEARN → DECIDE

LAST EXTENSION:

👉 DECIDE layer (score-based prioritization) ← NOVO

3. CORE SISTEMI
3.1 DevOrchestrator
centralni execution engine
koordinira celoten pipeline
3.2 TestRunner (STRICT MODE)
subprocess pytest
no silent failure
deterministic output
3.3 AutoFixEngine
multi-strategy repair
function-level patching
FixMemory integracija
3.4 ArchitectureGuardian
FAIL-CLOSED zaščita
blokira:
eval, exec, subprocess
enforce-a:
path integrity
syntax
structure

📄 Validirano:

4. SELF-HEALING → SELF-IMPROVING EVOLUCIJA
FAZA 1: Self-healing
AutoFixEngine stabilen
repair loop determinističen
FAZA 2: Learning (FixMemory)
učenje po error signature
vpliv na StrategySelector

📄
📄

FAZA 3: Adaptive decision (Strategy weighting)
FixMemory vpliva na ranking
prehod:
→ statično → adaptivno odločanje

📄

FAZA 4: CAL loop (closed)
reward / penalize integracija
feedback iz execution

📄

FAZA 5: Autonomous generation
sistem generira naslednje naloge
success → extend
failure → improve

📄

FAZA 6: Signature-aware evolution
error-based task targeting
fix_TypeError_, fix_NameError_ …

📄

FAZA 7: CAL ↔ FixMemory loop closure
failure frequency vpliva na prioriteto
feedback amplification loop

📄

FAZA 8: Learning Measurement Layer
repair_iterations tracking
measurable learning

📄

5. 🔥 NOVO: DECISION LAYER (SCORE-BASED PRIORITIZATION)
Commit:
[CORE] Score-based task prioritization (CAL → decision layer)
IMPLEMENTACIJA
pop_next_task() uporablja:
metadata.score
sortiranje:
descending (highest score first)
stabilen sort:
→ ohranja vrstni red za enake score
OBNAŠANJE

PREJ:

task selection = FIFO / priority-only

ZDAJ:

task selection = priority + score (learning-driven)
POMEN

To je ključni prehod sistema:

PREJ:
CAL = opazovalec (scoring)
ZDAJ:
CAL = odločevalec (decision engine)
ARHITEKTURNI PREHOD
learning → decision → behavior

To pomeni:

👉 sistem NE samo uči
👉 ampak spreminja svoje obnašanje

IMPACT
prvi pravi decision layer
omogoča:
prioritizacijo učenja
fokus na uspešne smeri
izogibanje neuspešnim

👉 to je začetek “inteligence” sistema

VARNOST
brez spremembe strukture
determinističen sort
STRICT TEST MODE nedotaknjen

VALIDACIJA:

pytest: 159 passed, 1 skipped
6. CCS (CERTIFICATION SYSTEM)
CERTIFIED / REJECTED artifacts
noben nevalidiran code ne teče

📄

7. LLM LAYER (SAFE)
centraliziran preko LLMInterface
mock-first
fallback always

📄

Observability
LLMUsageTracker

📄

8. STABILNOST SISTEMA

Ključni milestone-i:

✅ 153/153 passing

📄

✅ 160/160 passing
CAL + CCS + FixMemory stabilni
9. TRENUTNO STANJE

SAPIANTA je:

✔ deterministic
✔ self-healing
✔ self-learning
✔ self-certifying
✔ decision-enabled (NEW)
10. KLJUČNA UGOTOVITEV

Z zadnjim commitom:

👉 sistem prvič doseže:

LEARNING → DECISION → EXECUTION LOOP

To je:

👉 prvi pravi “brain layer”

11. KAJ ŠE MANJKA DO “EXPLOSION”

Trenutno imaš:

✔ learning
✔ decision
✔ execution
✔ feedback

Manjka:

❗ global optimization pressure

To pomeni:

več vzporednih poti
konkurenca med strategijami
resource allocation

12. NASLEDNJI KORAK (KLJUČEN)

👉 Decision Spine (global orchestrator)

Zakaj:

score zdaj vpliva lokalno (task)
mora začeti vplivati globalno:
katere ideje sploh obstajajo
kateri branchi živijo ali umrejo

🚀 IDEJE / PRILOŽNOSTI
Runaway growth trigger
kombinacija:
score prioritization
autonomous generation
FixMemory feedback
→ vodi v samo-pospeševanje
AI kot optimizer (ne generator)
LLM lahko optimizira:
strategije
scoring
task creation
Multi-agent CAL
več paralelnih CAL “tokov”
tekmovanje med njimi
Trading integracija
sistem že ima:
decision layer
feedback loop
→ idealno za real-time decision system