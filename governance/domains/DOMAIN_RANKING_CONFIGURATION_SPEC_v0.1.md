# DOMAIN_RANKING_CONFIGURATION_SPEC_v0.1

## STATUS
ACTIVE

## LAYER
DOMAIN_GOVERNANCE

## TYPE
RANKING_CONFIGURATION_SPECIFICATION

## VERSION
0.1

---

# 1. PURPOSE

Ta dokument formalizira strukturo in pravila Domain Ranking Configuration artefaktov.

Ranking Configuration določa, kako se kandidati (artefakti), generirani znotraj Execution Architecture,
deterministično ocenijo in rangirajo.

Ranking je normativna domenska odločitev.

Execution Engine izvaja formulo, vendar ne določa metrike ali uteži.

---

# 2. ONTOLOGICAL POSITION

Ranking Configuration je:

- Domain Governance artefakt
- hash-bound
- versioned
- replay-verifiable
- Promotion Gate nadzorovan

Sprememba ranking konfiguracije je normativna sprememba.

LLM nima vpliva na ranking konfiguracijo.

---

# 3. GLOBAL RANKING INVARIANTS

Vsaka Domain Ranking Configuration mora spoštovati:

1. Determinism Invariance  
   Score mora biti popolnoma determinističen.

2. Replay Invariance  
   Score mora biti reproducibilen iz:
   - Governance Snapshot hash
   - Ranking Configuration verzije
   - Candidate artefakta

3. No Runtime Dependency  
   Ranking ne sme uporabljati runtime podatkov.

4. No LLM Dependency  
   Ranking ne sme klicati modelov.

5. Hash-Bound Formula  
   Ranking formula mora biti del hash-bound artefakta.

---

# 4. STRUCTURE OF DOMAIN RANKING CONFIGURATION

Vsaka domena mora definirati:

## 4.1 Metric Set

Strukturiran seznam metrik.

Primer:

- scope_compliance
- threshold_margin
- dependency_safety
- minimal_change_penalty
- drift_alignment

Vsaka metrika mora biti:

- formalno definirana
- izračunljiva
- deterministična

---

## 4.2 Weight Vector

Vsaka metrika ima utež:

w_i ∈ ℝ

Uteži morajo biti:

- numerične
- eksplicitno zapisane
- verzionirane
- hash-bound

Implicitne uteži niso dovoljene.

---

## 4.3 Penalty Rules

Domena lahko definira penalizacijska pravila:

- kršitev scope → diskvalifikacija
- dependency break → hard reject
- threshold breach → negative weight

Penalty pravila morajo biti deterministična.

---

## 4.4 Normalization Rule

Domena mora definirati:

- ali se score normalizira
- kako se normalizira
- ali obstajajo hard-threshold cutoffs

---

# 5. SCORING FUNCTION MODEL

Standardna oblika:

score(candidate) = Σ (w_i * metric_i(candidate)) − penalties

Execution Architecture izvaja to funkcijo.

Struktura formule je globalno določena.
Metrike in uteži so domensko specifične.

---

# 6. TIE-BREAKING RULE

Domena mora definirati deterministični tie-break:

Primer:

1. višji threshold_margin
2. manjši change_footprint
3. nižji dependency_depth
4. deterministični lexicographic fallback

Tie-break mora biti popolnoma determinističen.

---

# 7. SCOPE INTERACTION

Ranking mora spoštovati aktivni Scope Engine.

Če kandidat preseže aktivni scope:

- kandidat je diskvalificiran
ali
- kandidat prejme absolutno penalizacijo

Scope eskalacija ni dovoljena brez governance override.

---

# 8. THRESHOLD INTERACTION

Ranking mora biti kompatibilen z Domain ThresholdPolicy.

Ranking ne sme preglasiti threshold discipline.

Threshold je ločen normativni mehanizem.

---

# 9. VERSIONING AND CHANGE CONTROL

Sprememba ranking konfiguracije zahteva:

- nov version number
- hash-bound zapis
- Promotion Gate klasifikacijo
- Authority approval (če zahteva)

Spremembe uteži so normativne spremembe.

---

# 10. META-INVARIANT

Ranking Configuration ne sme:

- redefinirati constitutional invariant
- redefinirati Scope Engine
- redefinirati Authority model
- uvesti runtime odvisnosti
- vključiti LLM-based ocenjevanja

Ranking Configuration je domenski optimizacijski artefakt,
ne evolucijski mehanizem.

---

END OF DOCUMENT