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
        "current_finding": None,
        "current_search_results": [],
        "findings": [],
        "retry_count": 0,
        "report": None,
    }

    result = graph.invoke(initial_state)

    report = result["report"]

    print("\n" + "=" * 80)
    print(report.title)
    print("=" * 80)

    print("\nSummary")
    print(report.summary)

    print("\nKey Findings")
    for finding in report.key_findings:
        print(f"- {finding}")

    print("\nConclusion")
    print(report.conclusion)


if __name__ == "__main__":
    main()