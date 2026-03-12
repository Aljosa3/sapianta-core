"""
Performance Feedback Engine

Reads strategy performance metrics and produces feedback
for the research system.
"""

from runtime.analytics.outcome_engine import OutcomeEngine


class PerformanceFeedbackEngine:

    def __init__(self):

        self.outcome_engine = OutcomeEngine()

    # ---------------------------------------------
    # STRATEGY PERFORMANCE
    # ---------------------------------------------

    def evaluate_strategy(self):

        metrics = self.outcome_engine.calculate_metrics()

        feedback = {
            "profit": metrics["profit"],
            "win_rate": metrics["win_rate"],
            "drawdown": metrics["max_drawdown"],
            "trades": metrics["trades"]
        }

        return feedback

    # ---------------------------------------------
    # RESEARCH SIGNAL
    # ---------------------------------------------

    def generate_research_signal(self):

        feedback = self.evaluate_strategy()

        signal = "KEEP"

        if feedback["profit"] < 0:
            signal = "RESEARCH_NEW_STRATEGY"

        if feedback["drawdown"] > 5:
            signal = "REDUCE_RISK"

        return {
            "signal": signal,
            "metrics": feedback
        }


if __name__ == "__main__":

    engine = PerformanceFeedbackEngine()

    result = engine.generate_research_signal()

    print("\nSAPIANTA PERFORMANCE FEEDBACK\n")

    for k, v in result.items():
        print(k, ":", v)
