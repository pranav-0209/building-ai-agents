from langchain_core.messages import (HumanMessage, ToolMessage)

from config import (get_llm)
from memory import MemoryManager
from repository import MemoryRepository
from tools import TOOLS

llm = get_llm()

llm_with_tools = llm.bind_tools(TOOLS)

tool_map = {
    tool.name: tool
    for tool in TOOLS
}

repository = MemoryRepository(session_id="session_002")

memory = MemoryManager(repository)

def run_agent(user_input: str):

    memory.add(
        HumanMessage(content=user_input)
    )

    memory.update_summary()

    while True:

        response = llm_with_tools.invoke(memory.get_messages())

        memory.add(response)

        if not response.tool_calls:
            return response.content

        for tool_call in response.tool_calls:

            tool = tool_map.get(tool_call["name"])

            if tool is None:
                memory.add(
                    ToolMessage(content=f"Tool not found: {tool_call['name']}",
                                tool_call_id=tool_call["id"])
                )

                continue

            try:

                result = tool.invoke(tool_call["args"])

            except Exception as e:

                result = str(e)

            memory.add(
                ToolMessage(content=result, tool_call_id=tool_call["id"])
            )

            memory.update_summary()
