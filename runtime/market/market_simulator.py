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

Used by experiment_engine for strategy evaluation.
"""

import random


# ---------------------------------------------------------
# PRICE SERIES GENERATION
# ---------------------------------------------------------

def generate_price_series(
    start_price=100,
    steps=50,
    volatility=0.01
):

    prices = [start_price]

    for _ in range(steps):

        change = random.gauss(0, volatility)

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
# MARKET REGIME GENERATOR
# ---------------------------------------------------------

def generate_market_regime():

    regimes = [
        "bull",
        "bear",
        "sideways",
        "volatile"
    ]

    regime = random.choice(regimes)

    if regime == "bull":

        volatility = 0.01
        drift = 0.002

    elif regime == "bear":

        volatility = 0.015
        drift = -0.002

    elif regime == "sideways":

        volatility = 0.005
        drift = 0

    else:

        volatility = 0.03
        drift = 0

    return {

        "regime": regime,
        "volatility": volatility,
        "drift": drift
    }


# ---------------------------------------------------------
# MARKET SIMULATION
# ---------------------------------------------------------

def simulate_market():

    regime = generate_market_regime()

    prices = generate_price_series(
        start_price=100,
        steps=50,
        volatility=regime["volatility"]
    )

    returns = compute_returns(prices)

    return {

        "regime": regime["regime"],
        "prices": prices,
        "returns": returns
    }


# ---------------------------------------------------------
# TEST
# ---------------------------------------------------------

if __name__ == "__main__":

    market = simulate_market()

    print("\nMarket regime:", market["regime"])

    print("\nFirst prices:")
    print(market["prices"][:5])

    print("\nFirst returns:")
    print(market["returns"][:5])