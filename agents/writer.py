from agents.base_agent import BaseAgent
from config.prompts import WRITER_PROMPT
from schemas.report import Report


class WriterAgent(BaseAgent):

    def __init__(self):

        super().__init__("Writer Agent")

    def write_report(self, evidence):

        context = ""

        for item in evidence:

            context += f"""

Title:
{item.title}

Findings:
{item.findings}

"""

        prompt = WRITER_PROMPT.format(
            evidence=context
        )

        return self.generate_structured(
            prompt,
            Report
        )