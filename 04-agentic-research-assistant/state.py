from typing import TypedDict

from schemas import ResearchPlan, SearchResult, ResearchFinding
class ResearchState(TypedDict):
    
    question: str

    plan: ResearchPlan | None

    current_task_index: int

    current_search_results: list[SearchResult]

    findings: list[ResearchFinding]

    report: str | None