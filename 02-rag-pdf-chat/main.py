from config import PDF_PATH

from loader import load_pdf
from splitter import split_documents
from vector_store import (
    create_vector_store, load_vector_store, vector_store_exists)
from chat import ask_question


def initialize_vector_store():

    if vector_store_exists():

        print("Loading existing vector store...")

        return load_vector_store()

    print("No vector store found.")
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

    print("Generating embeddings...")

    vector_store = create_vector_store(chunks)

    print("Vector store created.")

    return vector_store


def display_sources(documents):

    pages = set()

    for document in documents:

        page = document.metadata.get("page")

        if page is not None:
            pages.add(page + 1)

    if pages:

        sorted_pages = sorted(pages)

        page_text = ", ".join(
            f"Page {page}"
            for page in sorted_pages
        )

        print(f"\nSources: {page_text}")


def main():

    vector_store = initialize_vector_store()

    print("\nPDF Chat Ready!")
    print("Type 'exit' or 'quit' to stop.")

    while True:

        question = input("\nYou: ")

        if question.lower() in ["exit", "quit"]:

            print("\nGoodbye!")

            break

        answer, documents = ask_question(
            vector_store,
            question
        )

        print(f"\nAssistant: {answer}")

        display_sources(documents)


if __name__ == "__main__":
    main()
