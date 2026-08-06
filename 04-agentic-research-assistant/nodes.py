from state import ResearchState


def planner_node(state: ResearchState):

    print("\n--- PLANNER NODE ---")

    question = state["question"]

    print(f"Planning research for: {question}")

    plan = [
        "Research the main concepts related to the topic",
        "Find recent information about the topic",
        "Identify important implications",
    ]

    return {
        "plan": plan
    }

def search_node(state: ResearchState):

    print("\n--- SEARCH NODE ---")

    plan = state["plan"]

    print("Research tasks:")

    for index, task in enumerate(plan, start=1):
        print(f"{index}. {task}")

    return {
        "search_status": "Search completed"
    }