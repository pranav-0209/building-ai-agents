from container import ApplicationContainer
import container
from state import ResearchState
from schemas import ResearchFinding
from config import MAX_RETRIES


def get_plan(state: ResearchState):
    plan = state["plan"]

    if plan is None:
        raise ValueError("Research plan is missing.")

    return plan


def get_current_task(state: ResearchState):
    plan = get_plan(state)
    return plan.tasks[state["current_task_index"]]


def route_after_evaluation(state: ResearchState):

    finding = state["current_finding"]

    if finding is None:
        return "retry"

    if finding.is_sufficient:
        return "advance"

    return "retry"


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

        return {
            "current_finding": finding,
        }

    return node


def evaluator_node(container: ApplicationContainer):

    def node(state: ResearchState):

        finding = state["current_finding"]

        if finding is None:
            raise ValueError("Current finding is missing.")

        evaluation = container.evaluator.evaluate(finding)

        print("\nEvaluation")
        print("----------------")
        print(f"Sufficient : {evaluation.sufficient}")
        print(f"Reason      : {evaluation.reasoning}")

        finding.is_sufficient = evaluation.sufficient

        return {
            "current_finding": finding,
        }

    return node


def advance_task_node(container: ApplicationContainer):

    def node(state: ResearchState):

        finding = state["current_finding"]

        if finding is None:
            raise ValueError("Current finding is missing.")

        findings = list(state["findings"])
        findings.append(finding)

        next_index = state["current_task_index"] + 1

        print(f"\nCompleted task {next_index}")

        return {
            "findings": findings,
            "current_finding": None,
            "current_task_index": next_index,
            "retry_count": 0,
        }

    return node


def route_next_task(state: ResearchState):

    plan = get_plan(state)

    if state["current_task_index"] < len(plan.tasks):
        return "continue"

    return "report"

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


def retry_node(state: ResearchState):

    retry_count = state["retry_count"] + 1

    print(f"\nRetry attempt {retry_count}")

    return {
        "retry_count": retry_count,
    }

def route_after_retry(state: ResearchState):

    if state["retry_count"] >= MAX_RETRIES:

        print("\nMaximum retries reached. Moving to next task.")

        return "advance"

    return "search"

def report_node(state: ResearchState):

    print("\nGenerating final report...")

    report = container.report_generator.generate(
        question=state["question"],
        findings=state["findings"],
    )

    return {
        "report": report,
    }