"""
SAPIANTA Market Regime Engine

Purpose
-------
Generate deterministic market regimes for robust strategy evaluation.

Prevents overfitting by testing strategies across multiple regimes.

Regimes
-------
- bull
- bear
- sideways
- volatile
- crisis
"""

import random


# ---------------------------------------------------------
# REGIME DEFINITIONS
# ---------------------------------------------------------

REGIMES = {

    "bull": {
        "drift": 0.002,
        "volatility": 0.01
    },

    "bear": {
        "drift": -0.002,
        "volatility": 0.015
    },

    "sideways": {
        "drift": 0.0,
        "volatility": 0.005
    },

    "volatile": {
        "drift": 0.0,
        "volatility": 0.03
    },

    "crisis": {
        "drift": -0.005,
        "volatility": 0.05
    }

}


# ---------------------------------------------------------
# RANDOM REGIME
# ---------------------------------------------------------

def sample_regime():

    name = random.choice(list(REGIMES.keys()))

    regime = REGIMES[name]

    return {

        "regime": name,

        "drift": regime["drift"],

        "volatility": regime["volatility"]
    }


# ---------------------------------------------------------
# REGIME SUITE
# ---------------------------------------------------------

def generate_regime_suite():

    suite = []

    for name, params in REGIMES.items():

        suite.append({

            "regime": name,

            "drift": params["drift"],

            "volatility": params["volatility"]
        })

    return suite


# ---------------------------------------------------------
# TEST
# ---------------------------------------------------------

if __name__ == "__main__":

    print("\nRandom regime:")

    print(sample_regime())

    print("\nFull regime suite:")

    print(generate_regime_suite())