import uuid
import datetime


class IdeaEngine:

    def __init__(self, agent_id="research_agent_01"):
        self.agent_id = agent_id

    def generate_idea(self):

        idea_id = str(uuid.uuid4())

        idea = {
            "idea_artifact": {

                "idea_id": idea_id,

                "source": {
                    "type": "AI_AGENT",
                    "agent_id": self.agent_id
                },

                "timestamp": datetime.datetime.utcnow().isoformat(),

                "domain": {
                    "primary_domain": "trading",
                    "related_domains": ["ai", "data_science"]
                },

                "classification": {
                    "category": "strategy",
                    "subcategory": "momentum"
                },

                "description": {
                    "title": "Simple momentum strategy",
                    "summary": "Buy when price is above threshold."
                },

                "hypothesis": {
                    "description": "Momentum strategies may outperform in trending markets."
                },

                "expected_impact": {
                    "metrics": ["profit", "drawdown"],
                    "potential_improvement": "baseline experiment"
                },

                "metadata": {
                    "environment": "research"
                }

            }
        }

        return idea
