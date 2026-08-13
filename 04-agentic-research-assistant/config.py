from langchain_ollama import ChatOllama


MODEL_NAME = "qwen3.5:4b"

MAX_RETRIES = 2


def get_llm():
    return ChatOllama(
        model=MODEL_NAME,
        temperature=0,
        reasoning=False,
    )