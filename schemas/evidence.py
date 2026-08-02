from pydantic import BaseModel


class Source(BaseModel):
    title: str
    url: str


class Evidence(BaseModel):
    task_id: int
    title: str
    findings: str
    sources: list[Source]