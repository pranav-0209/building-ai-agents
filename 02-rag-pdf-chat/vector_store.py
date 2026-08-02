import os
from langchain_chroma import Chroma

from config import( get_embeddings, DATABASE_PATH, COLLECTION_NAME )


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