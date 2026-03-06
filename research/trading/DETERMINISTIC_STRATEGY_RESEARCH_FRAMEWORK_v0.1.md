# DETERMINISTIC_STRATEGY_RESEARCH_FRAMEWORK_v0.1

## STATUS
RESEARCH_REFERENCE

## DOMAIN
TRADING

## PURPOSE

Ta dokument povzema ključne koncepte za razvoj
avtonomnega trading sistema v okviru arhitekture SAPIANTA.

Cilj je zagotoviti, da se razvoj strategij izvaja
kot deterministični, reproducibilni raziskovalni proces.

Dokument ni governance artefakt.
Je konceptualna referenca za razvoj Trading domene.

---

# 1. CORE PRINCIPLE

Razvoj avtonomnega trading sistema mora ločiti dve ravni:

- signal quality
- decision integrity

Signal quality pomeni kakovost trgovalne strategije.

Decision integrity pomeni,
da je vsaka odločitev deterministična
in reproducibilna.

Sistem mora omogočiti,
da je vsaka trgovalna odločitev
reproducibilen artefakt.

---

# 2. DECISION ARTIFACT MODEL

Vsaka trgovalna odločitev se zapiše kot:

DecisionEnvelope

Artifact vsebuje:

- market snapshot
- indikatorje
- policy version (policy hash)
- execution engine version
- decision output

Tak zapis omogoča:

- replay odločitev
- forenzično analizo
- audit sled.

---

# 3. STRATEGY VERSIONING

Strategije so verzionirani objekti.

Primer:

policy_v1 → policy_v2 → policy_v3

Vsak trade vsebuje referenco
na policy hash.

To omogoča:

- primerjavo strategij
- sledljiv razvoj.

---

# 4. STRATEGY DIFF

Spremembe strategij se analizirajo kot diff.

Primer:

RSI threshold: 30 → 35  
position size: 2% → 1.5%  
volatility filter: added

To omogoča razumevanje,
katere spremembe so vplivale
na performanso.

---

# 5. DECISION REPLAY

Decision replay omogoča
ponovno izvedbo posamezne odločitve.

Replay pipeline:

1 market input  
2 indikatorji  
3 signal pravila  
4 risk pravila  
5 končna odločitev  

To omogoča forenzično analizo
posameznega trade-a.

---

# 6. COUNTERFACTUAL REPLAY

Counterfactual replay pomeni,
da se odločitev ponovi
z modificiranim parametrom.

Primer:

original: RSI threshold = 35  
counterfactual: RSI threshold = 30

To omogoča analizo
občutljivosti strategije.

---

# 7. PARAMETER LANDSCAPE

Parameter landscape prikazuje
performanso strategije
glede na parametre.

Vizualizacija pokaže:

parameter plateau  
random spike

Robustne strategije imajo
širok parameter plateau.

---

# 8. PARAMETER DRIFT

Parameter drift pomeni,
da se optimalni parametri
spreminjajo skozi čas.

Primer:

2018–2020: RSI optimum ≈ 30  
2020–2022: RSI optimum ≈ 25  
2022–2024: RSI optimum ≈ 35  

Močan drift lahko kaže na:

- nestabilno strategijo
- overfitting.

---

# 9. STRATEGY HALF-LIFE

Strategy half-life pomeni
čas, v katerem strategija izgubi
približno polovico svojega edge-a.

Primer:

Sharpe: 1.6 → 0.8

To kaže,
kako hitro strategija degradira.

---

# 10. IMPLICATION

Avtonomni trading sistem
ne sme optimizirati samo profita.

Optimizirati mora:

- robustnost strategij
- stabilnost parametrov
- odpornost na tržne spremembe.

---

# CONCLUSION

Avtonomni trading sistem
lahko deluje kot:

deterministični raziskovalni laboratorij
za trgovalne strategije.

Vsaka odločitev je:

- reproducibilen eksperiment
- verzioniran artefakt
- analizabilen skozi čas.

Tak pristop omogoča
znanstveni razvoj trading strategij.
