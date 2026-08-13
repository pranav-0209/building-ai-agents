import re

from langchain_core.prompts import ChatPromptTemplate

from config import get_llm
from schemas import ResearchPlan


class ResearchPlanner:

    def __init__(self):

        self.llm = get_llm()

        self.prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
You are an expert research planner.

Your job is to break a user's topic into small,
independent research tasks.

Rules:

1. Generate between 3 and 7 tasks.

2. Each task must answer ONLY ONE research question.

3. Each task should be answerable using
approximately 3-5 web pages.

4. Never combine multiple objectives into one task.

5. Avoid words like:
   - comprehensive
   - complete
   - entire
   - all aspects

6. Focus on facts that can realistically be gathered
through web search.

7. The final comparison or synthesis will be performed
later by another component.
"""
                ),
                (
                    "human",
                    "{question}",
                ),
            ]
        )

        self.chain = self.prompt | self.llm

    def _parse_tasks(self, text: str) -> list[str]:

        tasks: list[str] = []

        for line in text.splitlines():

            stripped = line.strip()

            if not stripped:
                continue

            match = re.match(r"^(?:\d+[\).:-]?\s+|[-*]\s+)(.+)$", stripped)

            if match:
                task = match.group(1).strip()

                if task:
                    tasks.append(task)

        if tasks:
            return tasks[:7]

        return [line.strip() for line in text.splitlines() if line.strip()][:7]

    def create_plan(self, question: str) -> ResearchPlan:

        for attempt in range(3):

            response = self.chain.invoke({"question": question})

            content = getattr(response, "content", str(response)).strip()

            if content:
                return ResearchPlan(
                    topic=question,
                    tasks=self._parse_tasks(content),
                )

            print(
                f"Planner returned an empty response "
                f"(attempt {attempt + 1}/3). Retrying..."
            )

        raise RuntimeError("Planner returned an empty response after 3 attempts.")
