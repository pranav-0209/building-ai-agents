from pydantic import BaseModel, Field


class ResearchPlan(BaseModel):
    topic: str = Field(
        description="The main research topic derived from the user's question"
    )

    tasks: list[str] = Field(
        description="A list of focused research tasks needed to investigate the topic"
    )

class SearchResult(BaseModel):
    title: str
    url: str
    content: str