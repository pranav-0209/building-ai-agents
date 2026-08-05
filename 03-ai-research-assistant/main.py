from planner import ResearchPlanner
from researcher import Researcher
from reporter import ReportGenerator
from sources import collect_unique_sources

from dotenv import load_dotenv

load_dotenv()

def main():

    planner = ResearchPlanner()
    researcher = Researcher()
    reporter = ReportGenerator()

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

    if not findings:
        print("\nNo research findings were generated.")
        return

    # Step 3: Generate final report

    print("\nGenerating final research report...")

    report = reporter.generate(
        question=question,
        findings=findings
    )

    # Step 4: Collect sources

    sources = collect_unique_sources(findings)

    # Step 5: Display report

    print("\n")
    print("=" * 60)
    print(report.title)
    print("=" * 60)

    print("\nSummary")
    print("-------")
    print(report.summary)

    print("\nKey Findings")
    print("------------")

    for index, finding in enumerate(
        report.key_findings,
        start=1
    ):
        print(f"{index}. {finding}")

    print("\nConclusion")
    print("----------")
    print(report.conclusion)

    print("\nSources")
    print("-------")

    for index, source in enumerate(
        sources,
        start=1
    ):
        print(f"[{index}] {source.title}")
        print(f"    {source.url}")


if __name__ == "__main__":
    main()