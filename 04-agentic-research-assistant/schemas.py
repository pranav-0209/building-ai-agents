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


class FindingAnalysis(BaseModel):

    task: str

    summary: str

    key_points: list[str]


class ResearchFinding(BaseModel):

    task: str

    summary: str

    key_points: list[str]

    sources: list[SearchResult]

class ResearchDecision(BaseModel):
    sufficient: bool = Field(
        description="Whether the available evidence is sufficient to answer the research task."
    )

    reasoning: str = Field(
        description="Short explanation of why the evidence is or is not sufficient."
    )


class ResearchReport(BaseModel):
    title: str
    summary: str
    key_findings: list[str]
    conclusion: str
