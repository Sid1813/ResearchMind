from agents.base_agent import BaseAgent
from config.prompts import PLANNER_PROMPT
from schemas.task import ResearchPlan


class PlannerAgent(BaseAgent):

    def __init__(self):
        super().__init__("Planner Agent")

    def create_plan(self, topic: str) -> ResearchPlan:

        prompt = PLANNER_PROMPT.format(
            topic=topic
        )

        return self.generate_structured(
            prompt,
            ResearchPlan
        )