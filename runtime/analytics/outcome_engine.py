"""
Outcome Engine

Reads the Decision Ledger and calculates performance metrics.
Supports both:
1. direct trading runner entries
2. older decision_envelope ledger entries
"""

import json
import os


LEDGER_PATH = "runtime/history/decision_ledger.jsonl"


class OutcomeEngine:

    def __init__(self):

        if not os.path.exists(LEDGER_PATH):
            raise Exception("Decision ledger not found")

        self.decisions = self.load_ledger()

    # ------------------------------------------------
    # LOAD LEDGER
    # ------------------------------------------------

    def load_ledger(self):

        decisions = []

        with open(LEDGER_PATH, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                decisions.append(json.loads(line))

        return decisions

    # ------------------------------------------------
    # NORMALIZATION
    # ------------------------------------------------

    def normalize_decision(self, decision):

        # New direct runner format
        if "price" in decision and "signal" in decision:
            return {
                "timestamp": decision.get("timestamp"),
                "price": decision.get("price"),
                "signal": decision.get("signal"),
                "strategy": decision.get("strategy"),
            }

        # Older decision envelope format
        # It usually does not contain market price / signal directly,
        # so we try a best-effort extraction and otherwise skip it.
        envelope = decision.get("decision_envelope")
        if envelope:
            action = envelope.get("action", {})
            action_type = action.get("type")

            signal = None
            if action_type == "BUY":
                signal = 1
            elif action_type == "SELL":
                signal = -1

            # old envelope entries do not contain explicit price
            price = decision.get("price")

            return {
                "timestamp": decision.get("timestamp"),
                "price": price,
                "signal": signal,
                "strategy": envelope.get("proposal_reference", {}),
            }

        return None

    # ------------------------------------------------
    # METRICS
    # ------------------------------------------------

    def calculate_metrics(self):

        profit = 0.0
        wins = 0
        losses = 0
        equity = 0.0
        peak = 0.0
        max_drawdown = 0.0
        processed_trades = 0
        skipped_entries = 0

        for raw_decision in self.decisions:

            decision = self.normalize_decision(raw_decision)

            if not decision:
                skipped_entries += 1
                continue

            signal = decision.get("signal")
            price = decision.get("price")

            # Skip entries that do not have enough data
            if signal is None or price is None:
                skipped_entries += 1
                continue

            try:
                price = float(price)
            except (TypeError, ValueError):
                skipped_entries += 1
                continue

            # Simple simulated outcome model
            if signal == 1:
                trade_profit = price * 0.01
            else:
                trade_profit = -price * 0.005

            profit += trade_profit
            processed_trades += 1

            if trade_profit > 0:
                wins += 1
            else:
                losses += 1

            equity += trade_profit

            if equity > peak:
                peak = equity

            drawdown = peak - equity
            if drawdown > max_drawdown:
                max_drawdown = drawdown

        trades = wins + losses
        win_rate = wins / trades if trades else 0.0

        return {
            "profit": round(profit, 4),
            "trades": trades,
            "wins": wins,
            "losses": losses,
            "win_rate": round(win_rate, 3),
            "max_drawdown": round(max_drawdown, 4),
            "skipped_entries": skipped_entries,
            "processed_trades": processed_trades,
        }


# ------------------------------------------------
# CLI TEST
# ------------------------------------------------

if __name__ == "__main__":

    engine = OutcomeEngine()
    metrics = engine.calculate_metrics()

    print("\nSAPIANTA STRATEGY PERFORMANCE\n")

    for k, v in metrics.items():
        print(f"{k}: {v}")