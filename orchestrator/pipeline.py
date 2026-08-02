from agents.planner import PlannerAgent
from agents.researcher import ResearchAgent
from agents.writer import WriterAgent
from agents.critic import CriticAgent


class ResearchPipeline:

    def __init__(self):

        self.planner = PlannerAgent()
        self.researcher = ResearchAgent()
        self.writer = WriterAgent()
        self.critic = CriticAgent()

    def run(
        self,
        topic: str,
        evaluate_report: bool = False
    ):

        # Planner
        plan = self.planner.create_plan(topic)

        # Sequential Research
        evidence = []

        for task in plan.tasks:
            evidence.append(
                self.researcher.research(task)
            )

        # Writer
        report = self.writer.write_report(evidence)

        # Optional Critic
        review = None

        if evaluate_report:
            review = self.critic.review(report)

        return plan, evidence, report, review