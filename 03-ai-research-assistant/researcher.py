from schemas import ResearchPlan, SearchResult, ResearchFinding
from search import WebSearchService
from analyzer import ResearchAnalyzer


class Researcher:

    def __init__(self):
        self.search_service = WebSearchService()
        self.analyzer = ResearchAnalyzer()

    def research(self, plan: ResearchPlan) -> list[ResearchFinding]:

        findings = []

        for task in plan.tasks:
            print(f"\nResearching: {task}")

            search_results = self.search_service.search(task)

            if not search_results:
                print(f"No results found for task: {task}")
                continue

            finding = self.analyzer.analyze(
                task=task, search_results=search_results)

            findings.append(finding)

        return findings
