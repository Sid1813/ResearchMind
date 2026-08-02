from pydantic import BaseModel


class Report(BaseModel):
    executive_summary: str
    detailed_analysis: str
    key_takeaways: list[str]
    conclusion: str