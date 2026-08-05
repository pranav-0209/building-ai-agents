from pydantic import BaseModel, Field


class ResearchPlan(BaseModel):
    topic: str = Field(description="The main research topic")

    tasks: list[str] = Field(
        description="A list of research tasks needed to investigate the topic")


class SearchResult(BaseModel):
    title: str
    url: str
    content: str

class Source(BaseModel):
    title: str
    url: str

class ResearchFinding(BaseModel):
    task: str = Field(description="The research task being investigated")
    summary: str = Field(
        description="A concise summary of the findings from the sources")
    key_points: list[str] = Field(
        description="Important facts and insights supported by the sources")
    sources: list[Source] = Field(
        description="Sources supporting the research finding"
    )

class ResearchReport(BaseModel):
    title: str = Field(
        description="A clear title for the research report"
    )

    summary: str = Field(
        description="Executive summary answering the research question"
    )

    key_findings: list[str] = Field(
        description="The most important findings from the research"
    )

    conclusion: str = Field(
        description="Final conclusion based only on the research findings"
    )