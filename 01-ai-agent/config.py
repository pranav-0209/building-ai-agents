from pathlib import Path

from langchain_ollama import ChatOllama

MODEL_NAME = "qwen3:4b"

TEMPERATURE = 0

WINDOW_SIZE = 5

SUMMARY_TRIGGER = 10

MEMORY_FOLDER = "memory"

def get_llm():

    return ChatOllama(
        model=MODEL_NAME,
        temperature=TEMPERATURE
    )
