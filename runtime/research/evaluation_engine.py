class EvaluationEngine:

    def __init__(self):
        pass

    def evaluate(self, experiment_result):

        profit = experiment_result["metrics"]["profit"]
        trades = experiment_result["metrics"]["trade_count"]

        score = 0

        if trades > 0:
            score = profit / trades

        evaluation = {
            "evaluation": {
                "profit": profit,
                "trade_count": trades,
                "score": score
            }
        }

        return evaluation
