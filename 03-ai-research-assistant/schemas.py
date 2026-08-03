from pydantic import BaseModel, Field

class ResearchPlan(BaseModel):
    topic: str = Field(description="The main research topic")

    tasks: list[str] = Field(description="A list of research tasks needed to investigate the topic")