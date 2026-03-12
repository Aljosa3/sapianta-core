"""
Simple Momentum Strategy Example
Used by ExperimentEngine
"""

def simple_strategy(price):

    price = float(price)   # <-- dodamo konverzijo

    threshold = 100

    if price > threshold:
        return 1
    else:
        return -1