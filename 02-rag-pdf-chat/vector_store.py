from langchain_chroma import Chroma

from config import get_embeddings, DATABASE_PATH


def create_vector_store(chunks):

    embeddings = get_embeddings()

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DATABASE_PATH
    )

    return vector_store