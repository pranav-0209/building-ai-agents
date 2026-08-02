from vector_store import initialize_vector_store
from chat import ask_question


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
