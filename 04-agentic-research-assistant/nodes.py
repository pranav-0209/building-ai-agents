from planner import ResearchPlanner
from search import WebSearchService
from state import ResearchState

planner = ResearchPlanner()
search_service = WebSearchService()


def planner_node(state: ResearchState):

    question = state["question"]

    print(f"Planning research for: {question}")

    plan = planner.create_plan(question)

    return {
        "plan": plan
    }


def search_node(state: ResearchState):

    plan = state["plan"]

    if plan is None:
        raise ValueError("Research plan is missing.")

    task = plan.tasks[state["current_task_index"]]

    print(f"\nSearching:\n{task}")

    search_results = search_service.search_web(task)

    return {
        "current_search_results": search_results
    }
