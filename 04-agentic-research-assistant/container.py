from planner import ResearchPlanner
from search import WebSearchService


class ApplicationContainer:

    def __init__(self):
        self.planner = ResearchPlanner()
        self.search = WebSearchService()