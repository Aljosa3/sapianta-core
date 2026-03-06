# WORLD_STATE_SCHEMA_v0.1

STATUS
ACTIVE

LAYER
L4_GLOBAL_CONTEXT_LAYER

TYPE
WORLD_STATE_SCHEMA

VERSION
0.1

---

# 1 PURPOSE

World State definira skupni opis globalnega
konteksta, ki ga uporabljajo vse domene
sistema SAPIANTA.

World State omogoča:

- skupni kontekst odločanja
- deterministični replay
- konsistentno interpretacijo sveta
- skupni imenovalec med domenami

Domene lahko World State berejo,
ne smejo ga spreminjati.

---

# 2 WORLD STATE PRINCIPLE

World State je:

- snapshot sveta
- hash-bound artifact
- verzioniran
- replay-verificiran

World State ne vsebuje domain logic.

---

# 3 STRUCTURE

World State vsebuje več kontekstnih modulov.

---

# 3.1 MACROECONOMIC STATE

Opis makroekonomskega okolja.

fields

inflation_regime  
interest_rate_regime  
growth_regime  
employment_regime  

example

inflation_regime = HIGH  
interest_rate_regime = RISING  
growth_regime = WEAK  
employment_regime = STABLE  

---

# 3.2 FINANCIAL CONDITIONS

Opis finančnega okolja.

fields

liquidity_regime  
credit_spread_regime  
market_volatility_regime  
funding_conditions  

example

liquidity_regime = TIGHT  
market_volatility_regime = HIGH  
credit_spread_regime = WIDENING  

---

# 3.3 GEOPOLITICAL STATE

Opis globalnih političnih tveganj.

fields

geopolitical_risk_level  
war_conflict_state  
sanctions_environment  
energy_security_state  

example

geopolitical_risk_level = ELEVATED  
war_conflict_state = ACTIVE_CONFLICT  
energy_security_state = STRESSED  

---

# 3.4 SOVEREIGN RISK STATE

Opis stabilnosti državnih financ.

fields

sovereign_debt_stress  
fiscal_stability  
currency_stability  

example

sovereign_debt_stress = MODERATE  
currency_stability = STABLE  

---

# 3.5 GLOBAL MARKET REGIME

Opis splošnega režima finančnih trgov.

fields

trend_regime  
volatility_regime  
correlation_regime  

example

trend_regime = TRENDING  
volatility_regime = HIGH  
correlation_regime = ELEVATED  

---

# 4 SNAPSHOT DISCIPLINE

World State se generira kot snapshot.

fields

world_state_id  
world_state_hash  
timestamp  
data_source_reference  

Snapshot mora omogočati:

deterministični replay odločitev.

---

# 5 WORLD STATE DELIVERY

World State se posreduje domenam preko
Domain Orchestration Layer.

Flow

World State Snapshot
        ↓
Domain Orchestrator
        ↓
Domain Execution

Vse domene v eni odločitvi morajo
uporabljati isti World State snapshot.

Domain Orchestrator ne sme spreminjati
World State artefakta.

---

# 6 DOMAIN INTERPRETATION

Domene interpretirajo World State
glede na svoje potrebe.

Example

Trading Domain

HIGH inflation → prefer trend strategies  
HIGH volatility → increase risk penalty  

Credit Domain

HIGH interest rates → increase default probability  

Risk Domain

HIGH geopolitical risk → increase systemic risk score  

---

# 7 GOVERNANCE

Spremembe World State strukture
so klasificirane kot

STRUCTURAL_CONTEXT_CHANGE

in zahtevajo

MetaAuthority approval.

---

# 8 META INVARIANTS

World State

- ne sme spreminjati execution pipeline
- ne sme neposredno spreminjati odločitev
- ne sme bypassati Domain Governance

World State je samo kontekstni model.

---

END OF DOCUMENT