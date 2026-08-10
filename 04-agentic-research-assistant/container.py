from planner import ResearchPlanner
from search import WebSearchService
from analyzer import ResearchAnalyzer
from evaluator import ResearchEvaluator


class ApplicationContainer:

    def __init__(self):
        self.planner = ResearchPlanner()
        self.search = WebSearchService()
        self.analyzer = ResearchAnalyzer()
        self.evaluator = ResearchEvaluator()