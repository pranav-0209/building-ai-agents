import json
import os

from langchain_core.messages import (
    HumanMessage, AIMessage, SystemMessage, ToolMessage)

from config import MEMORY_FOLDER
from interfaces import BaseRepostiory


class MemoryRepository(BaseRepostiory):

    def __init__(self, session_id):

        self.session_id = session_id

        os.makedirs(MEMORY_FOLDER, exist_ok=True)

        self.memory_file = os.path.join(
            MEMORY_FOLDER, f"{session_id}.json"
        )

    def save(self, summary_message, conversation):

        data = {
            "summary": None,
            "conversation": []
        }

        for msg in conversation:
            if isinstance(msg, HumanMessage):
                msg_type = "human"
            elif isinstance(msg, AIMessage):
                msg_type = "ai"
            elif isinstance(msg, ToolMessage):
                msg_type = "tool"
            else:
                continue

            item = {
                "type": msg_type,
                "content": msg.content
            }

            if isinstance(msg, ToolMessage):
                item["tool_call_id"] = msg.tool_call_id

            data["conversation"].append(item)

        with open(self.memory_file, "w", encoding="utf-8") as f:

            json.dump(data, f, ensure_ascii=False, indent=4)

    def load(self):

        if not os.path.exists(self.memory_file):
            return None, []

        try:
            with open(self.memory_file, "r", encoding="utf-8") as f:

                data = json.load(f)

        except json.JSONDecodeError:

            return None, []

        summary = None

        if data.get("summary"):

            summary = SystemMessage(content=data["summary"])

        conversation = []

        for msg in data.get("conversation", []):

            if msg["type"] == "human":

                conversation.append(HumanMessage(content=msg["content"]))

            elif msg["type"] == "ai":

                conversation.append(AIMessage(content=msg["content"]))

            elif msg["type"] == "tool":

                conversation.append(ToolMessage(
                    content=msg["content"], tool_call_id=msg.get("tool_call_id")))

        return summary, conversation
