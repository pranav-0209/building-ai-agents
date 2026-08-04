from planner import ResearchPlanner
from researcher import Researcher

from dotenv import load_dotenv

load_dotenv()

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

    findings = researcher.research(plan)

    # Step 3: Display analyzed findings

    print("\n\nResearch Findings")
    print("-----------------")

    for index, finding in enumerate(findings, start=1):

        print(f"\nFinding {index}")
        print("=" * 40)

        print(f"\nTask:")
        print(finding.task)

        print(f"\nSummary:")
        print(finding.summary)

        print("\nKey Points:")

        for point in finding.key_points:
            print(f"- {point}")

        print("\nSources:")

        for url in finding.source_urls:
            print(f"- {url}")


if __name__ == "__main__":
    main()
