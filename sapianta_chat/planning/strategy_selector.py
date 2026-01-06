from sapianta_chat.models import ChatRequest
from sapianta_chat.planning.strategies.simple_plan import SimplePlan
from sapianta_chat.planning.strategies.boundary_plan import BoundaryPlan
from sapianta_chat.planning.strategies.no_plan import NoPlan


class PlanningStrategySelector:
    def select(self, request: ChatRequest):
        if request.interaction_type == "boundary":
            return BoundaryPlan()

        if request.interaction_type == "unknown":
            return NoPlan()

        return SimplePlan()
