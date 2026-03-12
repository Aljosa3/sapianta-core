"""
SAPIANTA Trading Runner

Executes the current production strategy on incoming market data.
Records every decision in the Decision Ledger.
"""

import time
import random

from runtime.production.strategy_promotion_engine import load_current_strategy
from runtime.examples.simple_strategy import simple_momentum
from runtime.ledger.decision_ledger import record_decision


class TradingRunner:

    def __init__(self):

        self.strategy_record = load_current_strategy()

        if not self.strategy_record:
            raise Exception("No production strategy found")

        self.strategy = self.strategy_record["strategy"]

    # ------------------------------------------------
    # MARKET DATA (SIMULATED)
    # ------------------------------------------------

    def get_market_price(self):

        # simple simulated price
        return random.randint(80, 140)

    # ------------------------------------------------
    # DECISION
    # ------------------------------------------------

    def generate_signal(self, price):

        threshold = self.strategy["threshold"]

        return simple_momentum(price, threshold)

    # ------------------------------------------------
    # EXECUTION
    # ------------------------------------------------

    def execute(self, signal, price):

        if signal == 1:
            action = "BUY"
        else:
            action = "SELL"

        print(f"PRICE {price} → {action}")

        # record decision in canonical ledger format
        record_decision(
            price=price,
            signal=signal,
            strategy=self.strategy,
            domain="trading",
            asset="BTC"
        )

    # ------------------------------------------------
    # LOOP
    # ------------------------------------------------

    def run(self, steps=20, delay=1):

        print("Starting trading runner")

        for _ in range(steps):

            price = self.get_market_price()

            signal = self.generate_signal(price)

            self.execute(signal, price)

            time.sleep(delay)


if __name__ == "__main__":

    runner = TradingRunner()

    runner.run()