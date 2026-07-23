from langchain_core.messages import (HumanMessage, SystemMessage, ToolMessage)

from config import (get_llm, SUMMARY_TRIGGER, WINDOW_SIZE)
from tools import TOOLS

llm = get_llm()

llm_with_tools = llm.bind_tools(TOOLS)

tool_map = {
    tool.name: tool
    for tool in TOOLS
}

messages = [
    SystemMessage(
        content="""You are a helpful AI assistant.Use tools whenever necessary."""),
]


def run_agent(user_input: str):

    messages.append(
        HumanMessage(content=user_input)
    )

    while True:

        response = llm_with_tools.invoke(messages)

        messages.append(response)

        if not response.tool_calls:
            return response.content

        for tool_call in response.tool_calls:

            tool = tool_map.get(tool_call["name"])

            if tool is None:
                messages.append(
                    ToolMessage(content=f"Tool not found: {tool_call['name']}",
                                tool_call_id=tool_call["id"])
                )

                continue

            try:

                result = tool.invoke(tool_call["args"])

            except Exception as e:

                result = str(e)

            messages.append(
                ToolMessage(content=result, tool_call_id=tool_call["id"])
            )
