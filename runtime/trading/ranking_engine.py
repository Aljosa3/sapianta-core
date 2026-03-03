"""
Ranking engine for candidate generation and deterministic sorting.
"""

from scoring_components import (
    compute_atr,
    volatility_percentile,
    determine_horizon,
    projected_move,
    compute_edge
)


def generate_ranked_candidates(config_snapshot, data_dict, t) -> dict:
    """
    Generate and rank trading candidates for timestep t.

    Args:
        config_snapshot: Validated configuration dictionary
        data_dict: Dictionary mapping asset names to DataFrames
        t: Current timestep index

    Returns:
        Dictionary with:
            'raw_candidates': List of (asset, edge) in original iteration order
            'ranked_candidates': List of (asset, edge) sorted by edge desc, asset name asc
    """
    raw_candidates = []

    # Iterate over assets in deterministic order (sorted asset names)
    for asset in sorted(data_dict.keys()):
        df = data_dict[asset]

        # Compute ATR
        atr_series = compute_atr(df)

        # Compute volatility percentile
        vol_pct = volatility_percentile(atr_series, t)

        # Determine horizon
        horizon = determine_horizon(vol_pct)

        # Compute risk unit
        risk_unit = atr_series.iloc[t] * config_snapshot['stop_multiplier'][asset]

        # Compute forward returns
        forward_returns = df['close'].pct_change(horizon).shift(-horizon).iloc[:t]

        # Apply minimum sample filter
        if len(forward_returns.dropna()) < config_snapshot['min_sample']:
            continue

        # Compute projected move
        projected = projected_move(forward_returns.dropna())

        # Compute edge
        edge = compute_edge(projected, risk_unit)

        # Apply minimum edge threshold filter
        if edge > config_snapshot['min_edge_threshold']:
            raw_candidates.append((asset, edge))

    # Apply explicit deterministic sorting for ranked output
    # Primary: edge descending (negative for descending sort)
    # Secondary: asset name ascending (tie breaker)
    ranked_candidates = sorted(raw_candidates, key=lambda x: (-x[1], x[0]))

    return {
        'raw_candidates': raw_candidates,
        'ranked_candidates': ranked_candidates
    }
