from runtime.domains.trading.decision_to_intent import transform_decision_to_intent


def test_transform_basic():
    decision = {
        "decision_id": "D001",
        "action": "BUY",
        "symbol": "BTCUSDT",
        "timeframe": "1h"
    }

    intent = transform_decision_to_intent(decision)

    assert intent == {
        "intent_id": "INTENT_D001",
        "decision_id": "D001",
        "action": "BUY",
        "symbol": "BTCUSDT",
        "timeframe": "1h",
    }


def test_transform_is_deterministic():
    decision = {
        "decision_id": "D002",
        "action": "SELL",
        "symbol": "ETHUSDT",
        "timeframe": "4h"
    }

    intent1 = transform_decision_to_intent(decision)
    intent2 = transform_decision_to_intent(decision)

    assert intent1 == intent2