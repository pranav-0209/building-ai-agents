from langgraph.graph import StateGraph, START, END

from container import ApplicationContainer
from state import ResearchState
from nodes import planner_node, search_node


def build_graph():

    container = ApplicationContainer()

    graph_builder = StateGraph(ResearchState)

    graph_builder.add_node("planner", planner_node(container))
    graph_builder.add_node("search", search_node(container))

    graph_builder.add_edge(START, "planner")
    graph_builder.add_edge("planner", "search")
    graph_builder.add_edge("search", END)

    return graph_builder.compile()
