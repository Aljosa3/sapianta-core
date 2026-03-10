"""
SAPIANTA Experiment Engine Market Adapter

Purpose
-------
Connect experiment_engine with market_simulator.

Generates strategy returns based on synthetic market data.

Output is used by:
- fitness_metrics
- fitness_engine
"""

from runtime.market.market_simulator import simulate_market


# ---------------------------------------------------------
# STRATEGY RETURN SIMULATION
# ---------------------------------------------------------

def simulate_strategy_returns(strategy):

    market = simulate_market()

    returns = market["returns"]

    strategy_returns = []

    action = strategy["action"]["type"]
    position_size = strategy["action"]["quantity"]

    for r in returns:

        if action == "BUY":

            pnl = r * position_size

        else:  # SELL

            pnl = -r * position_size

        strategy_returns.append(pnl)

    return {

        "market_regime": market["regime"],

        "strategy_returns": strategy_returns
    }


# ---------------------------------------------------------
# FULL STRATEGY MARKET TEST
# ---------------------------------------------------------

def run_market_strategy_test(strategy):

    result = simulate_strategy_returns(strategy)

    return result


# ---------------------------------------------------------
# TEST
# ---------------------------------------------------------

if __name__ == "__main__":

    strategy = {

        "strategy_id": "test_strategy",

        "domain_id": "trading",

        "action": {

            "type": "BUY",

            "asset": "BTC",

            "quantity": 0.1
        }
    }

    result = run_market_strategy_test(strategy)

    print("\nMarket regime:", result["market_regime"])

    print("\nFirst returns:")

    print(result["strategy_returns"][:5])