from schemas import ResearchPlan, SearchResult
from search import WebSearchService


class Researcher:

    def __init__(self):
        self.search_service = WebSearchService()

    def research(self, plan: ResearchPlan) -> dict[str, list[SearchResult]]:

        research_results = {}

        for task in plan.tasks:
            print(f"\nResearching: {task}")

            results = self.search_service.search(task)

            research_results[task] = results

        return research_results
