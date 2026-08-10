from typing import TypedDict

from schemas import ResearchPlan, SearchResult, ResearchFinding, ResearchReport
class ResearchState(TypedDict):
    
    question: str

    plan: ResearchPlan | None

    current_task_index: int

    current_search_results: list[SearchResult]

    findings: list[ResearchFinding]

    retry_count: int

    report: ResearchReport | None