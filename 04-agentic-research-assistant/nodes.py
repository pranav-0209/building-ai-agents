from planner import ResearchPlanner
from state import ResearchState

planner = ResearchPlanner()


def planner_node(state: ResearchState):

    print("\n--- PLANNER NODE ---")

    question = state["question"]

    print(f"Planning research for: {question}")

    plan = planner.create_plan(question)

    return {
        "plan": plan
    }


def search_node(state: ResearchState):

    print("\n--- SEARCH NODE ---")

    plan = state["plan"]

    if plan is None:
        raise ValueError("Research plan is missing.")

    print(f"\nResearch topic: {plan.topic}")
    print("\nResearch tasks:")

    for index, task in enumerate(plan.tasks, start=1):
        print(f"{index}. {task}")

    return {
        "search_status": "Search ready"
    }
