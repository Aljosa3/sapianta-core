"""
SAPIANTA Market Simulator

Purpose
-------
Generate synthetic market data for strategy testing.

Capabilities
------------
- price series generation
- returns calculation
- market regimes
- strategy interaction

Used by experiment_runner for strategy evaluation.
"""

import random


# ---------------------------------------------------------
# PRICE SERIES GENERATION
# ---------------------------------------------------------

def generate_price_series(
    start_price=100,
    steps=50,
    volatility=0.01,
    drift=0,
    rng=None
):

    if rng is None:
        rng = random

    prices = [start_price]

    for _ in range(steps):

        change = drift + rng.gauss(0, volatility)

        next_price = prices[-1] * (1 + change)

        prices.append(next_price)

    return prices


# ---------------------------------------------------------
# RETURNS
# ---------------------------------------------------------

def compute_returns(prices):

    returns = []

    for i in range(1, len(prices)):

        r = (prices[i] - prices[i - 1]) / prices[i - 1]

        returns.append(r)

    return returns


# ---------------------------------------------------------
# MARKET SIMULATION WITH STRATEGY
# ---------------------------------------------------------

def simulate_market(strategy, regime, seed=None, steps=50):

    rng = random.Random(seed)

    prices = generate_price_series(
        start_price=100,
        steps=steps,
        volatility=regime["volatility"],
        drift=regime["drift"],
        rng=rng
    )

    history = []

    position = 0
    entry_price = None
    profit = 0

    for price in prices:

        history.append(price)

        decision = strategy(history)

        if decision == "BUY" and position == 0:

            entry_price = price
            position = 1

        elif decision == "SELL" and position == 1:

            profit += price - entry_price
            position = 0

    returns = compute_returns(prices)

    return {

        "regime": regime["regime"],

        "profit": profit,

        "final_price": prices[-1],

        "prices": prices,

        "returns": returns
    }


# ---------------------------------------------------------
# TEST STRATEGY
# ---------------------------------------------------------

def test_strategy(history):

    if len(history) < 2:
        return "HOLD"

    if history[-1] > history[-2]:
        return "BUY"

    return "HOLD"


# ---------------------------------------------------------
# TEST
# ---------------------------------------------------------

if __name__ == "__main__":

    regime = {

        "regime": "bull",

        "volatility": 0.01,

        "drift": 0.002
    }

    result = simulate_market(test_strategy, regime)

    print("\nMarket regime:", result["regime"])

    print("\nProfit:", result["profit"])

    print("\nFirst prices:")
    print(result["prices"][:5])

    print("\nFirst returns:")
    print(result["returns"][:5])