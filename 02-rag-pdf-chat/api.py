from fastapi import FastAPI

from schemas import (ChatRequest, ChatResponse)

from vector_store import initialize_vector_store
from chat import ask_question

app = FastAPI(
    title="RAG PDF Chat API",
    description="An API for a Retrieval-Augmented Generation (RAG) PDF Chat application.",
    version="1.0.0"
)

vector_store = initialize_vector_store()


@app.get("/")
def root():
    return {"message": "PDF RAG API is running"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    answer, documents = ask_question(
        vector_store,
        request.question
    )

    pages = set()

    for document in documents:
        page = document.metadata.get("page")

        if page is not None:
            pages.add(page + 1)

    return ChatResponse(
        answer=answer,
        sources=sorted(pages)
    )
