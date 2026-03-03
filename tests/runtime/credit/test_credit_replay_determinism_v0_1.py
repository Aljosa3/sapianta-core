import copy
from runtime.credit.credit_sim_v0_1 import CreditEngine


def _make_config():
    return {
        "min_income": 2000,
        "max_dti": 0.4,
    }


def _make_applications():
    return [
        {"income": 3000, "dti": 0.3},
        {"income": 1500, "dti": 0.2},
        {"income": 5000, "dti": 0.5},
    ]


def _history_to_plain(history):
    return [
        {
            "t": env.t,
            "hash": env.envelope_hash,
        }
        for env in history
    ]


def test_credit_replay_determinism_v0_1():

    config = _make_config()
    apps = _make_applications()

    eng1 = CreditEngine(copy.deepcopy(config), copy.deepcopy(apps))
    h1 = _history_to_plain(eng1.run())

    eng2 = CreditEngine(copy.deepcopy(config), copy.deepcopy(apps))
    h2 = _history_to_plain(eng2.run())

    assert h1 == h2