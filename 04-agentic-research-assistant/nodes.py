from container import ApplicationContainer
from state import ResearchState
from schemas import ResearchFinding


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

def analyzer_node(container: ApplicationContainer):

    def node(state: ResearchState):

        plan = state["plan"]

        if plan is None:
            raise ValueError("Research plan missing.")

        task = plan.tasks[state["current_task_index"]]

        analysis = container.analyzer.analyze(
            task,
            state["current_search_results"],
        )

        finding = ResearchFinding(
            task=analysis.task,
            summary=analysis.summary,
            key_points=analysis.key_points,
            sources=state["current_search_results"],
        )

        findings = list(state["findings"])
        findings.append(finding)

        return {
            "findings": findings,
        }

    return node
