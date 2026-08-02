import os
from langchain_chroma import Chroma

from config import (PDF_PATH, get_embeddings, DATABASE_PATH, COLLECTION_NAME)

from loader import load_pdf
from splitter import split_documents


def create_vector_store(chunks):

    embeddings = get_embeddings()

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DATABASE_PATH,
        collection_name=COLLECTION_NAME
    )

    return vector_store


def load_vector_store():

    embeddings = get_embeddings()

    vector_store = Chroma(
        persist_directory=DATABASE_PATH,
        embedding_function=embeddings,
        collection_name=COLLECTION_NAME
    )

    return vector_store


def vector_store_exists():

    return os.path.exists(DATABASE_PATH) and bool(os.listdir(DATABASE_PATH))


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
