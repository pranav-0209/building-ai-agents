from typing import TypedDict

from schemas import ResearchPlan
class ResearchState(TypedDict):
    
    question: str

    plan: ResearchPlan | None

    current_task_index: int

    current_search_results: list

    findings: list

    report: str | None