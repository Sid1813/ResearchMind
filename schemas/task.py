from pydantic import BaseModel


class ResearchTask(BaseModel):
    id: int
    title: str
    description: str


class ResearchPlan(BaseModel):
    tasks: list[ResearchTask]