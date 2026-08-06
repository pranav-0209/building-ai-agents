from typing import TypedDict

class ResearchState(TypedDict):
    question: str
    plan: list[str]
    search_status: str