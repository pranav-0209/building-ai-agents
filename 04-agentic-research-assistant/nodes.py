from container import ApplicationContainer
from state import ResearchState


def planner_node(container: ApplicationContainer):

    def node(state: ResearchState):

        question = state["question"]

        print(f"Planning research for: {question}")

        plan = container.planner.create_plan(question)

        return {
            "plan": plan
        }

    return node


def search_node(container: ApplicationContainer):

    def node(state: ResearchState):

        plan = state["plan"]

        if plan is None:
            raise ValueError("Research plan is missing.")

        task = plan.tasks[state["current_task_index"]]

        print(f"\nSearching:\n{task}")

        search_results = container.search.search_web(task)

        return {
            "current_search_results": search_results
        }

    return node
