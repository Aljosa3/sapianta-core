from runtime.modules.trading_validation.trading_policy import TradingPolicy
from runtime.domain_contract import DomainPolicy
from runtime.trading.deterministic_utils import stable_hash, freeze_config

# ✅ Execution Isolation Boundary
from runtime.governance.execution_boundary import ExecutionBoundary


class Portfolio:
    def __init__(self, capital):
        self.cash = capital
        self.positions = {}
        self.history = []


class TradingEngine:

    def __init__(self, config, data_dict):

        # Deterministic config hash
        self.config_hash = stable_hash(config)

        # Freeze config (immutability)
        self.config = freeze_config(config)

        self.data = data_dict
        self.portfolio = Portfolio(capital=100000)

        # L2 Execution Boundary
        self.boundary = ExecutionBoundary(engine_version="0.1")

        # DomainPolicy binding
        self.policy: DomainPolicy = TradingPolicy()

    def run(self):

        for t in range(50, len(next(iter(self.data.values())))):

            # 🔄 NEW: use domain-agnostic execute()
            candidates = self.policy.execute(
                self.data,
                self.config,
                t
            )

            if not candidates:
                continue

            total_edge = sum(edge for _, edge in candidates)

            for asset, edge in candidates:
                allocation = edge / total_edge
                allocation = min(allocation, self.config['max_position_cap'])

                capital_to_use = self.portfolio.cash * allocation
                self.portfolio.positions[asset] = capital_to_use
                self.portfolio.cash -= capital_to_use

            # Delegated to Execution Boundary
            self.boundary.record(
                policy_name=self.policy.POLICY_NAME,
                policy_version=self.policy.POLICY_VERSION,
                config_hash=self.config_hash,
                t=t,
                candidates=tuple(candidates),
                positions=self.portfolio.positions.copy(),
                cash=self.portfolio.cash,
            )

        # Fail-closed enforcement handled by boundary
        self.boundary.finalize()

        # Expose history externally (for tests / audit)
        self.portfolio.history = self.boundary.history