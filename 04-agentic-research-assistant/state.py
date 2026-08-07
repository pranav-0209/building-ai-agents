from typing import TypedDict

from schemas import ResearchPlan
class ResearchState(TypedDict):
    question: str
    plan: ResearchPlan | None
    search_status: str