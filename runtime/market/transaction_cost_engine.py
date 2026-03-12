"""
SAPIANTA Transaction Cost Engine

Purpose
-------
Simulate realistic trading costs.

Includes:
- exchange fees
- bid/ask spread
- slippage

Used by strategy evaluation to prevent unrealistic profitability.
"""

# ---------------------------------------------------------
# COST PARAMETERS
# ---------------------------------------------------------

DEFAULT_COST_MODEL = {

    "fee_rate": 0.001,     # 0.1% exchange fee
    "spread": 0.0005,      # 0.05% bid/ask spread
    "slippage": 0.0007     # 0.07% execution slippage
}


# ---------------------------------------------------------
# COST CALCULATION
# ---------------------------------------------------------

def compute_transaction_cost(position_size, price, cost_model=None):

    if cost_model is None:
        cost_model = DEFAULT_COST_MODEL

    trade_value = abs(position_size * price)

    fee = trade_value * cost_model["fee_rate"]

    spread_cost = trade_value * cost_model["spread"]

    slippage_cost = trade_value * cost_model["slippage"]

    total_cost = fee + spread_cost + slippage_cost

    return total_cost


# ---------------------------------------------------------
# APPLY COST TO RETURNS
# ---------------------------------------------------------

def apply_transaction_costs(strategy_returns, position_size, price=100):

    cost = compute_transaction_cost(position_size, price)

    adjusted_returns = []

    for i, r in enumerate(strategy_returns):

        if i == 0:
            adjusted_returns.append(r - cost)
        else:
            adjusted_returns.append(r)

    return adjusted_returns


# ---------------------------------------------------------
# TEST
# ---------------------------------------------------------

if __name__ == "__main__":

    test_returns = [0.01, -0.005, 0.004, -0.002]

    adjusted = apply_transaction_costs(
        test_returns,
        position_size=0.1,
        price=100
    )

    print("\nOriginal returns:")
    print(test_returns)

    print("\nReturns after costs:")
    print(adjusted)