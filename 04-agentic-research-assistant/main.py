from graph import build_graph

def main():

    graph = build_graph()

    question = input("Enter your research question: ")

    initial_state = {
        "question": question,
        "plan": None,
        "search_status": ""
    }

    final_state = graph.invoke(initial_state)

    print("\n--- FINAL STATE ---")
    print(final_state)


if __name__ == "__main__":
    main()