"""
SAPIANTA Fitness Metrics

Purpose
-------
Compute market-based performance metrics for strategy evaluation.

Metrics:
- profit
- drawdown
- volatility
- sharpe_like_score

These metrics complement policy evaluation and are used by
fitness_engine to compute final strategy fitness.
"""

import math


# ---------------------------------------------------------
# PROFIT
# ---------------------------------------------------------

def compute_profit(returns):

    if not returns:
        return 0

    return sum(returns)


# ---------------------------------------------------------
# MAX DRAWDOWN
# ---------------------------------------------------------

def compute_max_drawdown(returns):

    equity = 0
    peak = 0
    max_dd = 0

    for r in returns:

        equity += r

        peak = max(peak, equity)

        drawdown = peak - equity

        max_dd = max(max_dd, drawdown)

    return max_dd


# ---------------------------------------------------------
# VOLATILITY
# ---------------------------------------------------------

def compute_volatility(returns):

    if not returns:
        return 0

    mean = sum(returns) / len(returns)

    variance = sum(
        (r - mean) ** 2 for r in returns
    ) / len(returns)

    return math.sqrt(variance)


# ---------------------------------------------------------
# SHARPE-LIKE SCORE
# ---------------------------------------------------------

def compute_sharpe_like(returns):

    if not returns:
        return 0

    profit = compute_profit(returns)

    volatility = compute_volatility(returns)

    if volatility == 0:
        return 0

    return profit / volatility


# ---------------------------------------------------------
# FULL METRIC SET
# ---------------------------------------------------------

def compute_performance_metrics(returns):

    return {

        "profit": compute_profit(returns),

        "drawdown": compute_max_drawdown(returns),

        "volatility": compute_volatility(returns),

        "sharpe_like": compute_sharpe_like(returns)
    }


# ---------------------------------------------------------
# TEST
# ---------------------------------------------------------

if __name__ == "__main__":

    returns = [0.02, -0.01, 0.03, -0.02, 0.01]

    metrics = compute_performance_metrics(returns)

    print("Metrics:")
    print(metrics)