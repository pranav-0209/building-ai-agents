from planner import ResearchPlanner
from researcher import Researcher


def main():

    planner = ResearchPlanner()
    researcher = Researcher()

    print("\nAI Research Assistant")
    print("---------------------")

    question = input("\nEnter research question: ")

    # Step 1: Create research plan

    plan = planner.create_plan(question)

    print("\nResearch Topic:")
    print(plan.topic)

    print("\nResearch Plan:")

    for index, task in enumerate(plan.tasks, start=1):
        print(f"{index}. {task}")

    # Step 2: Execute research

    research_results = researcher.research(plan)

    # Step 3: Display collected sources

    print("\n\nResearch Results")
    print("----------------")

    for task, results in research_results.items():

        print(f"\nTask: {task}")

        for index, result in enumerate(results, start=1):

            print(f"\n  Source {index}")
            print(f"  Title: {result.title}")
            print(f"  URL: {result.url}")
            print(f"  Content: {result.content[:300]}...")


if __name__ == "__main__":
    main()
