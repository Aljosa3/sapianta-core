import copy
from runtime.trading.rolling_sim_v0_1 import TradingEngine
from runtime.governance.replay_engine import replay_and_verify
from tests.runtime.trading.test_trading_replay_determinism_v0_1 import (
    _make_data_dict,
    _make_config,
)


def test_replay_engine_trading():

    data = _make_data_dict()
    config = _make_config()

    engine = TradingEngine(
        config=copy.deepcopy(config),
        data_dict=copy.deepcopy(data),
    )

    engine.run()
    original_history = engine.portfolio.history

    def factory():
        return TradingEngine(
            config=copy.deepcopy(config),
            data_dict=copy.deepcopy(data),
        )

    assert replay_and_verify(factory, original_history)