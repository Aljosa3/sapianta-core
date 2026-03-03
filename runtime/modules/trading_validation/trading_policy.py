import numpy as np
from runtime.domain_contract import DomainPolicy
from .correlation_penalty import apply_correlation_penalty


class TradingPolicy(DomainPolicy):

    POLICY_NAME = "TradingPolicy"
    POLICY_VERSION = "0.1"

    # ------------------------------------------------------------------
    # 🔹 Domain-agnostic execution entry point (NEW)
    # ------------------------------------------------------------------

    def execute(self, input_data, config, t=None):
        """
        DomainPolicy contract implementation.

        input_data:
            market data dict

        config:
            frozen config snapshot

        t:
            time index
        """
        return self.generate_candidates(config, input_data, t)

    # ------------------------------------------------------------------
    # 🔹 Trading-specific logic (unchanged)
    # ------------------------------------------------------------------

    def compute_atr(self, df, period=14):
        high_low = df['high'] - df['low']
        return high_low.rolling(period).mean()

    def volatility_percentile(self, atr_series, t):
        window = atr_series[:t]
        return (window.rank(pct=True).iloc[-1]) * 100

    def determine_horizon(self, vol_pct):
        if vol_pct < 40:
            return 24
        elif vol_pct < 70:
            return 12
        else:
            return 6

    def projected_move(self, returns):
        median = np.median(returns)
        trimmed = np.mean(np.sort(returns)[5:-5]) if len(returns) > 10 else 0
        regime = np.mean(returns)
        return 0.4 * median + 0.3 * trimmed + 0.3 * regime

    def compute_edge(self, projected_move, risk_unit):
        if risk_unit == 0:
            return 0
        return projected_move / risk_unit

    def generate_candidates(self, config, data_dict, t):

        candidates = []

        for asset, df in data_dict.items():
            atr_series = self.compute_atr(df)
            vol_pct = self.volatility_percentile(atr_series, t)
            horizon = self.determine_horizon(vol_pct)

            risk_unit = atr_series.iloc[t] * config['stop_multiplier'][asset]

            forward_returns = df['close'].pct_change(horizon).shift(-horizon).iloc[:t]

            if len(forward_returns.dropna()) < config['min_sample']:
                continue

            projected = self.projected_move(forward_returns.dropna())
            edge = self.compute_edge(projected, risk_unit)

            if edge > config['min_edge_threshold']:
                candidates.append((asset, edge))

        if not candidates:
            return []

        # apply correlation penalty
        candidates = apply_correlation_penalty(candidates, data_dict, t)

        return candidates