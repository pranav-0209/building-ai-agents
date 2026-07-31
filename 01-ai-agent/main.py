from agent import run_agent

print("=" * 50)
print("AI Assistant Started")
print("Type 'exit' or 'quit' to quit.")
print("=" * 50)

while True:

    question = input("\nYou: ")

    if question.lower() == "exit" or question.lower() == "quit":
        print("\nExiting AI Assistant. Goodbye!")
        break

    answer = run_agent(question)

    print("\nAssistant: ")

    print(answer)