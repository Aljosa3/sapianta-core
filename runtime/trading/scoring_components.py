"""
Scoring component functions for trading engine.
All functions are pure and deterministic.
"""

import numpy as np


def compute_atr(df, period=14):
    """
    Compute Average True Range.

    Args:
        df: DataFrame with 'high' and 'low' columns
        period: Rolling window period

    Returns:
        ATR series
    """
    high_low = df['high'] - df['low']
    return high_low.rolling(period).mean()


def volatility_percentile(atr_series, t):
    """
    Compute volatility percentile at time t.

    Args:
        atr_series: ATR series
        t: Time index

    Returns:
        Percentile value (0-100)
    """
    window = atr_series[:t]
    return (window.rank(pct=True).iloc[-1]) * 100


def determine_horizon(vol_pct):
    """
    Determine trading horizon based on volatility percentile.

    Args:
        vol_pct: Volatility percentile (0-100)

    Returns:
        Horizon in periods
    """
    if vol_pct < 40:
        return 24
    elif vol_pct < 70:
        return 12
    else:
        return 6


def projected_move(returns):
    """
    Compute projected move from return series.

    Args:
        returns: Array-like of historical returns

    Returns:
        Projected move value
    """
    median = np.median(returns)
    trimmed = np.mean(np.sort(returns)[5:-5]) if len(returns) > 10 else 0
    regime = np.mean(returns)
    return 0.4*median + 0.3*trimmed + 0.3*regime


def compute_edge(projected_move, risk_unit):
    """
    Compute edge metric.

    Args:
        projected_move: Projected move value
        risk_unit: Risk unit value

    Returns:
        Edge value
    """
    if risk_unit == 0:
        return 0
    return projected_move / risk_unit
