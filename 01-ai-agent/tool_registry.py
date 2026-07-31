from tools import TOOLS


class ToolRegistry:

    def __init__(self):

        self.tools = TOOLS

        self.tool_map = {
            tool.name: tool
            for tool in self.tools
        }

    def get_tools(self):

        return self.tools

    def get_tool(self, tool_name):

        return self.tool_map.get(tool_name)
