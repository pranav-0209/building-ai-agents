import os
import json

from langchain_core.messages import (
    SystemMessage, HumanMessage, AIMessage, ToolMessage)
from config import (WINDOW_SIZE, SUMMARY_TRIGGER, MEMORY_FILE, get_llm)

llm = get_llm()


class MemoryManager:

    def __init__(self):

        self.system_message = SystemMessage(
            content="You are a helpful AI assistant. Use tools whenever necessary.")

        self.summary_message = None

        self.conversation = []

        self.load()

    def add(self, message):

        self.conversation.append(message)

        self.save()

    def update_summary(self):

        if len(self.conversation) <= SUMMARY_TRIGGER:
            return

        old_messages = self.conversation[:-WINDOW_SIZE]
        recent_messages = self.conversation[-WINDOW_SIZE:]

        conversation_text = ""

        for msg in old_messages:

            role = msg.__class__.__name__.replace("Message", "")

            conversation_text += f"{role}: {msg.content}\n"

        current_summary = ""

        if self.summary_message:
            current_summary = self.summary_message.content.replace(
                "Conversation Summary:\n", ""
            )

        prompt = f"""
You are an expert conversation summarizer.

Below is the existing summary.

------------------------
{current_summary}
------------------------

Below is the new conversation.

------------------------
{conversation_text}
------------------------

Update the summary.

Instructions:

- Preserve important existing facts.
- Add new information.
- Remove duplicate information.
- Update facts if they changed.
- Ignore greetings and small talk.
- Return ONLY the updated summary.
"""

        updated_summary = llm.invoke(prompt).content.strip()

        self.summary_message = SystemMessage(
            content=f"Conversation Summary:\n{updated_summary}"
        )

        self.conversation = recent_messages

        self.save()

    def get_messages(self):

        messages = [self.system_message]

        if self.summary_message:
            messages.append(self.summary_message)

        messages.extend(self.conversation)

        return messages

    def save(self):

        data = {
            "summary": None,
            "conversation": []
        }

        if self.summary_message:
            data["summary"] = self.summary_message.content

        for msg in self.conversation:

            if isinstance(msg, HumanMessage):
                msg_type = "human"

            elif isinstance(msg, AIMessage):
                msg_type = "ai"

            elif isinstance(msg, ToolMessage):
                msg_type = "tool"

            else:
                continue

            data["conversation"].append({
                "type": msg_type,
                "content": msg.content
            })

        with open(MEMORY_FILE, "w", encoding="utf-8") as f:

            json.dump(data, f, indent=4)

    def load(self):

        if not os.path.exists(MEMORY_FILE):
            return

        try:

            with open(MEMORY_FILE, "r", encoding="utf-8") as f:

                raw_data = f.read().strip()

                if not raw_data:
                    return

                data = json.loads(raw_data)

        except json.JSONDecodeError:

            return

        if data.get("summary"):
            self.summary_message = SystemMessage(content=data["summary"])

        for msg in data.get("conversation", []):

            if msg["type"] == "human":

                self.conversation.append(HumanMessage(content=msg["content"]))

            elif msg["type"] == "ai":

                self.conversation.append(AIMessage(content=msg["content"]))

            elif msg["type"] == "tool":

                self.conversation.append(ToolMessage(
                    content=msg["content"], tool_call_id=""))
