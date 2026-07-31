from langchain_core.tools import tool

@tool
def random_number(start: int, end: int) -> str:
    """Generate a random number between start and end"""

    import random

    return str(random.randint(start, end))