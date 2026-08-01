from config import PDF_PATH

from loader import load_pdf
from splitter import split_documents
from vector_store import create_vector_store
from chat import ask_question


def main():

    print("Loading PDF...")

    documents = load_pdf(PDF_PATH)

    print(
        f"Loaded {len(documents)} pages."
    )

    print("Splitting documents...")

    chunks = split_documents(documents)

    print(
        f"Created {len(chunks)} chunks."
    )

    print("Creating vector store...")

    vector_store = create_vector_store(chunks)

    print("Vector store created.")

    print("\nPDF Chat Ready!")
    print("Type 'exit' or 'quit' to stop.")

    while True:

        question = input("\nYou: ")

        if question.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        answer = ask_question(
            vector_store,
            question
        )

        print(f"\nAssistant: {answer}")


if __name__ == "__main__":
    main()