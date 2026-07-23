from langchain_ollama import ChatOllama

MODEL_NAME = "qwen3:4b"

TEMPERATURE = 0

WINDOW_SIZE = 10

SUMMARY_TRIGGER = 15

def get_llm():

    return ChatOllama(
        model=MODEL_NAME,
        temperature=TEMPERATURE
    )
