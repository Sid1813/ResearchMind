from agents.base_agent import BaseAgent
from config.prompts import CRITIC_PROMPT
from schemas.review import Review


class CriticAgent(BaseAgent):

    def __init__(self):

        super().__init__("Critic Agent")

    def review(self, report):

        prompt = CRITIC_PROMPT.format(
            report=report.model_dump_json(indent=2)
        )

        return self.generate_structured(
            prompt,
            Review
        )