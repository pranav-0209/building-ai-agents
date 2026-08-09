from dotenv import load_dotenv

load_dotenv()

from graph import build_graph

def main():

    graph = build_graph()

    question = input("Enter your research question: ")

    initial_state = {
        "question": question,
        "plan": None,
        "current_task_index": 0,
        "current_search_results": [],
        "findings": [],
        "report": None,
    }

    final_state = graph.invoke(initial_state)

    print("\n--- FINAL STATE ---")
    print(final_state)


if __name__ == "__main__":
    main()