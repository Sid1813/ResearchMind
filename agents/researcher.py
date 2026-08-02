from agents.base_agent import BaseAgent
from config.prompts import RESEARCH_PROMPT
from schemas.evidence import Evidence, Source
from schemas.task import ResearchTask
from services.tavily_service import TavilyService


class ResearchAgent(BaseAgent):

    def __init__(self):

        super().__init__("Research Agent")
        self.search = TavilyService()

    def research(self, task: ResearchTask) -> Evidence:

        results = self.search.search(task.title)

        context = ""

        for result in results:

            context += f"""
Title:
{result['title']}

Content:
{result['content']}

URL:
{result['url']}

"""

        prompt = RESEARCH_PROMPT.format(
            title=task.title,
            description=task.description,
            context=context
        )

        findings = self.generate(prompt)

        sources = [
            Source(
                title=result["title"],
                url=result["url"]
            )
            for result in results
        ]

        return Evidence(
            task_id=task.id,
            title=task.title,
            findings=findings,
            sources=sources
        )