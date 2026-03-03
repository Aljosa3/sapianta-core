"""
Deterministic correlation penalty for trading candidates.

Purpose:
- Penalize candidate edges if candidates are highly correlated.
- Pure function, deterministic, replay-safe.
- Does NOT change candidate order (preserves original allocation mutation sequence).
"""

import numpy as np


def apply_correlation_penalty(candidates, data_dict, t, lookback=50):
    """
    Apply simple Pearson correlation penalty to candidate edges.

    Args:
        candidates: list of (asset, edge) in ORIGINAL order
        data_dict: dict {asset: dataframe}, must contain 'close'
        t: timestep index
        lookback: lookback window for correlation calculation

    Returns:
        list of (asset, adjusted_edge) in SAME order as input
    """
    if len(candidates) <= 1:
        return candidates

    assets = [a for a, _ in candidates]

    # Build return matrix over a fixed historical window [t-lookback, t)
    start = max(1, t - lookback)  # start at >=1 due to pct_change
    end = t

    series_list = []
    for asset in assets:
        df = data_dict[asset]
        r = df["close"].pct_change().iloc[start:end]
        # Ensure same length across assets (should be, given same slicing)
        series_list.append(r.to_numpy(dtype="float64"))

    # If window too small, do nothing (fail-open but deterministic)
    if len(series_list[0]) < 2:
        return candidates

    returns_matrix = np.column_stack(series_list)

    # Pearson correlation matrix (deterministic)
    corr = np.corrcoef(returns_matrix, rowvar=False)

    adjusted = []
    n = len(assets)

    for i, (asset, edge) in enumerate(candidates):
        # avg corr with others
        vals = [corr[i, j] for j in range(n) if j != i]
        avg_corr = float(np.nanmean(vals)) if vals else 0.0

        # Simple penalty
        adjusted_edge = edge * (1.0 - avg_corr)
        adjusted.append((asset, adjusted_edge))

    return adjusted