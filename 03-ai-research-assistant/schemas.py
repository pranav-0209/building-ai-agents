from pydantic import BaseModel, Field


class ResearchPlan(BaseModel):
    topic: str = Field(description="The main research topic")

    tasks: list[str] = Field(
        description="A list of research tasks needed to investigate the topic")


class SearchResult(BaseModel):
    title: str
    url: str
    content: str


class ResearchFinding(BaseModel):
    task: str = Field(description="The research task being investigated")
    summary: str = Field(
        description="A concise summary of the findings from the sources")
    key_points: list[str] = Field(
        description="Important facts and insights supported by the sources")
    source_urls: list[str] = Field(
        description="URLs of the sources supporting the findings")
