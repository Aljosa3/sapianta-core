"""
Auto Research Trigger

Monitors strategy performance and automatically triggers
research when performance degrades.
"""

from runtime.research.performance_feedback_engine import PerformanceFeedbackEngine
from runtime.research.research_orchestrator import run_research_cycle


class AutoResearchTrigger:

    def __init__(self):

        self.feedback_engine = PerformanceFeedbackEngine()

    # ------------------------------------------------
    # CHECK PERFORMANCE
    # ------------------------------------------------

    def check_performance(self):

        result = self.feedback_engine.generate_research_signal()

        signal = result["signal"]
        metrics = result["metrics"]

        print("\nSAPIANTA PERFORMANCE MONITOR\n")

        print("Signal:", signal)
        print("Metrics:", metrics)

        return signal

    # ------------------------------------------------
    # TRIGGER RESEARCH
    # ------------------------------------------------

    def run(self):

        signal = self.check_performance()

        if signal == "RESEARCH_NEW_STRATEGY":

            print("\nTriggering research cycle...\n")

            run_research_cycle()

        elif signal == "REDUCE_RISK":

            print("\nRisk warning: strategy drawdown high\n")

        else:

            print("\nStrategy remains in production\n")


if __name__ == "__main__":

    trigger = AutoResearchTrigger()

    trigger.run()
