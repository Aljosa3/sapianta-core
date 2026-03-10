"""
SAPIANTA Strategy Genome

Purpose
-------
Defines the genetic structure of strategies for evolutionary search.

Provides:
- genome creation
- mutation
- crossover
- conversion to executable strategy
"""

import random
import uuid


# ---------------------------------------------------------
# PARAMETER SPACE
# ---------------------------------------------------------

PARAMETER_SPACE = {

    "action_type": ["BUY", "SELL"],

    "asset": ["BTC", "ETH"],

    "position_size": {
        "min": 0.01,
        "max": 0.2
    },

    "risk_limit": {
        "min": 0.05,
        "max": 0.5
    }

}


# ---------------------------------------------------------
# GENOME GENERATION
# ---------------------------------------------------------

def create_random_genome():

    genome = {

        "genome_id": uuid.uuid4().hex[:8],

        "action_type": random.choice(PARAMETER_SPACE["action_type"]),

        "asset": random.choice(PARAMETER_SPACE["asset"]),

        "position_size": round(
            random.uniform(
                PARAMETER_SPACE["position_size"]["min"],
                PARAMETER_SPACE["position_size"]["max"]
            ), 3
        ),

        "risk_limit": round(
            random.uniform(
                PARAMETER_SPACE["risk_limit"]["min"],
                PARAMETER_SPACE["risk_limit"]["max"]
            ), 3
        )
    }

    return genome


# ---------------------------------------------------------
# MUTATION
# ---------------------------------------------------------

def mutate_genome(genome):

    mutated = dict(genome)

    mutation_field = random.choice([
        "position_size",
        "risk_limit"
    ])

    if mutation_field == "position_size":

        delta = random.uniform(-0.05, 0.05)

        mutated["position_size"] = max(
            PARAMETER_SPACE["position_size"]["min"],
            min(
                PARAMETER_SPACE["position_size"]["max"],
                round(mutated["position_size"] + delta, 3)
            )
        )

    if mutation_field == "risk_limit":

        delta = random.uniform(-0.1, 0.1)

        mutated["risk_limit"] = max(
            PARAMETER_SPACE["risk_limit"]["min"],
            min(
                PARAMETER_SPACE["risk_limit"]["max"],
                round(mutated["risk_limit"] + delta, 3)
            )
        )

    mutated["genome_id"] = uuid.uuid4().hex[:8]

    return mutated


# ---------------------------------------------------------
# CROSSOVER
# ---------------------------------------------------------

def crossover(parent_a, parent_b):

    child = {

        "genome_id": uuid.uuid4().hex[:8],

        "action_type": random.choice(
            [parent_a["action_type"], parent_b["action_type"]]
        ),

        "asset": random.choice(
            [parent_a["asset"], parent_b["asset"]]
        ),

        "position_size": random.choice(
            [parent_a["position_size"], parent_b["position_size"]]
        ),

        "risk_limit": random.choice(
            [parent_a["risk_limit"], parent_b["risk_limit"]]
        )
    }

    return child


# ---------------------------------------------------------
# CONVERSION TO STRATEGY
# ---------------------------------------------------------

def genome_to_strategy(genome):

    strategy = {

        "strategy_id": f"genome_{genome['genome_id']}",

        "domain_id": "trading",

        "action": {
            "type": genome["action_type"],
            "asset": genome["asset"],
            "quantity": genome["position_size"]
        },

        "risk_limit": genome["risk_limit"]
    }

    return strategy


# ---------------------------------------------------------
# TEST
# ---------------------------------------------------------

if __name__ == "__main__":

    genome = create_random_genome()

    print("\nRandom genome")
    print(genome)

    mutated = mutate_genome(genome)

    print("\nMutated genome")
    print(mutated)

    strategy = genome_to_strategy(genome)

    print("\nConverted strategy")
    print(strategy)