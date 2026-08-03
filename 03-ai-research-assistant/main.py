from planner import ResearchPlanner

def main():

    planner = ResearchPlanner()

    print("\nAI Research Assistant")
    print("---------------------")

    question = input("\nEnter research question: ")

    plan = planner.create_plan(question)

    print("\nResearch Topic:")
    print(plan.topic)

    print("\nResearch Plan:")

    for index, task in enumerate(plan.tasks, start=1):
        print(f"{index}. {task}")

if __name__ == "__main__":
    main()