from pydantic import BaseModel


class Review(BaseModel):
    strengths: list[str]
    weaknesses: list[str]
    improvements: list[str]
    score: int