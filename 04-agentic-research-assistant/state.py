from typing import TypedDict

from schemas import ResearchPlan, SearchResult
class ResearchState(TypedDict):
    
    question: str

    plan: ResearchPlan | None

    current_task_index: int

    current_search_results: list[SearchResult]

    findings: list

    report: str | None