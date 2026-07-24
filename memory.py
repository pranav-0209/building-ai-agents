import os
import json

from langchain_core.messages import SystemMessage
from config import (WINDOW_SIZE, SUMMARY_TRIGGER, get_llm)
from repository import MemoryRepository

llm = get_llm()


class MemoryManager:

    def __init__(self):

        self.system_message = SystemMessage(
            content="You are a helpful AI assistant. Use tools whenever necessary.")

        self.repository = MemoryRepository()

        self.summary_message, self.conversation = self.repository.load()

    def add(self, message):

        self.conversation.append(message)

        self.repository.save(self.summary_message, self.conversation)

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

        self.save(self.summary_message, self.conversation)

    def get_messages(self):

        messages = [self.system_message]

        if self.summary_message:
            messages.append(self.summary_message)

        messages.extend(self.conversation)

        return messages
