"""
SAPIANTA Regime Strategy Evaluator

Purpose
-------
Evaluate strategies across multiple market regimes to ensure robustness.

This prevents overfitting to a single market scenario.
"""

from runtime.market.market_regime_engine import generate_regime_suite
from runtime.market.market_simulator import generate_price_series, compute_returns

from runtime.evolution.fitness_metrics import compute_performance_metrics
from runtime.evolution.strategy_evaluator import compute_final_fitness


# ---------------------------------------------------------
# STRATEGY RETURNS PER REGIME
# ---------------------------------------------------------

def simulate_strategy_on_returns(strategy, returns):

    action = strategy["action"]["type"]
    position_size = strategy["action"]["quantity"]

    strategy_returns = []

    for r in returns:

        if action == "BUY":

            pnl = r * position_size

        else:

            pnl = -r * position_size

        strategy_returns.append(pnl)

    return strategy_returns


# ---------------------------------------------------------
# REGIME EVALUATION
# ---------------------------------------------------------

def evaluate_strategy_regime(strategy, regime):

    prices = generate_price_series(
        start_price=100,
        steps=100,
        volatility=regime["volatility"]
    )

    returns = compute_returns(prices)

    strategy_returns = simulate_strategy_on_returns(strategy, returns)

    metrics = compute_performance_metrics(strategy_returns)

    return metrics


# ---------------------------------------------------------
# MULTI REGIME EVALUATION
# ---------------------------------------------------------

def evaluate_strategy_across_regimes(strategy):

    regimes = generate_regime_suite()

    regime_results = []

    for regime in regimes:

        metrics = evaluate_strategy_regime(strategy, regime)

        regime_results.append(metrics)

    # average metrics

    avg_profit = sum(r["profit"] for r in regime_results) / len(regime_results)
    avg_drawdown = sum(r["drawdown"] for r in regime_results) / len(regime_results)
    avg_volatility = sum(r["volatility"] for r in regime_results) / len(regime_results)
    avg_sharpe = sum(r["sharpe_like"] for r in regime_results) / len(regime_results)

    metrics = {
        "profit": avg_profit,
        "drawdown": avg_drawdown,
        "volatility": avg_volatility,
        "sharpe_like": avg_sharpe
    }

    return metrics


# ---------------------------------------------------------
# FINAL FITNESS
# ---------------------------------------------------------

def evaluate_strategy(strategy, policy_score=0):

    metrics = evaluate_strategy_across_regimes(strategy)

    fitness = compute_final_fitness(policy_score, metrics)

    return {
        "metrics": metrics,
        "fitness": fitness
    }


# ---------------------------------------------------------
# TEST
# ---------------------------------------------------------

if __name__ == "__main__":

    strategy = {
        "strategy_id": "test_strategy",
        "domain_id": "trading",
        "action": {
            "type": "BUY",
            "asset": "BTC",
            "quantity": 0.1
        }
    }

    result = evaluate_strategy(strategy)

    print("\nRegime evaluation result:\n")

    print(result)