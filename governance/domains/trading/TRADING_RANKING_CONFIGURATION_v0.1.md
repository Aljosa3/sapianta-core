# TRADING_RANKING_CONFIGURATION_v0.1

## STATUS
ACTIVE

## LAYER
DOMAIN_GOVERNANCE

## TYPE
TRADING_RANKING_CONFIGURATION

## VERSION
0.1

---

# 1. SCOPE

Domain: CRYPTO_SPOT  
Exchange: Kraken  
Assets: BTC, ETH, SOL  
Timeframe: 1H  
Execution Mode: Rolling Simulation  

---

# 2. ACTIVATION MODEL

## 2.1 Portfolio Activation Mode

activation_mode = VOLATILITY_DEPENDENT

Modes:
- SINGLE_BEST
- MULTI_ALLOCATION

---

## 2.2 Volatility Regime Mode

volatility_regime_mode = PER_ASSET

volatility_percentile_thresholds:
- low_high_boundary = 40
- mid_high_boundary = 70

volatility_horizon_mapping:
- LOW  -> 24 hours
- MID  -> 12 hours
- HIGH -> 6 hours

---

# 3. EDGE MODEL

Edge predstavlja risk-adjusted empirical expectancy.

## 3.1 Risk Model

stop_multiplier:
  BTC: 1.8
  ETH: 2.0
  SOL: 2.5

R_multiple:
  BTC: 2.5
  ETH: 2.8
  SOL: 3.2

risk_unit(asset, t) =
    ATR(asset, t) * stop_multiplier(asset)

target_distance =
    risk_unit * R_multiple(asset)

---

## 3.2 Empirical Expectancy

projected_move(asset, signal_type, regime_bucket) =
    weighted_estimators(asset, signal_type, regime_bucket)

---

## 3.3 Estimator Weights

estimators:
  E1: median_forward_return
  E2: trimmed_mean_forward_return
  E3: regime_conditioned_return

estimator_weights:
  E1: 0.4
  E2: 0.3
  E3: 0.3

min_sample_size_per_bucket: 30
fallback_policy: NO_TRADE

---

## 3.4 Edge Formula

raw_edge =
    projected_move / risk_unit

edge_score =
    (raw_edge * 0.6)
  - (volatility_penalty * 0.2)
  - (correlation_penalty * 0.2)

min_edge_threshold: 0.1

---

# 4. ALLOCATION MODEL

allocation_method = PROPORTIONAL_TO_EDGE

allocation_i =
    edge_score_i / sum(edge_score_positive)

min_position_floor: 0.05
max_position_cap: 0.40

max_portfolio_exposure: 1.0
max_asset_exposure: 0.50

---

# 5. POSITION EXIT MODEL

exit_type = STOP_TARGET_ONLY

stop_distance =
    ATR(asset, t_entry) * stop_multiplier(asset)

target_distance =
    stop_distance * R_multiple(asset)

Stops and targets are fixed at entry.
No trailing stop in v0.1.

---

# 6. EVOLUTION POLICY BOUNDARY

Allowed:
- stop_multiplier adjustment
- R_multiple adjustment
- estimator_weights adjustment
- volatility threshold adjustment
- horizon mapping adjustment

Not allowed:
- formula change
- new estimator addition
- trailing stop introduction

Structural change requires STRUCTURAL_DOMAIN_CHANGE regime.

---

END OF DOCUMENT