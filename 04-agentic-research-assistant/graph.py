from langgraph.graph import StateGraph, START, END

from state import ResearchState
from nodes import planner_node, search_node


def build_graph():
    graph_builder = StateGraph(ResearchState)

    graph_builder.add_node("planner", planner_node)
    graph_builder.add_node("search", search_node)

    graph_builder.add_edge(START, "planner")
    graph_builder.add_edge("planner", "search")
    graph_builder.add_edge("search", END)

    return graph_builder.compile()
