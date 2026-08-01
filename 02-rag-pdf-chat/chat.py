from config import get_llm


llm = get_llm()


def ask_question(vector_store, question):

    retriever = vector_store.as_retriever(
        search_kwargs={
            "k": 3
        }
    )

    documents = retriever.invoke(question)

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    prompt = f"""
You are a helpful AI assistant.

Answer the question using ONLY the provided context.

If the answer cannot be found in the context, say:
"I could not find this information in the document."

Context:
----------------
{context}
----------------

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content