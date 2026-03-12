"""
Simple Momentum Strategy Example
Used by ExperimentEngine and TradingRunner
"""

# ------------------------------------------------
# PARAMETRIC MOMENTUM STRATEGY
# ------------------------------------------------

def simple_momentum(price, threshold=100):

    price = float(price)

    if price > threshold:
        return 1
    else:
        return -1


# ------------------------------------------------
# BACKWARD COMPATIBILITY
# ------------------------------------------------
# ExperimentEngine še vedno uporablja simple_strategy(price)

def simple_strategy(price):

    return simple_momentum(price, 100)