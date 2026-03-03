import copy
import hashlib
import json

import numpy as np
import pandas as pd

from runtime.trading.rolling_sim_v0_1 import TradingEngine


def _stable_hash(obj) -> str:
    """Deterministic hash for nested python structures (dict/list/primitives)."""
    canonical = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def _make_deterministic_ohlc(n: int, seed: int) -> pd.DataFrame:
    """
    Create deterministic OHLC dataframe.
    We avoid randomness at runtime by using a fixed seed and fixed transforms.
    """
    rng = np.random.default_rng(seed)
    base = 100 + np.cumsum(rng.normal(0, 0.2, size=n))
    high = base + np.abs(rng.normal(0.1, 0.05, size=n))
    low = base - np.abs(rng.normal(0.1, 0.05, size=n))
    close = base + rng.normal(0, 0.05, size=n)

    # Use float64 explicitly
    df = pd.DataFrame(
        {
            "high": high.astype("float64"),
            "low": low.astype("float64"),
            "close": close.astype("float64"),
        }
    )
    return df


def _make_data_dict() -> dict:
    # Deterministic asset keys and deterministic data
    return {
        "ASSET_A": _make_deterministic_ohlc(n=140, seed=1),
        "ASSET_B": _make_deterministic_ohlc(n=140, seed=2),
        "ASSET_C": _make_deterministic_ohlc(n=140, seed=3),
    }


def _make_config() -> dict:
    return {
        "stop_multiplier": {
            "ASSET_A": 1.5,
            "ASSET_B": 1.5,
            "ASSET_C": 1.5,
        },
        "min_sample": 20,
        "min_edge_threshold": 0.0001,
        "max_position_cap": 0.6,
    }


def _history_to_plain(engine: TradingEngine):
    """
    Convert history to plain JSON-serializable structure.
    Ensures stable comparison across runs.
    """
    out = []
    for row in engine.portfolio.history:
        out.append(
            {
                "t": int(row["t"]),
                "cash": float(row["cash"]),
                "positions": {k: float(v) for k, v in row["positions"].items()},
            }
        )
    return out


def test_trading_replay_determinism_v0_1():
    data = _make_data_dict()
    config = _make_config()

    # Run #1
    eng1 = TradingEngine(config=copy.deepcopy(config), data_dict=copy.deepcopy(data))
    eng1.run()
    h1 = _history_to_plain(eng1)
    hash1 = _stable_hash(h1)

    # Run #2
    eng2 = TradingEngine(config=copy.deepcopy(config), data_dict=copy.deepcopy(data))
    eng2.run()
    h2 = _history_to_plain(eng2)
    hash2 = _stable_hash(h2)

    assert h1 == h2, "Replay invariance violated: history differs between identical runs"
    assert hash1 == hash2, "Replay invariance violated: history hash differs between identical runs"