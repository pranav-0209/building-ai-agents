from langchain_ollama import ChatOllama, OllamaEmbeddings

MODEL_NAME = "qwen3:4b"

EMBEDDING_MODEL = "nomic-embed-text"

TEMPERATURE = 0

PDF_PATH = "data/sample.pdf"

DATABASE_PATH = "database"


def get_llm():

    return ChatOllama(
        model=MODEL_NAME,
        temperature=TEMPERATURE
    )


def get_embeddings():

    return OllamaEmbeddings(
        model=EMBEDDING_MODEL
    ) 