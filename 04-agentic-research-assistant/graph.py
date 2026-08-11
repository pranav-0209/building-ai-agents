from langgraph.graph import StateGraph, START, END

from container import ApplicationContainer

from state import ResearchState

from nodes import (
    planner_node,
    search_node,
    analyzer_node,
    evaluator_node,
    advance_task_node,
    report_node,
    route_next_task,
)


def build_graph():

    container = ApplicationContainer()

    builder = StateGraph(ResearchState)

    builder.add_node("planner",planner_node(container))

    builder.add_node("search",search_node(container))

    builder.add_node("analyzer",analyzer_node(container))

    builder.add_node("evaluator",evaluator_node(container))

    builder.add_node("advance",advance_task_node(container))

    builder.add_node("report",report_node(container))

    builder.add_edge(START,"planner")

    builder.add_edge("planner","search")

    builder.add_edge("search","analyzer")

    builder.add_edge("analyzer","evaluator")

    builder.add_edge("evaluator","advance")

    builder.add_conditional_edges(
        "advance",
        route_next_task,
        {
            "continue": "search",
            "finish": "report",
        },
    )

    builder.add_edge("report",END)

    return builder.compile()
