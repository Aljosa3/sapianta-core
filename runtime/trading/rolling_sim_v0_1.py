import pandas as pd
import numpy as np

class Portfolio:
    def __init__(self, capital):
        self.cash = capital
        self.positions = {}
        self.history = []

class TradingEngine:

    def __init__(self, config, data_dict):
        self.config = config
        self.data = data_dict  # dict: {asset: dataframe}
        self.portfolio = Portfolio(capital=100000)

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
        return 0.4*median + 0.3*trimmed + 0.3*regime

    def compute_edge(self, projected_move, risk_unit):
        if risk_unit == 0:
            return 0
        return projected_move / risk_unit

    def run(self):

        for t in range(50, len(next(iter(self.data.values())))):
            candidates = []

            for asset, df in self.data.items():
                atr_series = self.compute_atr(df)
                vol_pct = self.volatility_percentile(atr_series, t)
                horizon = self.determine_horizon(vol_pct)

                risk_unit = atr_series.iloc[t] * self.config['stop_multiplier'][asset]

                forward_returns = df['close'].pct_change(horizon).shift(-horizon).iloc[:t]

                if len(forward_returns.dropna()) < self.config['min_sample']:
                    continue

                projected = self.projected_move(forward_returns.dropna())
                edge = self.compute_edge(projected, risk_unit)

                if edge > self.config['min_edge_threshold']:
                    candidates.append((asset, edge))

            if not candidates:
                continue

            total_edge = sum(edge for _, edge in candidates)

            for asset, edge in candidates:
                allocation = edge / total_edge
                allocation = min(allocation, self.config['max_position_cap'])

                capital_to_use = self.portfolio.cash * allocation
                self.portfolio.positions[asset] = capital_to_use
                self.portfolio.cash -= capital_to_use

            self.portfolio.history.append({
                't': t,
                'positions': self.portfolio.positions.copy(),
                'cash': self.portfolio.cash
            })