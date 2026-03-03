import copy
from runtime.trading.rolling_sim_v0_1 import TradingEngine
from runtime.governance.run_manifest import generate_run_manifest
from tests.runtime.trading.test_trading_replay_determinism_v0_1 import (
    _make_data_dict,
    _make_config,
)


def test_run_manifest_deterministic():

    data = _make_data_dict()
    config = _make_config()

    engine1 = TradingEngine(
        config=copy.deepcopy(config),
        data_dict=copy.deepcopy(data),
    )
    engine1.run()

    manifest1 = generate_run_manifest(engine1.portfolio.history)

    engine2 = TradingEngine(
        config=copy.deepcopy(config),
        data_dict=copy.deepcopy(data),
    )
    engine2.run()

    manifest2 = generate_run_manifest(engine2.portfolio.history)

    assert manifest1.run_hash == manifest2.run_hash