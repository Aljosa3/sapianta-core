# STRATEGY_EVOLUTION_FRAMEWORK_v0.1

STATUS
ACTIVE

LAYER
DOMAIN_GOVERNANCE

DOMAIN
TRADING

TYPE
EVOLUTION_FRAMEWORK

VERSION
0.1

---

# 1 PURPOSE

Ta dokument definira okvir za evolucijo strategij
v determinističnem raziskovalnem sistemu.

Strategije se obravnavajo kot:

versioned research artifacts

in ne kot statične implementacije.

---

# 2 CORE PRINCIPLE

Sistem obravnava vsako trgovalno odločitev kot
reproducibilen eksperiment.

Vsaka odločitev je zapisana kot:

DecisionEnvelope

ki vsebuje:

market snapshot
indicator state
strategy policy hash
execution engine version
decision result

---

# 3 STRATEGY GENOME

Strategija je definirana kot skupek parametrov
in pravil.

Primer genome:

RSI threshold
position size rule
volatility filter
risk constraints

Genome določa identiteto strategije.

---

# 4 STRATEGY VERSIONING

Vsaka sprememba strategije ustvari novo verzijo.

Primer:

strategy_v1
strategy_v2
strategy_v3

Trades so vedno vezani na policy hash.

---

# 5 STRATEGY PHYLOGENY

Sistem vodi rodovnik strategij.

Primer:

strategy_A
strategy_A1
strategy_A2

To omogoča analizo evolucije strategij.

---

# 6 STRATEGY GRAVEYARD

Strategije, ki ne prestanejo robustness kriterijev,
se arhivirajo kot zavrnjene.

Graveyard preprečuje ponovno generiranje
identičnih neuspešnih strategij.

---

# 7 STRATEGY ECOSYSTEM

Portfelj lahko vsebuje več strategij.

Primer:

trend following
mean reversion
volatility breakout

Strategije lahko koeksistirajo.

---

# 8 POPULATION CONTROL

Sistem omejuje velikost populacije strategij.

Primer:

max_active_strategies = 20
max_research_strategies = 500

Slabše strategije se odstranijo.

---

# 9 GOVERNANCE PROMOTION

Strategija mora prestati:

robustness evaluation
governance approval

šele nato lahko vstopi v execution.

---

# 10 OBJECTIVE

Cilj sistema ni maksimiranje kratkoročnega profita,
ampak razvoj robustnih strategij.

optimize:

robustness(strategy)

in ne:

profit(strategy)

---

END OF DOCUMENT