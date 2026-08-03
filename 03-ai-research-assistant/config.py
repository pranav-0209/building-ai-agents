from langchain_ollama import ChatOllama

MODEL_NAME = "qwen3.5:4b"

def get_llm():

    return ChatOllama(
        model=MODEL_NAME,
        temperature=0,
    )