import hashlib


class ExperimentEngine:

    def __init__(self, strategy_function):
        self.strategy_function = strategy_function

    def run_experiment(self, dataset):

        trades = []

        for price in dataset:
            decision = self.strategy_function(price)
            trades.append(decision)

        profit = sum(trades)

        result = {
            "metrics": {
                "profit": profit,
                "trade_count": len(trades)
            }
        }

        return result

    def compute_hash(self, data):

        serialized = str(data).encode()
        return hashlib.sha256(serialized).hexdigest()
