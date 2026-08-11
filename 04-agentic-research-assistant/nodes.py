from container import ApplicationContainer
from state import ResearchState
from schemas import ResearchFinding


def get_plan(state: ResearchState):
    plan = state["plan"]

    if plan is None:
        raise ValueError("Research plan is missing.")

    return plan


def get_current_task(state: ResearchState):
    plan = get_plan(state)
    return plan.tasks[state["current_task_index"]]


def planner_node(container: ApplicationContainer):

    def node(state: ResearchState):

        question = state["question"]

        print(f"\nPlanning research for:\n{question}")

        plan = container.planner.create_plan(question)

        return {
            "plan": plan,
        }

    return node


def search_node(container: ApplicationContainer):

    def node(state: ResearchState):

        task = get_current_task(state)

        print(f"\nSearching:\n{task}")

        search_results = container.search.search_web(task)

        return {
            "current_search_results": search_results,
        }

    return node


def analyzer_node(container: ApplicationContainer):

    def node(state: ResearchState):

        task = get_current_task(state)

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


def evaluator_node(container: ApplicationContainer):

    def node(state: ResearchState):

        finding = state["findings"][-1]

        evaluation = container.evaluator.evaluate(finding)

        print("\nEvaluation")
        print("----------------")
        print(f"Sufficient : {evaluation.sufficient}")
        print(f"Reason      : {evaluation.reasoning}")

        return {}

    return node


def advance_task_node(container: ApplicationContainer):

    def node(state: ResearchState):

        next_index = state["current_task_index"] + 1

        print(
            f"\nCompleted task {next_index}"
        )

        return {
            "current_task_index": next_index,
        }

    return node


def route_next_task(state: ResearchState):

    plan = get_plan(state)

    if state["current_task_index"] < len(plan.tasks):
        return "continue"

    return "finish"

def report_node(container: ApplicationContainer):

    def node(state: ResearchState):

        print("\nResearch Completed")
        print("=" * 60)

        for index, finding in enumerate(state["findings"], start=1):

            print(f"\nFinding {index}")
            print(f"Task: {finding.task}")
            print(f"Summary: {finding.summary}")

        return {}

    return node